#
# Tests for the forth fifth and sixth stagse of 'layer one' of deploying: link_targets_and_events,
# semantic_links_for_missions and relate_stored_dbpedias
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
    def test_link_targets_and_events(cls, test=True):
        cls.built.link_targets_and_events(test=test)

    @classmethod
    def test_semantic_links_for_missions(cls, test=True):
        cls.built.semantic_links_for_missions(test=test)

    @classmethod
    def test_relate_stored_dbpedias(cls, test=True):
        cls.built.relate_stored_dbpedias(test=test)
