__author__ = ['lorenzo@pramantha.net']

import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from pymongo.errors import CollectionInvalid
from datastoreapi.Wrapper import *
from datastoreapi import Operations


class Build:
    """
    This class contains all the methods used in "main" package's steps
    ------------------------------------------------------------------
    It uses all the classes defined in the 'datastoreapi' and 'tagmeapi' packages.

    :method add_all_concept: read and store all the <skos:Concept> tags in the raw XML string,
        see datastoreapi.XMLstringHandler.XMLskos.py.store_STI_document()
    :method add_all_linked: add to the above stored documents by :add_all_concept the taxonomy's
        relations and predicates
    :method tag_keywords_and_subjects: annotate with TagMaAPI the documents stored above
    :method add_targets: store planets' documents from file
    :method add_missions: merge launches and missions from files, by storing them in the same skos:ConceptScheme
    :method add_events: add missions' events
    :method add_keywords_to_missions: takes the added missions and link them to the concepts in the cloud
    :method link_targets_and_events
    :method semantic_links_for_missions
    :method relate_stored_dbpedias
    :method crawl_agencies: crawl with selenium webdriver using scraping.libs library
    :method crawl_google
    :method store_crawling_cache
    :method store_webpages_mongo_documents
    """

    def __init__(self):
        self.w = Wrapper()
        self.mongod = self.w.return_mongo()

        # create collections in DB
        try:
            self.mongod.create_collection("base")
            self.mongod.create_collection("sensors")
            self.mongod.create_collection("crawling", autoIndexId=False)
            self.mongod.create_collection("webpages")
            self.mongod.create_collection("DBpediacache", autoIndexId=False)
        except CollectionInvalid:
            pass

        # create indexes in DB
        self.mongod.base.ensure_index("@id", unique=True)
        self.mongod.base.ensure_index("skos:prefLabel")
        self.mongod.base.ensure_index("chronos:group", sparse=True)
        self.mongod.sensors.ensure_index("@id", unique=True)
        self.mongod.crawling.ensure_index("hashed", unique=True)
        self.mongod.crawling.ensure_index("key")
        self.mongod.crawling.ensure_index("keyword")
        self.mongod.webpages.ensure_index("chronos:base64", unique=True)
        self.mongod.webpages.ensure_index("@id", unique=True)
        self.mongod.DBpediacache.ensure_index("@id", unique=True)

        print("Build Constructor")
        # Finished initializing the basic building object

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

        coll = self.mongod[in_collection]

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
            print(document)
            raise BaseException('Document trying to modify doesn\'t exist')

        return coll.find_and_modify({"_id": document["_id"]}, document, new=True)

    #
    # Layer Zero
    #
    # Step 1: add SKOS concepts
    def add_SKOS_concepts(self, test=False):
        """
        Looks for concepts in the XML-DOM file, dumps the right document in Mongo
        :return: None
        """

        Operations.dump_concepts(build=self, test=test)
        return None

    # Step 2: add hierarchical links among concepts
    def add_hierarchical_links_among_concepts(self, test=False):
        """
        Stores in the database all the hierarchical information in the XML-DOM file
        :return: None
        """

        Operations.dump_hierarchy(build=self, test=test)
        return None

    # Step 3: semantic linking for concepts
    def semantic_linking_for_concepts(self):
        """
        use the tagmeapi to store annotations about keywords and subjects
        :return: None
        """

        keywords = self.w.get_all_concepts(timeout=False)
        Operations.semantic_hierarchy(build=self, keywords=keywords)
        keywords.close()
        return None

    #
    # Layer One
    #
    def add_targets(self):
        """
        Stores in the database all the information about missions' targets, taken from a JSON file
        and also stores annotations about the given target
        :return: None
        """

        Operations.get_and_store_targets_from_chronos_dump(build=self)
        return None

    def add_missions(self, test=False):
        """
        Stores in the database all the information about missions, taken from a JSONs: a single file about missions
        and many others about launches
        :return: None
        """

        Operations.get_and_store_missions_from_chronos_dump(build=self, test=test)
        return None

    def add_events(self, test=False):
        """
        Stores in the database all the information about missions, taken from a JSONs: a single file about missions
        and many others about launches
        :return: None
        """

        Operations.get_and_store_events_from_chronos_dump(build=self, test=test)
        return None

    def add_sensors(self):
        """
        Stores in the database all the information about the starting set of sensors, taken from a JSONs
        :return: None
        """

        Operations.get_and_store_sensors(build=self)
        return None

    def link_targets_and_events(self, test=False):
        """
        use the tagmeapi to store annotations about targets and events stored above
        :return: None
        """

        docs = self.w.get_events_and_targets(timeout=False)
        Operations.annotate_targets_and_events(build=self, test=test, docs=docs)
        docs.close()
        return None

    def link_missions(self, test=False):
        """
        use the tagmeapi to store annotations about missions stored above
        :return: None
        """

        missions = self.w.get_all_missions(timeout=False)
        Operations.annotate_missions(build=self, test=test, missions=missions)
        missions.close()
        return None

    def relate_stored_dbpedias(self, test=False):
        """
        use the tagmeapi "rel" service to link dbpediadocs with high rho by "chronos:relatedMatch" predicate
        :return:
        """

        dbpedias = self.w.get_all_dbpediadocs(timeout=False)
        Operations.link_correlated_dbpediadocs(build=self, test=test, dbpedias=dbpedias)
        dbpedias.close()
        return None

    #
    # Layer Two
    #
    @staticmethod
    def crawl_agencies(test=False):
        """
        Does the crawling in agencies websites and store results in 'crawling' collection
        :return: None
        """
        from objectsapi.ResourceObjects.agenciesWebPages import CrawlSearchEngine
        new = CrawlSearchEngine()
        new.start_loops(test=test)  # crawl and save in crawling cache

    def crawl_google_search(self):
        # to be implemented
        pass

    def store_crawling_cache(self):
        """
        Store the documents in the 'crawling' collection
        :return: None
        """
        from objectsapi.ResourceObjects.agenciesWebPages import WebPages

        for p in self.mongod.crawling.find({}):  # query cache and store in base collection
            storeit = WebPages(cache_obj=p, publisher=p["home"])
            storeit.store_webpage_URLs()
            del storeit
        return None

    def store_webpages_mongo_documents(self):
        """
        Store webpages' documents from 'crawling' collection to 'webpages' collection
        :return:
        """
        from objectsapi.basicDocs import BasicDoc
        from datastoreapi.datastoreErrors import DocumentExists
        from tagmeapi.tagMeService import TagMeService
        from objectsapi.ResourceObjects.repoDocs import PublicRepoDocument
        agencies = ["NASA", "JAXA", "European Space Agency"]

        crawled = self.mongod.crawling.find({}, timeout=False)

        def link_webpage_to_kwd_by_abstract(docstring, url_doc):
            """
            Store link from url document to keywords based on url's abstract
            :param docstring: a string containing abstract and title of webpage
            :return: None
            """

            # retrieve annotations in the url's abstract
            try:
                results = TagMeService.retrieve_taggings(docstring, method='POST')
            except Exception:
                return None

            print(docstring)
            if len(results['annotations']) != 0:
                try:
                    results = list(l for l in results['annotations']
                                   if float(l['rho']) > 0.073 and l['title'] not in agencies)
                    print(results)
                except KeyError as e:
                    print("AgenciesWebPages.py line 174: " + str(e))
                    return
                # for a in annotations: retrieve or store wiki doc
                for a in results:
                    slug = a['title'].replace(' ', '_')
                    dbpedia = DBPEDIA_URL % slug
                    chronos_id = RESOURCE_URL % ("dbpediadocs", slug)
                    new = PublicRepoDocument(build=self, dbpedia=dbpedia)
                    try:
                        new_doc = new.store_wiki_resource()
                        if not new_doc:
                            continue
                    except DocumentExists:
                        try:
                            new_doc = self.mongod.base.find_one({"@id": chronos_id})
                        except Exception as e:
                            print(str(e) + " link_webpage_to_kwd_by_abstract() no dbpediadocs found")
                            continue

                    if new_doc["chronos:relKeyword"]:
                        for n in new_doc["chronos:relKeyword"]:
                            # if wiki doc is linked to a keyword: store link URL_doc["schema:about"]: keyword
                            try:
                                self.append_link_to_mongodoc(url_doc, "schema:about", n, "webpages")
                                print("Annotations store in url document")
                            except DocumentExists:
                                pass

                    t = self.mongod.base.find_one({"chronos:slug": slug, "chronos:group": "targets"})
                    if t:
                        # if annotation is a Target, add chronos:relTarget
                        try:
                            self.append_link_to_mongodoc(url_doc, "chronos:relTarget", t, "webpages")
                            print("Annotation of Target added")
                        except DocumentExists:
                            pass

                    m = self.mongod.base.find_one({"chronos:slug": slug, "chronos:group": "missions"})
                    if m:
                        try:
                            self.append_link_to_mongodoc(url_doc, "chronos:relMission", m, "webpages")
                            print("Annotation of Mission added")
                        except DocumentExists:
                            continue

            return None

        for res in crawled:
            at_id = RESOURCE_URL % ("urls", res["hashed"])
            check = self.mongod.webpages.find_one({"@id": at_id})
            if check is not None:
                # update keyword (append to chronos:keyword)
                kwd = self.mongod.base.find_one({
                    "@id": RESOURCE_URL % ("keywords", res["keyword"])})
                if kwd is not None:
                    try:
                        self.append_link_to_mongodoc(check, "schema:about", kwd, "webpages")
                        print("FIRST TRY: STORING Keyword Related in URLS and KWD: " + check["@id"])
                    except DocumentExists:
                        pass
            else:
                # create webpagedoc in webpages collection (BasicDoc.blank_webpage())
                publisher = res["home"]
                if res["home"] == "ESA":
                    publisher = "European_Space_Agency"
                # fill basic properties
                new = BasicDoc()
                doc = new.blank_webpage()
                del new
                doc["@id"] = at_id
                doc["chronos:base64"] = res["hashed"]
                doc["schema:url"]["@value"] = res["url"]
                doc["schema:headline"]["@value"] = res["title"]
                doc["schema:description"]["@value"] = res["abstract"]
                doc["schema:publisher"]["@value"] = publisher

                _id = self.mongod.webpages.insert(doc)
                url_doc = self.mongod.webpages.find_one(_id)
                # fill keyword
                kwd = self.mongod.base.find_one({"chronos:group": "keywords", "skos:prefLabel": res["key"]})
                if kwd is not None:
                    try:
                        self.append_link_to_mongodoc(url_doc, "schema:about", kwd, "webpages")
                        print("FIRST TRY: STORING Keyword Related in URLS and KWD: " + url_doc["@id"])
                    except DocumentExists:
                        pass

                # fill mission
                if "mission" in res.keys():
                    qm = self.mongod.base.find_one({"skos:prefLabel": res["mission"]})
                    # update the "chronos:relMission" property
                    if qm is not None:
                        try:
                            self.append_link_to_mongodoc(url_doc, "chronos:relMission", qm, "webpages")
                        except DocumentExists:
                            pass
                # set a string representing abstract and title of webpage
                if not res["abstract"]:
                    docstring = res["title"]
                else:
                    docstring = res["abstract"] + ' ' + res["title"]

                docstring = docstring.lower().replace(' ', '+')

                # fill dbpediadoc with TagMe
                link_webpage_to_kwd_by_abstract(docstring=docstring, url_doc=url_doc)
                # if res is in Targets add chronos:relTarget
                # else take annotations' dbpediadocs and schema:about their chronos:keyword

        crawled.close()
        return None

    to_be_excluded = ["Drives_(Lonnie_Smith_album)", "Internets", "Tunnels_(owarai)", "Manual_(music)",
              "Blood_plasma", "Ambient_music", "The_Plotters", "Architecture", "2C_(psychedelics)",
              "E4_(TV_channel)", "KLIM (Nestlé)"]


