#!/bin/bash

#
# This script downloads browser client libraries.
# Currently all scripts are downloaded from GitHub.
#
# Versions used may be changed by altering the lines
# starting with 'downloadFromGithub' at the bottom.
# The last argument is expected to be a git ref (ie
# a branch name, tag or commit-ish).
# 

set -e

DEST=$(dirname $(dirname $0))/static/libs

# Github download helper
#   $1	destination directory name under static/libs
#   $2  github repo name (user-or-org/repo)
#   $3  ref to use (branch or tag or commit)
function downloadFromGithub()
{
	local dest=$DEST/$1
	local repo=$2
	local ref=$3

	echo "* Downloading $repo ($ref) from Github..."
	wget -O temp.zip -q https://github.com/${repo}/archive/${ref}.zip
	unzip -q temp.zip
	mv $(basename ${repo})* ${dest}
	rm temp.zip
}

set -e

[ -d ${DEST} ] && rm -r ${DEST}
mkdir -p ${DEST}

downloadFromGithub jquery jquery/jquery 2.1.4
downloadFromGithub fontawesome FortAwesome/Font-Awesome v4.3.0
downloadFromGithub flag-icon-css lipis/flag-icon-css 0.7.1
downloadFromGithub bootstrap twbs/bootstrap v3.3.5

echo "* Done."
