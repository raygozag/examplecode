#!/bin/bash


chr=$(echo ${1}|awk -F'\:' '{print $1}')
echo ${chr}
pos=$(echo ${1}|awk -F'\:' '{print $2}')

echo 'chr'${chr}' '${pos}' '${pos} | ./ucsc.pl -d hg19 -p snp151:::