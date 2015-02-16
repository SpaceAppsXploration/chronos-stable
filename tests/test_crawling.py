__author__ = 'lorenzo'

import os
import sys
from pprint import pprint
import time
from pymongo import MongoClient

import simplejson as json


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
sys.path.append(os.path.dirname("../"))

import unittest

client = MongoClient('localhost', 27017)
db_instance = client.TESTSONLY


class TestCrawling(unittest.TestCase):
    def test_crawl_and_cache(self):
        """
        Crawl a small amount of keywords from agencies' sites and store them in "crawling" cache collection
        :return:
        """
        import scraping.agenciesScraperUtils as Scraping

        cursor = db_instance.base.find({"chronos:group": "keywords"}, timeout=False)
        print("ESA crawling started")
        for doc in cursor:
            key = doc['skos:prefLabel']
            for keyword in doc['chronos:toSearch']:
                url = Scraping.generate_esa_url(keyword)
                print(url)
                html = Scraping.retrieve(url)
                #print(html)
                Scraping.store_to_cache_collection(key, keyword, html, "ESA", db_instance)
        print("ESA crawling finished")
        cursor.close()

        if db_instance.crawling.find({}).count() > 1:
            assert True
            return

        assert False

    def test_cache_to_cloud(self):
        """
        Take the urls in "crawling" collection and store them in Mongo
        :return:
        """
        from cloudapi.ResourceObjects.agenciesWebPages import WebPages

        cursor = db_instance.crawling.find({})
        for p in cursor:
            storeit = WebPages(db_instance, cache_obj=p, publisher=p["home"])
            storeit.store_webpage_URLs()
            del storeit

        if db_instance.webpages.find({}).count() > 1:
            assert True
            return

        assert False

    def test_print_keywords_used(self):
        """
        Print keywords that have been used to index crawled urls.
        This method use a cache collection called "memcached". It's useful for different front-end use-cases
        :return:
        """
        from bson.objectid import ObjectId

        query = db_instance["memcached"].find_one({"object": "homepageKeys"})
        if query is None:  # create the dictionary of keywords and cache
            indexing = dict()

            query = {"$and": [
                        {"schema:about": {"$exists": True, "$ne": []}},
                        {"chronos:group": "urls"}
                    ]
            }

            projection = {"schema:about": True,
                          "skos:prefLabel": True,
                          "schema:headline": True,
                          "schema:description": True}
            objects = db_instance['webpages'].find(query, projection)

            #pprint(objects[5])

            for o in objects:
                if "chronos:hasKeyword" in o:
                    ref = "chronos:hasKeyword"
                else:
                    ref = "schema:about"
                for k in o[ref]:
                    doc = db_instance['base'].find_one({"_id": ObjectId(k["_id"])})
                    if str(doc["_id"]) in indexing.keys():
                        # append
                        indexing[str(doc["_id"])]["linked"].append(str(o["_id"]))
                    else:
                        # create key > value
                        q = db_instance["base"].find_one({"_id": ObjectId(doc["skos:exactMatch"][0]["_id"])})
                        indexing[str(doc["_id"])] = {
                            "broader": q["skos:prefLabel"],
                            "pref_label": doc["skos:prefLabel"],
                            "linked": [str(o["_id"])]
                        }

            index = indexing
            indexing = json.dumps(indexing)
            db_instance["memcached"].insert({"object": "homepageKeys", "time": time.time(), "value": indexing})
        else:  # retrieve from cache
            index = json.loads(query["value"])

        sort = []
        for k, v in sorted(index.items(), key=lambda x: len(x[1]["linked"]), reverse=True):
            sort.append([k, len(index[k]["linked"]), index[k]["pref_label"], index[k]["broader"]])

        for s in sort:
            print(s)
