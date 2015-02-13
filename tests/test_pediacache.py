__author__ = 'lorenzo'

from toolbox.pediacache import DBpediaCache
from toolbox.surfing import JsonLD

from toolbox import pediacache
from pprint import pprint

import unittest


class Test(unittest.TestCase):
    """
    Class for testing the tools in the 'toolbox' package
    """

    title_slug0 = 'Spacecraft'
    title_slug1 = 'Sun'
    buggy = 'Joker&amp;s'
    dbpedia_url1 = 'http://dbpedia.org/data/Spacecraft.jsond'
    dbpedia_url2 = 'http://dbpedia.org/data/Sun.jsond'

    def test_get_or_retrieve_and_store(self):
        # tests variables
        w = DBpediaCache(unittest=True)
        a = w.get_or_retrieve_and_store(self.title_slug0)
        #b = pediacache.get_or_retrieve_and_store(self.mongo, self.buggy)
        c = w.get_or_retrieve_and_store(self.title_slug1)

        pprint(type(a))
        #pprint(b)
        pprint(c)

    def test_surfing_get_body_text_from_dbpedia_json(self):
        j = JsonLD(unittest=True)
        text2 = j.get_body_text_from_dbpedia_json(self.dbpedia_url2)
        text1 = j.get_body_text_from_dbpedia_json(self.dbpedia_url1)

        print(text2)
        print(text1)
