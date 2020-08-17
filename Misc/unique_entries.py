s = set()
f = open("fsocity.dic", 'r')

count = 0
while True:
	count += 1
	line = f.readline()
	if not line:
		break
	else:
		s.add(line)
		print("reading lines: " + str(count))
f.close()

newFile = open("unique.txt", 'w')
newcount = 0
for i in s:
	newFile.write(i)
	newFile.write("\n")
	newcount += 1
newFile.close()
print("total: " + str(newcount))
