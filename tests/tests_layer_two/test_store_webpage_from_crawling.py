#
# Tests for the last stage of 'layer two' of deploying: store_webpages_mongo_documents
#

__author__ = 'lorenzo'


import unittest
from pprint import pprint


from datastoreapi.buildDatastore import Build


class Test(unittest.TestCase):
    """
    Class for testing the Datastore building process
    """

    built = Build()

    @classmethod
    def test_store_webpages_mongo_documents(cls):
        cls.built.store_webpages_mongo_documents()
