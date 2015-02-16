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
db_instance = client.TESTSONLY


class TestKB(unittest.TestCase):
    def test_print_divisions(self):
        """
        Tests if divisions' documents and collection are stored correctly
        :return:
        """
        pass

    def test_print_subjects(self):
        """
        Tests if subjects' documents and collection are stored correctly
        :return:
        """
        pass

    def test_get_all_pediasocs_by_keyword(self):
        """
        Retrieve all the documents 'dbpediadocs' that are linked to certain keyword
         :return:
        """
        pass

    def test_pediadoc_insertion(self):
        """
        test how it works to insert a certain document of kind 'dbpedias' passing the url of a dpedia resource
        """
        pass

    def test_get_first_level_of_a_node(self):
        """
        Retrieves a node and all the documents linked to it
        """
        pass

    def test_get_second_level_of_a_node(self):
        """
        Retrieves a node and all the documents linked to it and all the documents linked to them
        """
        pass


if __name__ == '__main__':
    pass
