#!/bin/bash  
## git upload auto script - example script
## CLASS_PROGRAMMING 
cd CLASS_PROGRAMMING/
git add .

currentDate=`date +"%Y-%m-%d %T"`
git commit -m  currentDate
git pull origin master 
git push origin master 


exit 1
