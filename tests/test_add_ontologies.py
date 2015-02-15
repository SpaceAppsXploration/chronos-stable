__author__ = 'lorenzo'


import unittest
from pprint import pprint
import simplejson as json

from tests.test_inputs.test_mongod import get_connection
from datastoreapi.buildDatastore import Build


class Test(unittest.TestCase):
    """
    Class for testing the Datastore building process
    """
    import simplejson as json
    with open("../SensorOntology/SpaceSensor_json-ld_v2.json", "r") as jsonld:
        sensors = json.loads(jsonld.read())

    with open("../SensorOntology/ChronosOntology.json", "r") as jsonld:
        chronos = json.loads(jsonld.read())

    mongod = get_connection()
    built = Build(mongod)

    def test_add__ontologies(self):
        self.built.add_ontologies()

    def test_ontology_collection_picking(self):
        result = self.mongod.ontology.find_one({"@id": "http://pramantha.eu/ontology/sensors/isEmittedBy"})

        from tests.test_outputs.dump_isEmittedBy import dump_isemitteby

        if result["owl:inverseOf"] == dump_isemitteby["owl:inverseOf"] and len(result["@type"]) == len(dump_isemitteby["@type"]):
            assert True
        else:
            assert False

    def test_base_collection_picking(self):
        result = self.mongod.base.find_one({"skos:prefLabel": "Astronautics"}, {"_id": False})
        from tests.test_outputs.dump_Astronautics import dump_astronautics

        if len(result["skos:narrower"]) == len(dump_astronautics["skos:narrower"]):
            assert True
        else:
            assert False
