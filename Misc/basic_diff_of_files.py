#!/usr/bin/env python

f1 = open('file1').read()
f2 = open('file2').read()

message = []
for i in range(len(f1)):
	if (f1[i] == f2[i]):
		message.append(f1[i])

print ''.join(message)
