#
# Tests for the second stage of 'layer zero' of deploying: add_all_concepts
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
    def test_add_all_concepts(cls, test=True):
        cls.built.add_all_concepts(test=test)