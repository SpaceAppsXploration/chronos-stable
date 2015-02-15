__author__ = 'lorenzo'

import os
import sys
from pprint import pprint
import time
from pymongo import MongoClient

import simplejson as json


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
sys.path.append(os.path.dirname("../"))

import unittest

client = MongoClient('localhost', 27017)
db_instance = client.PMT
db_2 = client.PTEST


def copy_collection():
    prefLabel = db_instance.base.find({"chronos:group": "keywords"}, {"skos:prefLabel": True, "_id": False})
    for p in prefLabel:
        found = db_2.crawling.find({"key": p["skos:prefLabel"]})
        for f in found:
            db_instance.crawling.insert(f)

copy_collection()
