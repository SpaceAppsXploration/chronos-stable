__author__ = ['lorenzo@pramantha.net']

from datastoreapi.buildDatastore import Build


def deploy_layer_one():
    building = Build()

    building.add_targets()

    building.add_missions()

    building.add_events()

    building.add_sensors()

    building.link_targets_and_events()

    building.link_missions()

    building.relate_stored_dbpedias()