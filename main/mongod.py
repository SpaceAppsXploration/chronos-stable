__author__ = 'lorenzo'

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
test = True


def get_connection(unittest=False):
    # create a Mongo client
    if unittest:
        mongod = client.TESTONLY
    else:
        if test:
            mongod = client.PMT
        else:
            mongod = client.PTEST
    return mongod