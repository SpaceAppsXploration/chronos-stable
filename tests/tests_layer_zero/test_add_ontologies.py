#
# Tests for the first stage of 'layer zero' of deploying: add_ontologies
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
    def test_add_ontologies(cls):
        cls.built.add_ontologies()

    def test_ontology_collection_picking(self):
        result = self.built.mongod.ontology.find_one({"@id": "http://pramantha.eu/ontology/sensors/isEmittedBy"})

        from tests.test_outputs.dump_isEmittedBy import dump_isemitteby

        if result["owl:inverseOf"] == dump_isemitteby["owl:inverseOf"] and len(result["@type"]) == len(dump_isemitteby["@type"]):
            assert True
        else:
            assert False

    def test_base_collection_picking(self):
        result = self.built.mongod.base.find_one({"@id" : "http://pramantha.eu/dbpediadocs/Planet"}, {"_id": False})
        from tests.test_outputs.dump_Astronautics import dump_planet

        if result["chronos:dbpediaCategories"] == dump_planet["chronos:dbpediaCategories"]:
            assert True
        else:
            assert False
