#!/bin/bash
#change name of all files in a directory to have a .html extension
for file in *.HTM; do
    name=$(basename "$file" .HTM)
    # add echo to see what will happen
    echo mv "$file" "$name.html"
done