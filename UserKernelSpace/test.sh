#!/bin/bash 

while true; do
    echo "Writing to files"	
    grep "cpu0" /proc/stat | awk '{print $2}' >> userfile.txt 
    grep "cpu0" /proc/stat | awk '{print $4}' >> kernelfile.txt
    sleep 5
done 
