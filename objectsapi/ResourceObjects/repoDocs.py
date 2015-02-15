from pprint import pprint
from pymongo.errors import DuplicateKeyError, DocumentTooLarge

from main.mongod import get_connection
from datastoreapi.buildDatastore import Build
from datastoreapi.datastoreErrors import DocumentExists
from datastoreapi.XMLstringHandler.XMLtaxonomyUtilities import SKOSconcepts
from datastoreapi.basicDocs import BasicDoc
from tagmeapi.tagMeService import TagMeService
from toolbox.tools import retrieve_from_sparql


class PublicRepoDocument(Build):
    def __init__(self, dbpedia=None, freebase=None,  abstract=None):
        super().__init__(mongod=get_connection())
        self.db = self.mongod
        self.dbpedia = dbpedia  # url of dbpedia jsond
        self.freebase = freebase  # url of freebase doc
        self.abstract = abstract  # optional abstract

        self.concept_utilities = SKOSconcepts()  # instance of the concept utilities

    def store_wiki_resource(self):
        """
        Utility: store resources from other repository.
        DBpedia resource has always a sameAs in Freebase
        Freebase can be a term or a comment or a text

        NOTE: to avoid problems with same prefLabel with other kinds of resources in the KB,
        wiki resources define ONLY an altLabel
        -----------------------------------------------------------------------------------
        this is consistent with the JSON-LD notation that uses with preferred identification
        the @id property

        :param self.dbpedia: DBpedia resource URL
        :param self.freebase: Freebase resource URL
        :return: document or raise DocumentExists
        """

        categories_to_exclude = [
            "Scenic highways in Oregon", "Volkswagen platforms", "All-American Roads",
            "North Atlantic convoys of World War II", "Highlands and Islands of Scotland",
            "Canadian drama television series", "State_routes_in_Oregon"

        ]

        if self.dbpedia is not None:  # dbpedia resource only
            i = self.dbpedia.rfind('/data/')
            label = self.dbpedia[i + 6:-6]
            sparql = self.DBPEDIA_SPQL % label

            url = self.PRAMANTHA_URL % ("dbpediadocs", label)
            if self.db.base.find_one({"@id": url}) is None:
                pprint("Storing Resource:" + url)

                doc = BasicDoc.blank_dbpediadoc()
                doc["@id"] = url
                doc["skos:altLabel"] = label
                doc["owl:sameAs"][0]["@value"] = self.dbpedia
                doc["owl:sameAs"][1]["@value"] = sparql

                # store abstract and categories via TagMe API
                annotation = []
                try:
                    annotation = TagMeService.retrieve_taggings(label)["annotations"][0]
                    if len(annotation["dbpedia_categories"]) != 0:
                        add_to = doc["chronos:dbpediaCategories"]
                        for ct in annotation["dbpedia_categories"]:
                            if ct in categories_to_exclude:
                                return None  # document has wrong argument return None
                            if ct not in add_to:
                                add_to.append(ct)
                        print("ADDED CATEGORIES: " + str(doc["chronos:dbpediaCategories"]))

                    if doc["chronos:tagMeAbs"] is None and len(annotation["abstract"]) != 0:
                        doc["chronos:tagMeAbs"] = annotation["abstract"]
                except (IndexError, KeyError):
                    pass

                # insert doc
                id_ = self.db.base.insert(doc)
                this_doc = self.db.base.find_one({"_id": id_})
                print("DBPEDIA DOC INSERTED <<<<<<<<<<<<<<<")

                # insert cache
                try:
                    cache = dict()
                    cache['body'] = str(retrieve_from_sparql(sparql))
                    cache['@id'] = url
                except Exception as e:
                    print("URL " + str(sparql))
                    raise Exception(e)

                try:
                    self.mongod.DBpediacache.insert(cache)
                    print("DBPEDIA CACHE INSERTED <<<<<<<<<<<<<<<")
                except (DuplicateKeyError, DocumentTooLarge):
                    pass

                return this_doc
            else:
                raise DocumentExists(str(url))


    def link_to_repository_with_tagme(self, keyword):
        """
        find links to dbpedia looking for a keyword with TagMe API
        """
        # tagme.spotting keyword
        # check response
        # update or add dbpedia doc in db "narrowMatch" property
        pass
