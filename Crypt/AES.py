#!/usr/bin/env python

import base64
from Crypto.Cipher import AES

ciphertext = base64.b64decode('')
key = base64.b64decode('')

aes = AES.new(key, AES.MODE_ECB)
plaintext = aes.decrypt(ciphertext)

print plaintext
