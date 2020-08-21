#!/usr/bin/env python

with open("ry_only_ten.txt", "w") as out:	#newfile
	with open("oldry.txt") as f:	#oldfile
		for line_no, line in enumerate(f):
			if len(line.strip()) == 10:
				out.write(line)
			else:
				print "Removing line {0}".format(line_no)

