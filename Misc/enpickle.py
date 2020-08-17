#!/usr/bin/env python

import base64 as b
import pickle

p = b.b64decode('asdfasdf')
# print pickle.loads(p)

ours = { } #pickle content as dictionary
o = pickle.dumps(ours)
print b.b64encode(o)

