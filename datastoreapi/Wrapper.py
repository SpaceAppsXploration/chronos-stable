#
# This Module has the Wrapper class, it contains the connection handler.
# And a lot of VARIABLES useful all over the rest of the script
#

__author__ = ['lorenzo@pramantha.net']

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from datastoreapi.datastoreErrors import DocumentExists, ErrorInQuery


class Wrapper(object):
    """
    This is the class that wraps the connection, Wrapper instance or any of its children has to be called to get connection
    ----------------------------------------------------------------------

    :method return_mongo: return to other classes and scripts the connection to Mongo
    :method return_orient: return to other classes and scripts the connection to Orient
    """

    __mongo = None   # client
    __mongod = None   # connection to database

    def __init__(self):
        self.__mongo = MongoClient('localhost', 27017)
        self.test = True

        self.__mongod = self.__get_mongo_db()

    def __get_mongo_db(self):
        # create a Mongo __client
        if self.test:
            self.__mongod = self.__mongo.PMT
        else:
            self.__mongod = self.__mongo.PTEST

        # print(type(self.__mongod))
        return self.__mongod

    def return_mongo(self):
        if self.__mongod is not None:
            return self.__mongod

        raise ConnectionFailure("MongoDB is not up")

    def create_databases(self):
        pass

    def get_all_concepts(self, timeout):
        try:
            keywords = self.__mongod.base.find(
                {
                    "$or": [
                        {"chronos:group": "keywords"},
                        {"chronos:group": "subjects"},
                        {"chronos:group": "divisions"}
                    ]
                },
                timeout=timeout
            )
        except ErrorInQuery as e:
            raise e

        return keywords

    def get_events_and_targets(self, timeout):
        try:
            docs = self.__mongod.base.find(
                {"$or": [
                    {"chronos:group": "targets"},
                    {"chronos:group": "events"}
                ]},
                timeout=timeout)
        except ErrorInQuery as e:
            raise e

        return docs

    def get_all_missions(self, timeout):
        try:
            missions = self.__mongod.base.find({"chronos:group": "missions"}, timeout=timeout)
        except ErrorInQuery as e:
            raise e

        return missions

    def get_all_dbpediadocs(self, timeout):
        try:
            dbpedias = self.__mongod.base.find({"chronos:group": "dbpediadocs"}, timeout=timeout)
        except ErrorInQuery as e:
            raise e

        return dbpedias

# resource repositories links
DBPEDIA_URL = "http://dbpedia.org/data/%s.jsond"             # string-substitute with wikipage title (slug)
DBPEDIA_RESOURCE = "http://dbpedia.org/resource/%s"          # string-substitute with wikipage title (slug)
UMBEL_RESOURCE = "http://umbel.org/umbel/rc/%s"              # string-substitute with umbel title (slug)
ONTOLOGY_URL = "http://ontology.projectchronos.eu/%s/"       # domain for ontologies
RESOURCE_URL = "http://api.pramantha.net/data/%s/%s"         # domain for local resources (chronos:group, slug)
CHRONOS_GROUPS = ['missions', 'keywords', 'events', 'targets',
                  'dbpediadocs', 'areas', 'divisions', 'schemes',
                  'subjects', 'urls', 'events']

# common Links to use in resources addresses
STI_LD_LINK = "http://dbpedia.org/data/NASA_STI_Program.jsond"
RDF_RESOURCE = "http://www.w3.org/1999/02/22-rdf-syntax-ns#resource"
RDF_PLAIN_LITERAL = "http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral"
SKOS_CONCEPT = "http://www.w3.org/2004/02/skos/core#Concept"
SKOS_COLLECTION = "http://www.w3.org/2004/02/skos/core#Collection"
SKOS_SCHEME = "http://www.w3.org/2004/02/skos/core#ConceptScheme"

# static file for external resources
from input.STI import STI_divisions, STI_subjects  # file where taxonomy subjects and divisions are stored
static = STI_divisions.copy()
static.update(STI_subjects)
