#!/bin/bash

echo "This is me writing to a file" >> editme.txt
cat editme.txt > /dev/null 2>&1
echo "This is another line dog" >> editme.txt
echo $(cat editme.txt | cut -d" " -f2,3) >> editme.txt
rm -f editme.txt
