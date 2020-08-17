#!/usr/bin/env python

import pwn

greeting_message = "You have now entered the Duck Web, and youre in for a honkin good time.\nCan you figureout my trick?"

xor_string = '\x29\x06\x16\x4f\x2b\x35\x30\x1e\x51\x1b\x5b\x14\x4b\x08\x5d\x2b\x56\x47\x57\x50\x16\x4d\x51\x51\x5d\x00'

print pwn.xor(greeting_message, xor_string)
