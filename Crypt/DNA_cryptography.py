#!/usr/bin/env python

# mappings = {
# 	'A': '00',
# 	'C': '10',
# 	'G': '01',
# 	'T': '11'
# }

mappings = {
	'AAA': 'a',
	'AAC': 'b',
	'AAG': 'c',
	'AAT': 'd',
	'ACA': 'e',
	'ACC': 'f',
	'ACG': 'g',
	'ACT': 'h',
	'AGA': 'i',
	'AGC': 'j',
	'AGG': 'k',
	'AGT': 'l',
	'ATA': 'm',
	'ATC': 'n',
	'ATG': 'o',
	'': 'p',
	'': 'q',
	'': 'r',
	'': 's',
	'': 't',
	'': 'u',
	'': 'v',
	'': 'w',
	'': 'x',
	'': 'y',
	'': 'z',
	'': '',
	'TAG': 'Y',
	'TAT': 'Z',
	'TCA': '1',
	'TCC': '2',
	'TCG': '3',
	'TCT': '4',
	'TGA': '5',
	'TGC': '6',
	'TGG': '7',
	'TGT': '8',
	'TTA': '9',
	'TTC': '0',
	'TTG': ' ',
	'TTT': '.'
}

c = open('Biography.txt').read().strip()

flag = []
for x in range(0, len(c), 3):
	piece = c{x:x+3]
	print piece, mappings[piece]
	flag.append(mappings[piece])

print ''.join(flag)

# for k, v in mappings.iteritems():
# 	c = c.replace(k,v)


# print hex(int(c,2))[2:-1]