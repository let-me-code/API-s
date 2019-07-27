#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:38:40 2019

@author: saurabh
"""


phnum = int(input("Enter mobile number : "))

url = "https://api.datayuge.com/v1/lookup/" + str(phnum)

import urllib.request as ur, json
result = json.loads(ur.urlopen(url).read())
print("Operator Name: " + result["operator"])
print("Operator Circle: " + result["circle"])
