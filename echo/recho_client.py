"""
echo client, usage:

 python echo_client.py <host> <port>

Both host and port are optional, defaults: localhost 50000
host must be present if you want to provide port
"""

import socket 
import sys

host = 'localhost' 
port = 50000 
size = 1024 

nargs = len(sys.argv)
if nargs > 1:
    host = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM) 
s.connect((host,port)) 
#s.send('Hello, world') 

message = raw_input('write message here: ')

while message != '':
    s.send(message)
    data = s.recv(size) 
    print 'from (%s,%s) %s' % (host, port, data)
    message = raw_input('write another message here: ')

s.close()
