#!/usr/bin/python

from PIL import Image

white = (255, 255, 255)
black = (0, 0, 0)

image1 = Image.open('QR1.png')
image2 = Image.open('QR2.png')
data1 = image1.load()
data2 = image2.load()

size = width, height = image1.size

qr = Image.new('RGBA', size, white)
new_data = qr.load()

for y in range(height):
	for x in range(width):
		if (data1[x, y] == data2[x, y]):
			# new_data[x, y] = white
			continue
		else:
			new_data[x, y] = black

qr.show()

qr.close()
image1.close()

