# Give all .wav files in folder audio_out/sub_folder/  .
#
# Run:
# python3 train_text_generator.py
# Get train_text accordingly.

import subprocess
subprocess.call(['./get_file_names.sh'])

with open('sorted_file_names') as f:
    content = f.readlines()

f = open("corpora.txt")
f_out = open('train_text', 'w')

lines = f.readlines()


for x in content:
    line_no = int(x[10:16].strip('\n')) # from 10th to 16th character is line no from corpora.txt
    print(x.strip('\n') + ' '+ lines[line_no-1].strip('\n'))
    f_out.write(x.strip('\n') + ' '+ lines[line_no-1])




f_out.close()
f.close()

exit (1)