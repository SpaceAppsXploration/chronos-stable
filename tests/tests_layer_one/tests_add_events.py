#
# Tests for the third stage of 'layer one' of deploying: add_events
#

__author__ = ['lorenzo@pramantha.net']


import unittest
from pprint import pprint


from datastoreapi.buildDatastore import Build


class Test(unittest.TestCase):
    """
    Class for testing the Datastore building process
    """

    built = Build()

    @classmethod
    def test_add_events(cls, test):
        cls.built.add_events(test=test)
