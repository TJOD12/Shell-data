#!/bin/bash 

# i: The number of iterations performed in the while loop
# This determines e execution time (roughly) as sleep time is 3 seconds (e=i*3)
i=$1

c=0
written=false

while [ $c -lt $i ]; do
    # only need to call free once
    totalMetrics=$(free -m)

    # only record the total RAM once, as it isn't a dynamic value
    if [ "$written" = false ]; then
        totalSpace=$(echo $totalMetrics | awk '{print $8}')
        echo "$totalSpace" > total.txt
        written=true
    fi

    # record used space each iteration
    usedSpace=$(echo $totalMetrics | awk '{print $9}')
    echo "$usedSpace" >> used.txt

    # display iteration progress
    echo "->"
    sleep 3

    # increment the counter 
    c=$(( c + 1))
done

# call the python plotting file and pass the files to read the data from
python3 plot.py total.txt used.txt