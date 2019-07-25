#!/bin/bash
# Kaldi

# Convert *.wav files to some other frequencies 
# Directory Structure: run.sh  out  wav
# wav: folder contains all *.wav files; out: Result *.wav; run.sh code see below.
# sudo run.sh
sudo apt-get install ffmpeg
for file in wav/*; do
  #sox -S $file out/${file##*/} rate -L -s 8000
  #sox $file -r 8000 -c 1 -b 32 out/${file##*/}
  ffmpeg -i $file -ar 8000 out/${file##*/}
  echo "${file##*/}"
done
sudo chmod 777 out/*
exit 1