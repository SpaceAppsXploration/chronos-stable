__author__ = 'lorenzo'

from main.mongod import get_connection
from datastoreapi.buildDatastore import Build


def deploy_layer_two():
    building = Build(mongod=get_connection())

    building.crawl_agencies()

    #building.crawl_google_search()

    building.store_crawling_cache()

    building.store_webpages_mongo_documents()


