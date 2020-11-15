#!/bin/bash
## git upload auto script - example script

## Pass repo_path as 1st argument
# example usage: sudo ./git_commit_auto_script.sh  https://github.com/<UserName>/<RepoName>

if [ "$0" == "-h" ]; then
  echo "Usage: `sudo ./git_commit_auto_script.sh $repolink` [somestuff]"
  return
fi

PATH_REPO=$1

cd $PATH_REPO
git add .

currentDate=$(date +"%Y-%m-%d %T")
git commit -m currentDate
git pull origin master
git push origin master

exit 1
