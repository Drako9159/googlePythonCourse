#!/bin/bash
# n is a variable
# if n is less than or equal to 5
n=1
while [ $n -le 5 ]; do
    echo "Looping ... number $n"
    ((n+=1))
done

# other loop
for fruit in peach orange apple; do
    echo "I like $fruit pie."
done