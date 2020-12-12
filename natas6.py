# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 16:04:26 2020

@author: SnowHam
"""

import requests

url = 'http://natas5.natas.labs.overthewire.org/'

s = requests.Session()
s.auth = ('natas5', 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq')
r = s.get(url)

print(r.headers)