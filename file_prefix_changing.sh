#!/bin/bash

dir="file-dir......"
for file in "$dir"/*; do
	string=${file##*/}
	prefix="s01_"
	foo=${string#"$prefix"}
	
	n="a01-133x-"${foo//_/$'-'}
	m="file-dir......"${n}
	mv $file $m
	
done
