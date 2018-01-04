#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 16:24:31 2017

@author: andy
"""

import requests
import simplejson
import ast
from pymongo import MongoClient
from datetime import datetime

#url = "https://data.nasa.gov/resource/y77d-th95.json"
#r = requests.get(url)
#data = ast.literal_eval(r.text)

#Alternative way
#import pandas as pd
#query = url
#data = pd.read_json(query)

#initialize mongo client and collection
mc = MongoClient()
db = mc.practice
meteor = db.meteorites

#for d in data:
#    if "year" in d.keys():
#        d["time"] = datetime.strptime(d["year"], "%Y-%m-%dT%H:%M:%S.%f")
#    else:
#        d["time"] = ""
#
#met = meteor.insert_many(data)

start = datetime(2012, 1, 1, 00, 00, 00)
end = datetime.now()
most_recent = list(meteor.find({ 'time' : { "$lt": end, "$gte" : start }}))