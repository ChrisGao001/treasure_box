#!/bin/bash

tool_path=$(cd `dirname $0`;pwd)
cd $tool_path
bird_path="${tool_path}/birds/"


for dir in $(ls $bird_path);do
	rm -rf ${tool_path}/train/$dir
	rm -rf ${tool_path}/validation/$dir
	mkdir -p ${tool_path}/train/$dir
	mkdir -p ${tool_path}/validation/$dir
	i=1
	for file in $(find ${bird_path}/$dir -type f -name '*.jpg');do
		if [[ $i -le 90 ]];then
			image_file_dest="${tool_path}/train/$dir/"
		else
			image_file_dest="${tool_path}/validation/$dir/"
		fi
		cp $file $image_file_dest
		echo $file  $image_file_dest
		
		((i += 1))
	done
done
	
