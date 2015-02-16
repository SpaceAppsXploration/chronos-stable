__author__ = 'lorenzo'

from main.mongod import get_connection
from datastoreapi.buildDatastore import Build


def deploy_layer_one():
    building = Build(mongod=get_connection())

    building.add_targets()

    building.add_missions()

    building.add_events()

    building.link_targets_and_events()

    building.semantic_links_for_missions()

    building.relate_stored_dbpedias()