#!/usr/bin/env python

import base64 as b
import pickle

p = b.b64decode('asdfasdf')
print pickle.loads(p)
