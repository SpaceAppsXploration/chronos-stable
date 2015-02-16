#
# Tests for the first stage of 'layer one' of deploying: add_targets
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
    def test_add_targets(cls):
        cls.built.add_targets()
