__author__ = ['lorenzo@pramantha.net']

from datastoreapi.buildDatastore import Build


def deploy_layer_two():
    building = Build()

    building.crawl_agencies()

    #building.crawl_google_search()

    building.store_crawling_cache()

    building.store_webpages_mongo_documents()


