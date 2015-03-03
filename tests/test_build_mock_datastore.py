#
# This is the base test for creating a partial datastore for front-end tests
# Run the run_ordered_tests() method
#

from datastoreapi.buildDatastore import Build
import unittest


class TestKBcreation(unittest.TestCase):
    """
    Set of tests for KB operations. Check in test database if data is properly stored.
    ----------------------------------------------------------------------------------
    Have to be run in order.
    """

    built = Build()

    @staticmethod
    def run_ordered_tests():
        """
        Full set of tests. It creates a very partial test instance
        :return:
        """
        #
        # Test Layer Zero
        #

        from tests.tests_layer_zero.test_add_concepts import Test
        t = Test()
        t.test_add_all_concepts(test=True)
        del t

        from tests.tests_layer_zero.tests_tag_keywords import Test
        t = Test()
        t.test_tag_keywords_and_subjects()
        del t

        #
        # Test Layer One
        #
        from tests.tests_layer_one.tests_add_targets import Test
        t = Test()
        t.test_add_targets()
        del t

        from tests.tests_layer_one.tests_add_missions import Test
        t = Test()
        t.test_add_missions(test=True)
        del t

        from tests.tests_layer_one.tests_add_events import Test
        t = Test()
        t.test_add_events(test=True)
        del t

        from tests.tests_layer_one.tests_semantic_linking import Test
        t = Test()
        t.test_link_targets_and_events(test=True)
        del t

        from tests.tests_layer_one.tests_semantic_linking import Test
        t = Test()
        t.test_semantic_links_for_missions(test=True)
        del t

        #
        # Test Layer Two
        #
        from tests.tests_layer_two.test_store_webpage_from_crawling import Test
        t = Test()
        t.test_store_webpages_mongo_documents()
        del t

        #cls.test_crawl()
        #cls.test_store_webpages_with_tagme()
