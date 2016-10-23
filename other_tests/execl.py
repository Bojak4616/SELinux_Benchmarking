#!/usr/bin/python

import os
from multiprocessing import Process
from time import time

def spawn():
    os.execl('/usr/bin/echo', '-n', ' be patient please ')

if __name__ == '__main__':
    print "[+]Note: This test will take 100 seconds, be patient"
    count_array = []
    for i in range(100):
        count = 0
        start = time()

        while True:
            if time() - start >= 1:
                count_array.append(count)
                break
            
            p = Process(target=spawn)
            p.start()
            count += 1

    for num in count_array:
        print num
 
