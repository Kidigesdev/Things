#!/usr/bin/python
import base64
import socket
import sys

ON = 'AAAAKtDygfiL/5r31e+UtsWg1Iv5nPCR6LfEsNGlwOLYo4HyhueT9tTu36Lfog=='
OFF = 'AAAAKtDygfiL/5r31e+UtsWg1Iv5nPCR6LfEsNGlwOLYo4HyhueT9tTu3qPeow=='

#IP of your HS100. (example: '192.168.178.40')
TCP_IP = '192.168.178.40'
TCP_PORT = 9999
BUFFER_SIZE = 1024

cmdargs = str(sys.argv)

if 'on' in cmdargs:
    in_base = ON
else:
    in_base = OFF

out_base = base64.standard_b64decode(in_base)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(out_base)
data = s.recv(BUFFER_SIZE)
s.close()
