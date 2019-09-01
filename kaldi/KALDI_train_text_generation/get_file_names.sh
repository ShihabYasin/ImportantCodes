#!/bin/bash  
rm list_of_files;
rm sorted_file_names;
rm list_of_files_no_ext;


for D in audio_out/*; do
    if [ -d "${D}" ]; then
        ls ${D} >> list_of_files
    fi
done

sed -i -e 's/.wav//g'  list_of_files # .wav ext removed
perl -lne 'length()>13 && print' list_of_files > list_of_files_no_ext

cat list_of_files_no_ext | sort > sorted_file_names

exit 1
