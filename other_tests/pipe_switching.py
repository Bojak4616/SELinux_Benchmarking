#!/usr/bin/python

from time import time
from multiprocessing import Process, Pipe

def ping(conn):
    global count
    start = time()
    while True:
        if time() - start >= 1:
            break

        conn.send(count+1)
        count = conn.recv()

def pong(conn):
    global count
    start = time()
    while True:
        if time() - start >= 1:
            print count
            break

        count = conn.recv()
        conn.send(count+1)

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    print "[+] Note: This test will take ~200 seconds, be patient"
    for i in range(200):
        count = 0
        p1 = Process(target=ping, args=(child_conn,))
        p2 = Process(target=pong, args=(parent_conn,))
        
        p2.start()
        p1.start()
        
        hung = time()
        while True:
            if time() - hung > 2:
                p1.terminate()
                p2.terminate()

            if not p1.is_alive() and p2.is_alive():
                p2.terminate()
                
            if p1.is_alive() and not p2.is_alive():
                p1.terminate()

            if not p1.is_alive() and not p2.is_alive():
                hung = time()
                break

