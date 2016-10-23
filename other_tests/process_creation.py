#!/usr/bin/python

import os, sys
import signal
from time import time

if __name__ == '__main__':
    print "[+]Note: this test will take 100 seconds to complete, be patient"

    for i in range(100):
        count = 0
        start = time()

        while True:
            if time() - start >= 1:
                print count
                break
            try:
                PID = os.fork()
            except OSError:
                continue

            if PID:
                count += 1
            else:
                sys.exit(0)
            
            os.wait()

