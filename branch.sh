#!/bin/sh
set -e
url=https://code.exim.org/exim/exim.git
package=exim
tag=4.99.3
#branch=exim-4.97+fixes
branch=master
out=$package-git.patch
repo=$package.git

# Filter out files we do not ship from the generated git patch.
filter() {
	filterdiff \
		-x '*/Readme.pod' \
		-x '*/README.md' \
		-x '*/SECURITY.md' \
		-x '*/test/*' \
		-x '*/doc/*' \
		-x '*/release-process/*'
}

review_log() {
	base=$1

	echo "# Review base: $git_tag"
	echo "# Target branch: $branch"
	echo "#"

	if [ -n "$(git rev-list --max-count=1 "$base..refs/tags/$git_tag")" ]; then
		echo "# Commits only in $git_tag (removed by the resulting patch):"
		git log --first-parent "$base..refs/tags/$git_tag" | sed 's/^/# /'
		echo "#"
	fi

	echo "# Commits only in $branch (present in the resulting patch):"
	git log --first-parent "$base..refs/heads/$branch" | sed 's/^/# /'
	echo
}

git_tag=$tag
case $git_tag in
	"$package"-*) ;;
	*) git_tag=$package-$git_tag ;;
esac

if [ ! -d "$repo" ]; then
	git clone --bare "$url" -b "$branch" "$repo"
fi

cd "$repo"
	git fetch origin \
		"+refs/heads/$branch:refs/heads/$branch" \
		"+refs/tags/$git_tag:refs/tags/$git_tag"
	base=$(git merge-base "refs/tags/$git_tag" "refs/heads/$branch")
	{
		review_log "$base"
		# The applyable payload must be a tree diff from the tarball tag to the
		# target branch. A commit-by-commit "git log -p" stream is useful for
		# review, but it may not replay cleanly when the tag and branch diverge.
		git diff "refs/tags/$git_tag" "refs/heads/$branch" \
			-- \
			src \
			":(exclude)src/.*" | filter
	} > "../$out.tmp"
cd ..

if [ -f "$out" ] && cmp -s "$out" "$out.tmp"; then
	echo >&2 "No new diffs..."
	rm -f "$out.tmp"
	exit 0
fi
mv -f "$out.tmp" "$out"

../md5 "$package.spec"
../dropin "$out"
