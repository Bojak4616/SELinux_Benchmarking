#!/usr/bin/python

import os
import subprocess
from time import time

if __name__ == '__main__':
    print "[+]Note: This test will take 3min, be patient"
    count_array = []
    for i in range(3):
        count = 0
        start = time()

        while True:
            if time() - start >= 60:
                break
            
            for x in range(8):
                p = subprocess.call(['/bin/bash','callme.sh'])

            count += 1
        
        print count
 
