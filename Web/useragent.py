#1/usr/bin/env python

import urllib2

address = 'http://site:port/'

opener = urllib2.build_opener()
opener.addheaders = 	[	
				('User-agent', 'Firefox'),
				('Referer', 'kylecool.org')
			]
response = opener.open(address)
print response.read()
