#!/usr/bin/python

import os
from time import time

if __name__ == '__main__':

    count_array = []
    print "[+] Note: This test will take 100 seconds to run, be patient" 
    for i in range(100):

        start = time()
        count = 0
        payload = '\x00' * 512

        while True:
            if time() - start > 1:
                count_array.append(count)
                break

            read_fd, write_fd = os.pipe()
            #os.close(read_fd)
            write_fd = os.fdopen(write_fd, 'w')
            write_fd.write(payload)
            write_fd.close()
 
            #os.close(write_fd)
            read_fd = os.fdopen(read_fd)
            read_fd.read()
            read_fd.close()
            count += 1
            
    for num in count_array:
        print num        
