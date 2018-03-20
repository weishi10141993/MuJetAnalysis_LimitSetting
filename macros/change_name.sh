#!bin/bash

for file in sh/1_ITER_BKP/OutPut_*_T50000_*.txt
do
    echo $file
    mv "${file}" "${file/.txt/_1Iter.txt}"
done
