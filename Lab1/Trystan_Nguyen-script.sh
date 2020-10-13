#!/bin/bash
dir="${PWD}/*"
for f in $dir
do
    var=1
    while IFS= read -r line
    do
	[[ $((var%2)) == 0 ]] && echo $(basename $f): $line
	var=$var+1
    done < $f
done
