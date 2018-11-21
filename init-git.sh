#!/usr/bin/env bash
echo "# test-ideas" >> README.md
#git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/fenwk0/test-ideas.git
git push -u origin master