#
# Tests for the forth stage of 'layer zero' of deploying: tag_keywords_and_subjects
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
    def test_tag_keywords_and_subjects(cls):
        cls.built.tag_keywords_and_subjects()
