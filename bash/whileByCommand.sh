#!/bin/bash

n=0
command=$1
while ! $command && [ $n -le 5 ]; do
    sleep $n
    ((n=n+1))
    echo "Retru #$n."
    sleep 1
done

# for exect ./retry.sh ./retry.py

