#
# Tests for the third stage of 'layer zero' of deploying: add_ontologies
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

    def test_add_hierarchy_linked(self):
        # Data from previous Test:test_add_all_concepts is needed
        self.built.add_all_linked()