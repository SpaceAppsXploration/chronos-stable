__author__ = 'lorenzo'

from main.mongod import get_connection
from datastoreapi.buildDatastore import Build


def deploy_layer_zero():
    building = Build(mongod=get_connection())
    # Store ontologies
    building.add_ontologies()
    # Store taxonomy concepts
    building.add_all_concepts()
    # Store hierarchy in the taxonomy
    building.add_all_linked()
    # Store dbpedia docs linked to concepts
    building.tag_keywords_and_subjects()

    return None
