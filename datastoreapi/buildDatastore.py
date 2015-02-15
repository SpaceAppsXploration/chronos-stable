__author__ = 'lorenzo'

import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from pymongo.errors import CollectionInvalid
from datastoreapi.wrapper import *
from toolbox import tools


class Build():
    """
    This class contains all the methods used in "main" package's steps
    ------------------------------------------------------------------
    It uses all the classes defined in the 'cloudapi' and 'tagmeapi' packages.

    This is the parent class for different classes defining and storing types of documents:
        :child STItaxonomyUtilities: Set of tools to process and store taxonomy concepts
        :child STIdivision: To format and store NASA taxonomy divisions, from XML to cloud
        :child STIsubject: To format and store NASA taxonomy subjects and keywords, from XML to cloud
        :child ChronosMission: To format, merge and store launches and missions data from DBpedia and old database, from file to cloud
        :child ChronosTarget: To format and store planets data from the old database, from file to cloud
        :child PublicRepoDocument: To format, link and store documents indexing external resources, from file to cloud

    :param mongod: the connection to a MongoDB instance

    :method add_ontologies: takes the ontologies file in the local directory and dumps them in the DB
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
        self.connection = Wrapper()
        self.mongod = self.connection.return_connection()

        # create collections in DB
        try:
            self.mongod.create_collection("ontology")
            self.mongod.create_collection("base")
            self.mongod.create_collection("crawling", autoIndexId=False)
            self.mongod.create_collection("webpages")
            self.mongod.create_collection("DBpediacache", autoIndexId=False)
        except CollectionInvalid:
            pass

        # create indexes in DB
        self.mongod.base.ensure_index("@id", unique=True)
        self.mongod.base.ensure_index("skos:prefLabel")
        self.mongod.base.ensure_index("chronos:group", sparse=True)
        self.mongod.crawling.ensure_index("hashed", unique=True)
        self.mongod.crawling.ensure_index("key")
        self.mongod.crawling.ensure_index("keyword")
        self.mongod.webpages.ensure_index("chronos:base64", unique=True)
        self.mongod.webpages.ensure_index("@id", unique=True)
        self.mongod.DBpediacache.ensure_index("@id", unique=True)

        import simplejson as json
        import platform
        path = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
        if platform.system() == 'Linux':
            ''' linux path '''
            path += '/SensorOntology/'
        else:
            '''  windows path  '''
            path += '\\SensorOntology\\'

        # Loading  Sensors ontology from file
        self.sensors = None
        with open(path + "SpaceSensor_json-ld_v2.json", "r", encoding="utf8") as jsonld:
            self.sensors = json.loads(jsonld.read())

        # Loading  Chronos ontology from file
        self.chronos = None
        with open(path + "ChronosOntology.json", "r", encoding="utf8") as jsonld:
            self.chronos = json.loads(jsonld.read())

        # Loading  Astronomy ontology from file
        self.astronomy = None
        with open(path + "Astronomy.json", "r", encoding="utf8") as jsonld:
            self.astronomy = json.loads(jsonld.read())

        # Loading  Engineering ontology from file
        self.engineering = None
        with open(path + "Engineering.json", "r", encoding="utf8") as jsonld:
            self.engineering = json.loads(jsonld.read())

        print("Build Constructor")
        # Finished initializing the basic building object

    #
    # Starting of the main algorithm methods
    # Step 1: add ontologies to the datastore
    #
    def add_ontologies(self):
        """
        Takes ontologies from the files and stores them as single documents in the 'ontology' collection.
        All the basic concepts and physical properties are initialized also as a 'dbpediadocs' document connected
         to the ontology documents with skos:exactMatch property
        :return:
        """
        from objectsapi.ResourceObjects.repoDocs import PublicRepoDocument
        from datastoreapi.datastoreErrors import DocumentExists

        sensors = self.sensors['defines']
        chronos = self.chronos['defines']
        astronomy = self.astronomy['defines']
        engineering = self.engineering['defines']

        ontologies = sensors + chronos + astronomy + engineering
        # from pprint import pprint
        # pprint(ontologies)

        if self.mongod.ontology.find().count() == 0:
            for doc in ontologies:
                id_ = self.mongod.ontology.insert(doc)
                if "owl:sameAs" in doc.keys() and doc["owl:sameAs"].find('dbpedia.org') != -1:
                    new_url = doc["owl:sameAs"]
                    try:
                        new = PublicRepoDocument(dbpedia=new_url)
                        resource = new.store_wiki_resource()
                        del new
                    except DocumentExists:
                        try:
                            look_for = PRAMANTHA_URL % ('dbpediadocs', tools.from_dbpedia_url_return_slug(doc["owl:sameAs"]))
                            print(look_for)
                            resource = self.mongod.base.find_one({"@id": look_for})
                        except Exception as e:
                            print(str(e) + " link_webpage_to_kwd_by_abstract() no dbpediadocs found")
                            continue
                    if resource is not None:
                        self.connection.append_link_to_mongodoc(resource, "skos:exactMatch", doc, "base")

                print(id_)

        return None

    # Step 2: add SKOS concepts
    @staticmethod
    def add_all_concepts():
        """
        Looks for concepts in bs4 XML-DOM, loops over all and stores them using XMLskos.store_sti_document
        :return: None
        """
        # load XML-munching utilities
        from objectsapi.XMLstringHandler.XMLskos import XMLskos
        from input.JPLSKOS.jpl_skos import jpl_skos_xml

        xml_processing = XMLskos(xml_string=jpl_skos_xml)
        # add root object
        xml_processing.add_root()

        # loop all the skos:concept in the file
        for obj in xml_processing.return_soup().find_all('skos:concept'):
            obj_code = obj.find("nt2:code").string
            print(obj_code)
            xml_processing.store_sti_document(obj, obj_code)

        del xml_processing
        return None

    # Step 3: add hierarchical links among concepts
    @staticmethod
    def add_all_linked():
        """
        Stores in the database all the hierarchical information in the SKOS-XML string
        :return: None
        """
        # load XML-munching utilities
        from objectsapi.XMLstringHandler.XMLskos import XMLskos
        from input.JPLSKOS.jpl_skos import jpl_skos_xml

        xml_processing = XMLskos(xml_string=jpl_skos_xml)

        # add links
        for obj in xml_processing.return_soup().find_all('skos:concept'):
            xml_processing.link_sti_document(obj)

        xml_processing.check_concept_complete()

        del xml_processing
        return None

    # Step 4: semantic linking for concepts
    def tag_keywords_and_subjects(self):
        """
        use the tagmeapi to store annotations about keywords and subjects
        :return: None
        """
        from tagmeapi.tagMeOperation import TagMeOperation
        new = TagMeOperation()
        new.insert_sections()
        keywords = self.mongod.base.find(
            {
                "$or": [
                    {"chronos:group": "keywords"},
                    {"chronos:group": "subjects"},
                    {"chronos:group": "areas"}
                ]
            },
            timeout=False
        )

        # add dbpedia documents semantically linked to detector ontologies

        for k in keywords:
            print("KEYWORD >>> ", k["skos:prefLabel"])
            try:
                new.link_annotated_keywords_and_subjects(k)
            except Exception as e:
                print("Tagging Keyword: " + str(e))
                continue

        keywords.close()
        del new

    # Layer One
    @staticmethod
    def add_targets():
        """
        Stores in the database all the information about missions' targets, taken from a JSON file
        and also stores annotations about the given target
        :return: None
        """
        from tagmeapi.tagMeOperation import TagMeOperation
        from objectsapi.ChronosObjects.chronosTarget import CHRONOStarget
        from input.Targets.targets import Chronos_Targets

        ops = TagMeOperation()
        for t in Chronos_Targets:
            new = CHRONOStarget(t)
            # store target
            new.store_target()
            del new

        del ops

        return None

    @staticmethod
    def add_missions():
        """
        Stores in the database all the information about missions, taken from a JSONs: a single file about missions
        and many others about launches
        :return: None
        """
        from objectsapi.ChronosObjects.chronosMission import CHRONOSmission
        from input.Missions.missions import Chronos_Missions
        from input.Launches.GetLaunches import get_launches_from_file

        # aggregate missions by codename
        missions_to_store = {}

        for m in Chronos_Missions:
            if m["codename"] not in missions_to_store.keys():
                missions_to_store[m["codename"]] = m
                target = missions_to_store[m["codename"]]["target"]
                missions_to_store[m["codename"]]["target"] = list()
                missions_to_store[m["codename"]]["target"].append(target)
            else:
                missions_to_store[m["codename"]]["target"].append(m["target"])
                if "slug" in m:
                    missions_to_store[m["codename"]]["slug"] = m["slug"]
        missions_to_store = list(missions_to_store.values())

        # from pprint import pprint
        # pprint(missions_to_store)

        # first part added from mission.py file
        for m in missions_to_store:
            new = CHRONOSmission(m)
            new.store_mission()

        # second part added from Launches directory
        history = get_launches_from_file()
        for year in history.keys():
            for m in history[year]:
                new = CHRONOSmission(m)
                new.store_launch(year)

        return None

    @staticmethod
    def add_events():
        from toolbox import tools
        from input.Details.missions_ids import missions_ids
        from objectsapi.ChronosObjects.chronosEvent import CHRONOSEvent

        for i in missions_ids:
            # retrieve events referred to a mission from old APIs
            js = tools.retrieve_json("http://www.spacexplore.it:80/api/missions/details/" + str(i))
            new = CHRONOSEvent(i, js)
            new.store_event()

        return None

    def link_targets_and_events(self):
        """
        Establishes "chronos:relatedDoc" predicate to Targets and Missions documents
        :return: None
        """
        from tagmeapi.tagMeOperation import TagMeOperation

        ops = TagMeOperation()
        docs = self.mongod.base.find(
            {"$or": [
                {"chronos:group": "targets"},
                {"chronos:group": "events"}
            ]},
            timeout=False)

        for d in docs:
            ops.store_annotations_for_targets_and_events(doc=d)

        del ops
        docs.close()
        return None

    def semantic_links_for_missions(self):
        from toolbox import surfing
        from tagmeapi.tagMeService import TagMeService, BadRequest
        from objectsapi.ResourceObjects.repoDocs import PublicRepoDocument
        from datastoreapi.datastoreErrors import DocumentExists, DocumentExistNot

        def tag_and_link_resources_to_mission(mssn, txt):
            # retrieve_taggings(body of the resource)
            # find annotations in the db
            # store link: annotation objects["chronos:relMission"] = mission object
            try:
                found = TagMeService.retrieve_taggings(txt)
            except BadRequest:
                raise BadRequest('retrieve_taggings in semantic_links_for_missions() Failed')

            # print(found)

            if found["annotations"]:
                for f in found["annotations"]:
                    try:
                        alt_label = f["title"].replace(" ", "_")
                    except KeyError:
                        continue
                    doc = self.mongod.base.find_one({"skos:altLabel": alt_label})
                    if doc is None:
                        # store resource and link resource[chronos:mission] = mission document
                        new_url = DBPEDIA_URL % alt_label
                        new = PublicRepoDocument(dbpedia=new_url)
                        new_doc = new.store_wiki_resource()
                        del new
                        if new_doc is None:
                            return
                        self.connection.append_link_to_mongodoc(new_doc, "chronos:relMission", mssn, "base")

                    else:
                        # link resource[chronos:mission] = mission document
                        try:
                            self.connection.append_link_to_mongodoc(doc, "chronos:relMission", mssn, "base")
                        except DocumentExists:
                            pass

            return None

        missions = self.mongod.base.find({"chronos:group": "missions"}, timeout=False)

        for m in missions:
            # get resource
            # get body of the resource
            to_crawl = m["owl:sameAs"][0]["@value"]  # "http://dbpedia.org/data/Clementine_(spacecraft).jsond"
            try:
                new = surfing.JsonLD()
                text = new.get_body_text_from_dbpedia_json(to_crawl)
                del new
            except DocumentExistNot:
                continue
            tag_and_link_resources_to_mission(m, text)

        missions.close()
        return None

    def relate_stored_dbpedias(self):
        """
        loops through all dbpedia stored and check if there are high-rhos relating.
        if yes link resources with "chronos:relatedMatch"
        :return:
        """
        from toolbox import surfing
        from datastoreapi.datastoreErrors import DocumentExists
        from tagmeapi.tagMeService import TagMeService

        dbpedias = self.mongod.base.find({"chronos:group": "dbpediadocs"}, timeout=False)

        for d in dbpedias:
            # relate with the rest of dbpedias
            # filter by rhos
            # link each other chronos:relatedMatch
            name = tools.from_dbpedia_url_return_slug(d["owl:sameAs"][0]["@value"])
            for d2 in dbpedias:
                ops = surfing.JsonLD()
                comparing = tools.from_dbpedia_url_return_slug(d2["owl:sameAs"][0]["@value"])
                del ops
                if name != "Space" and comparing != "Space" and name != comparing:
                    print("Relating...")
                    output = TagMeService.relate(name, comparing, min_rho=0.67)
                    if len(output) != 0:
                        print(">>>>>>>>>>>>>>>> Linking " + name + " with " + comparing)
                        try:
                            self.connection.append_link_to_mongodoc(d, "chronos:relatedMatch", d2, "base")
                        except DocumentExists:
                            pass
                        try:
                            self.connection.append_link_to_mongodoc(d2, "chronos:relatedMatch", d, "base")
                        except DocumentExists:
                            pass
        dbpedias.close()
        return None

    @staticmethod
    def crawl_agencies():
        """
        Does the crawling in agencies websites and store results in 'crawling' collection
        :return: None
        """
        from objectsapi.ResourceObjects.agenciesWebPages import CrawlSearchEngine
        new = CrawlSearchEngine()
        new.start_loops()  # crawl and save in crawling cache

    def crawl_google_search(self):
        # to be implemented
        pass

    def store_crawling_cache(self):
        """
        Store in the documents in the 'crawling' collection
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
            results = TagMeService.retrieve_taggings(docstring, method='POST')
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
                    chronos_id = PRAMANTHA_URL % ("dbpediadocs", slug)
                    new = PublicRepoDocument(dbpedia=dbpedia)
                    try:
                        new_doc = new.store_wiki_resource()
                        if new_doc is None:
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
                                self.connection.append_link_to_mongodoc(url_doc, "schema:about", n, "webpages")
                                print("Annotations store in url document")
                            except DocumentExists:
                                pass

                    t = self.mongod.base.find_one({"chronos:slug": slug, "chronos:group": "targets"})
                    if t:
                        # if annotation is a Target, add chronos:relTarget
                        try:
                            self.connection.append_link_to_mongodoc(url_doc, "chronos:relTarget", t, "webpages")
                            print("Annotation of Target added")
                        except DocumentExists:
                            pass

                    m = self.mongod.base.find_one({"chronos:slug": slug, "chronos:group": "missions"})
                    if m:
                        try:
                            self.connection.append_link_to_mongodoc(url_doc, "chronos:relMission", m, "webpages")
                            print("Annotation of Mission added")
                        except DocumentExists:
                            continue

            return None

        for res in crawled:
            at_id = PRAMANTHA_URL % ("urls", res["hashed"])
            check = self.mongod.webpages.find_one({"@id": at_id})
            if check is not None:
                # update keyword (append to chronos:keyword)
                kwd = self.mongod.base.find_one({
                    "@id": PRAMANTHA_URL % ("keywords", res["keyword"])})
                if kwd is not None:
                    try:
                        self.connection.append_link_to_mongodoc(check, "schema:about", kwd, "webpages")
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
                        self.connection.append_link_to_mongodoc(url_doc, "schema:about", kwd, "webpages")
                        print("FIRST TRY: STORING Keyword Related in URLS and KWD: " + url_doc["@id"])
                    except DocumentExists:
                        pass

                # fill mission
                if "mission" in res.keys():
                    qm = self.mongod.base.find_one({"skos:prefLabel": res["mission"]})
                    # update the "chronos:relMission" property
                    if qm is not None:
                        try:
                            self.connection.append_link_to_mongodoc(url_doc, "chronos:relMission", qm, "webpages")
                        except DocumentExists:
                            pass
                # set a string representing abstract and title of webpage
                if res["abstract"] is None:
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

