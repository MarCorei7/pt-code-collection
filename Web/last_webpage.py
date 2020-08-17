#!/usr/bin/env python

import requests
import re

url = 'http://ip:port'
first_page = '/fp/'

s = requests.Session()

r = s.get(url + first_page)

counter = 1
while ( 1 ):
	next_page = re.findall(r'action="(.*?)"', r.text)[0]
	r = s.get(url + next_page)
	print counter, r.text
	counter += 1
