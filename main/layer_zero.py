__author__ = ['lorenzo@pramantha.net']

from datastoreapi.buildDatastore import Build


def deploy_layer_zero():
    building = Build()

    # Store taxonomy concepts
    building.add_SKOS_concepts()

    # Store hierarchy in the taxonomy
    building.add_hierarchical_links_among_concepts()

    # Store dbpedia docs linked to concepts
    building.semantic_linking_for_concepts()

    return None
