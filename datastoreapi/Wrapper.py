__author__ = 'Lorenzo'

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from datastoreapi.datastoreErrors import DocumentExists


class Wrapper(object):
    """
    This is the class that wraps the connection, Wrapper instance or any of its children has to be called to get connection
    ----------------------------------------------------------------------

    :method return_connection:
    """

    __client = None
    __mongod = None

    def __init__(self):
        self.__client = MongoClient('localhost', 27017)
        self.test = True

        self.__mongod = self.__get_connection()

    def __get_connection(self):
        # create a Mongo __client
        if self.test:
            self.__mongod = self.__client.PMT
        else:
            self.__mongod = self.__client.PTEST

        # print(type(self.__mongod))
        return self.__mongod

    def return_connection(self):
        if self.__mongod is not None:
            return self.__mongod

        raise ConnectionFailure("MongoDB is not up")

    def return_client(self):
        if self.__client is not None:
            return self.__client

        raise ConnectionFailure("Client has not been initiated")

    def append_link_to_mongodoc(self, document, field, resource, in_collection):
        """
        Utility method for all the different objects involved in the building.
        Append @id, _id, @type of a certain resource to a document[field] into a collection.
        If exist, it stores also skos:inScheme, altLabel and topConceptOf.
        Needed when some stored document[field] needs to be updated.
        """
        to_append = dict(
            {
                "@id": resource["@id"],
                "_id": resource["_id"],
                "@type": resource["@type"],
            }
        )

        if "skos:inScheme" in resource:
            to_append["skos:inScheme"] = resource["skos:inScheme"]
        if "skos:topConceptOf" in resource:
            to_append["skos:topConceptOf"] = resource["skos:topConceptOf"]
        if "skos:altLabel" in resource.keys() and in_collection == 'freebaseRes':
            to_append["skos:altLabel"] = resource["skos:altLabel"]

        coll = self.__mongod[in_collection]

        if document is not None:
            try:
                if type(document[field]) is list:
                    if len(document[field]) == 0:
                        document[field] = [to_append]
                    elif [True for d in document[field] if d["_id"] == to_append["_id"]]:
                        raise DocumentExists('This document is already in the property\'s value')
                    else:
                        document[field].append(to_append)
                else:
                    document[field] = to_append
            except KeyError:
                document[field] = [to_append]

        else:
            raise BaseException('Document trying to modify doesn\'t exist')

        return coll.find_and_modify({"_id": document["_id"]}, document, new=True)


# resource repositories links
DBPEDIA_URL = "http://dbpedia.org/data/%s.jsond"        # string-substitute with wikipage title (slug)
DBPEDIA_RESOURCE = "http://dbpedia.org/resource/%s"     # string-substitute with wikipage title (slug)
PRAMANTHA_URL = "http://pramantha.eu/%s/%s"             # domain for local resources (chronos:group, slug)
CHRONOS_GROUPS = ['missions', 'keywords', 'events', 'targets',
                  'dbpediadocs', 'area', 'divisions', 'schemes',
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

CHRONOS_CONTEXT = dict(
    {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "schema": "http://schema.org/",
        "dbpedia": "http://dbpedia.org/property/",
        "owl": "http://www.w3.org/2002/07/owl#",
        "chronos": "http://pramantha.eu/ontology/",
        "@base": "http://pramantha.eu/ontology"
    }
)

SENSORS_ONTOLOGY_CONTEXT = dict(
    {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "schema": "http://schema.org/",
        "dbpedia": "http://dbpedia.org/property/",
        "owl": "http://www.w3.org/2002/07/owl#",
        "chronos": "http://pramantha.eu/ontology",
        "sensor": "http://pramantha.eu/ontology/sensors/",
        "@base": "http://pramantha.eu/ontology/sensors"
    }
)