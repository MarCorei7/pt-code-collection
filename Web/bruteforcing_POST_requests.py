#!/usr/bin/python3

import sys
import requests
import os

URL = "http://'machine-ip'/directory/?id={}"
for i in range(100):
    r = requests.get(url = URL.format(i))
    data = r.text
    if 'wrong!' in data:
        print("Sec {} is wrong".format(i))
    else:
        print("Sec {} is right".format(i))