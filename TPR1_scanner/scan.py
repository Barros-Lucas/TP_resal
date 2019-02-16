# -*- coding: utf-8 -*
import sys
import os
import socket

port = []

if len(sys.argv) != 2:
	print(f"Usage: {sys.argv[0]} <ip>", file=sys.stderr)
	sys.exit(1)

machine = sys.argv[1]


def scanTCPport(ip,rangeMin,rangeMax):
    for i in range(rangeMin,rangeMax):
        if os.fork() == 0:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                client.connect(("localhost", i))
                client.close()
            except ConnectionRefusedError:
                # print(f"le port {i} n'est pas ouvert")
                sys.exit(0)
            print(f"le port {i} est ouvert")
            sys.exit(0)

    for i in range(rangeMin,rangeMax):
        os.wait()

def scanUDPport(ip,rangeMin,rangeMax):
    for i in range(rangeMin,rangeMax):
        if os.fork() == 0:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                ret = sock.connect_ex(("localhost", i))           
                if ret == 0:
                    print(i)
 
            sys.exit(0)
    for i in range(rangeMin,rangeMax):
        os.wait()

scanTCPport(machine,7950,8001)

#ScanUDPport isn't working, i can't receave response from server and so i can't know if this port is available or not
#scanUDPport(machine,8000,8005)
