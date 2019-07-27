#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:20:55 2019

@author: saurabh
"""

import json, requests
from pprint import pprint

url1 = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=Indigo&api-key=kowiCbwVAzFvigJn8UbuGgNm2aomAWF9'

resp = requests.get(url1)
data = json.loads(resp.text)
#for key in data:
#    print(key)
i=0;
for key in data['response']['docs']:
    multimediaList = key['multimedia']
    length = len(multimediaList)
    for i in range(length) :
        print(multimediaList[i]['url'])
#x=data['response']['docs'][0]

#for key in x:
  #  pprint(x['multimedia'][0]['url'])