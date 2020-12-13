# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 09:33:59 2020

@author: SnowHam
"""

import base64

secret = '3d3d516343746d4d6d6c315669563362'

secret = bytes.fromhex(secret)
secret = secret[::-1]
secret = base64.decodebytes(secret)

print(secret)
