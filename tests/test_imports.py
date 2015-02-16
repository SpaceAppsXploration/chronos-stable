__author__ = 'lorenzo'


import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
sys.path.append(os.path.dirname("../"))

import unittest


class TestInit(unittest.TestCase):
    def test_requirements(self):
        print("here")
        try:
            from bs4 import BeautifulSoup, NavigableString
        except ImportError:
            assert False

        try:
            from selenium import webdriver
        except ImportError:
            assert False

        try:
            import requests
        except ImportError:
            assert False

        """try:
            import rdflib
        except ImportError:
            assert False"""

        try:
            import pyorient
        except ImportError:
            assert False

        try:
            import pymongo
            self.assertEqual(pymongo.version, "2.7.2", "Pymongo version is not GO")
        except ImportError:
            assert False

        try:
            from bson.objectid import ObjectId
        except ImportError:
            assert False

        assert True
