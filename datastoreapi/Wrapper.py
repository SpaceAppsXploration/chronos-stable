__author__ = 'Lorenzo'

import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


class Wrapper(object):
    """
    This is the class that wraps the connection, Wrapper instance or any of its children has to be called to get connection
    ----------------------------------------------------------------------

    :method return_connection:
    """

    __client = None
    __mongod = None

    def __init__(self, unittest=False):
        self.__client = MongoClient('localhost', 27017)
        self.test = True
        self.unittest = unittest

        self.__mongod = self.__get_connection(unittest=self.unittest)

    def __get_connection(self, unittest):
        # create a Mongo __client
        if unittest:
            self.__mongod = self.__client.TESTONLY
        else:
            if self.test:
                self.__mongod = self.__client.PMT
            else:
                self.__mongod = self.__client.PTEST
        #print(type(self.__mongod))
        return self.__mongod

    def return_connection(self):
        if self.__mongod is not None:
            return self.__mongod

        raise ConnectionFailure("MongoDB is not up")

    def return_client(self):
        if self.__client is not None:
            return self.__client

        raise ConnectionFailure("Client has not been initiated")


