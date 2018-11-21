#!/usr/bin/env bash
# see https://gist.github.com/adamjohnson/5682757
echo "# test-ideas" >> README.md
#git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/fenwk0/test-ideas.git
git push -u origin master