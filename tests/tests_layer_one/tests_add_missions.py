#
# Tests for the second stage of 'layer one' of deploying: add_missions
#

__author__ = ['lorenzo@pramantha.net']


import unittest
from pprint import pprint

from datastoreapi.Wrapper import *
from datastoreapi.buildDatastore import Build


class Test(unittest.TestCase):
    """
    Class for testing the Datastore building process
    """

    built = Build()

    @classmethod
    def test_add_missions(cls, test):
        cls.built.add_missions(test=test)


