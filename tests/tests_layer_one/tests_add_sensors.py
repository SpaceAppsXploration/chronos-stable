#
# Tests for the first stage of 'layer one' of deploying: add_sensors
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
    def test_add_sensors(cls):
        cls.built.add_sensors()
