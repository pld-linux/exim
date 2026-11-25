#!/bin/sh
# Smoke test of a freshly built exim binary, run unprivileged from %build.
# Usage: exim-smoke-test.sh path/to/exim version
#
# Exim drops privileges for a -C config, so the config names the calling user
# as exim_user, says it is meant to run unprivileged (deliver_drop_privilege)
# and keeps spool, log and mailboxes in a scratch directory.

exim=$(cd "$(dirname "$1")" && pwd)/$(basename "$1")
version=$2
failed=0

if [ "$(id -u)" = 0 ]; then
	echo "exim-smoke-test: skipped, exim_user cannot be root" >&2
	exit 0
fi

T=$(mktemp -d "${TMPDIR:-/tmp}/exim-test.XXXXXX") || exit 1
trap 'rm -rf "$T"' EXIT
mkdir "$T/spool" "$T/log" "$T/mail"

cat > "$T/exim.conf" <<EOF
exim_path = $exim
primary_hostname = test.example.com
exim_user = $(id -un)
exim_group = $(id -gn)
spool_directory = $T/spool
log_file_path = $T/log/%slog
deliver_drop_privilege = true
keep_environment =

begin routers

local:
  driver = accept
  domains = test.example.com
  local_parts = user
  transport = mbox

begin transports

mbox:
  driver = appendfile
  file = $T/mail/\$local_part_data
  user = $(id -un)
EOF

run() {
	"$exim" -C "$T/exim.conf" "$@" 2>&1
}

# fail WHAT DETAIL...: report a failed test, detail cut to a few lines
fail() {
	echo "FAIL: $1"
	shift
	printf '%s\n' "$@" | head -n 6 | sed 's/^/  /'
	failed=$((failed + 1))
}

# expand STRING EXPECTED: exim -be prints the result or "Failed: <reason>"
expand() {
	got=$(run -be "$1")
	[ "$got" = "$2" ] || fail "$1" "expected: $2" "got:      $got"
}

# exim -bV
got=$(run -bV)
case "$got" in
"Exim version $version "*) ;;
*) fail "-bV" "$got" ;;
esac

# Expansions
expand '${if bool{0}{yes}{no}} ${if !bool{0}{yes}{no}}' 'no yes'
expand '${sha256:abc}' 'BA7816BF8F01CFEA414140DE5DAE2223B00361A396177A9CB410FF61F20015AD'

# ${extract} and ${listextract} field numbers (exim-extract-*.patch)
expand '${extract{2fa}{2fa=on 3x=off}}' 'on'
expand '${extract{99999abc}{a=1}{wups}{expected-notfound}}' 'expected-notfound'
expand '${extract{10000}{:}{a:b:c:d:e}{yes}{no}}' 'no'
expand '${extract{10001}{:}{a:b:c:d:e}{yes}{no}}' 'Failed: extract: field number too large'
expand '${extract{-4294967296}{:}{a:b:c:d:e}{yes}{no}}' 'Failed: extract: field number too large'
expand '${listextract{10000}{a:b:c:d:e}{ouch}{expected-notfound}}' 'expected-notfound'
expand '${listextract{10001}{a:b:c:d:e}{bad1}{bad2}}' 'Failed: listextract: field number too large'

# ${eval} overflow (exim-eval-overflow-check.patch)
expand '${eval:4611686018427387904+1}' '4611686018427387905'
expand '${eval:9223372036854775807+1}' \
	'Failed: error in expression evaluation: overflow in sum (after processing "9223372036854775807+1")'
expand '${eval:-9223372036854775807-2}' \
	'Failed: error in expression evaluation: overflow in difference (after processing "-9223372036854775807-2")'

# forall_json/forany_json (exim-forall-json-unwrap.patch)
expand '${if forany_json{[1,2]}{eq{$item}{2}}{yes}{no}}' 'yes'
expand '${if forany_json{}{eq{$item}{1}}{yes}{no}}' 'no'
# the spec leaves an empty forall open; the json form must match the plain one
expand '${if forall_json{}{eq{$item}{1}}{yes}{no}}' \
	"$(run -be '${if forall{}{eq{$item}{1}}{yes}{no}}')"
expand '${if forany_json{1}{eq{$item}{1}}{yes}{no}}' 'no'
expand '${if or{{eq{1}{1}}{forany_json{[1]}{eq{$item}{1}}}}{yes}{no}}' 'yes'

# Routing and local delivery
got=$(run -bt user@test.example.com)
case "$got" in
*"router = local, transport = mbox"*) ;;
*) fail "-bt user@test.example.com" "$got" ;;
esac

got=$(run -odf -oi -f sender@example.com user@test.example.com <<EOF
Subject: smoke test

delivered body
EOF
)
[ -z "$got" ] || fail "delivery" "$got"
grep -qx 'delivered body' "$T/mail/user" 2>/dev/null ||
	fail "delivery: body not in mailbox" "$(cat "$T/log/mainlog" 2>/dev/null)"

if [ $failed -gt 0 ]; then
	echo "exim-smoke-test: $failed test(s) failed"
	exit 1
fi
echo "exim-smoke-test: all tests passed"
