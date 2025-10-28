#!/bin/sh
set -e
url=https://code.exim.org/exim/exim.git
package=exim
tag=exim-4.99
#branch=exim-4.97+fixes
branch=master
out=$package-git.patch
repo=$package.git

# use filterdiff, etc to exclude bad chunks from diff
filter() {
    filterdiff \
        -x '*/Readme.pod' \
        -x '*/test/*' \
        -x '*/doc/*' \
        -x '*/release-process/*'
}

if [ ! -d $repo ]; then
	git clone --bare $url -b $branch $repo
fi

cd $repo
	git fetch origin +$branch:$branch +refs/tags/$tag:refs/tags/$tag
	git log -p --reverse --first-parent $tag..$branch ":(exclude)doc/doc-*" ":(exclude)test" ":(exclude).*" | filter > ../$out.tmp
cd ..

if cmp -s $out{,.tmp}; then
	echo >&2 "No new diffs..."
	rm -f $out.tmp
	exit 0
fi
mv -f $out{.tmp,}

../md5 $package.spec
../dropin $out
