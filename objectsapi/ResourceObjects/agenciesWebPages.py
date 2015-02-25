from datastoreapi.Wrapper import *
from toolbox import tools
from datastoreapi.datastoreErrors import DocumentExists
from objectsapi.XMLstringHandler.XMLtaxonomyUtilities import SKOSconcepts

from objectsapi.basicDocs import BasicDoc

agencies = ["NASA", "JAXA", "European Space Agency"]


class CrawlSearchEngine:
    """
    Crawl links directly to Agencies website or through search engines' API
    """
    def __init__(self):
        self.connection = Wrapper()
        self.db = self.connection.return_mongo()

    def start_loops(self, test):
        ### import scraping lib from local directory
        import scraping.agenciesScraperUtils as Scraping

        def nasa_crawling():
            ### loop for NASA search
            cursor = self.db.base.find({"chronos:group": "keywords"}, timeout=False)
            for i, doc in enumerate(cursor):
                key = doc['skos:prefLabel']
                for keyword in doc['chronos:toSearch']:
                    url = Scraping.generate_nasa_url(keyword)
                    try:
                        html = tools.retrieve(url)
                    except ConnectionError as e:
                        print(ConnectionError("retrieve() raises and error: " + str(e)))
                        return None
                    Scraping.store_to_cache_collection(key, keyword, html, "NASA", self.db)
                if test and i > 35:
                    break
            print("NASA crawling finished")
            cursor.close()
            return None

        def esa_crawling():
            ### loop for ESA search
            cursor = self.db.base.find({"chronos:group": "keywords"}, timeout=False)
            for i, doc in enumerate(cursor):
                key = doc['skos:prefLabel']
                for keyword in doc['chronos:toSearch']:
                    url = Scraping.generate_esa_url(keyword)
                    try:
                        html = tools.retrieve(url)
                    except ConnectionError as e:
                        print(ConnectionError("retrieve() raises and error: " + str(e)))
                        return None
                    Scraping.store_to_cache_collection(key, keyword, html, "ESA", self.db)
                if test and i > 35:
                    break
            print("ESA crawling finished")
            cursor.close()
            return None

        def jaxa_crawling():
            ### loop for JAXA search
            cursor = self.db.base.find({"chronos:group": "keywords"}, timeout=False)
            for i, doc in enumerate(cursor):
                key = doc['skos:prefLabel']
                for keyword in doc['chronos:toSearch']:
                    url = Scraping.generate_jaxa_url(keyword)
                    html = Scraping.retrieve_webdriver(url)
                    Scraping.store_to_cache_collection(key, keyword, html, "JAXA", self.db)
                if test and i > 35:
                    break
            print("JAXA crawling finished")
            cursor.close()
            return None

        print("Start NASA crawling")
        nasa_crawling()
        print("Start ESA crawling")
        esa_crawling()
        print("Start JAXA crawling")
        jaxa_crawling()
        return None


class WebPages:
    """
    Store webpages data from static files or from cache
    """
    def __init__(self, cache_obj=None, publisher=None, obj=None):
        self.connection = Wrapper()
        self.db = self.connection.return_mongo()
        self.cache_obj = cache_obj  # used to store from cache, if None store from static files
        self.obj = obj

        if publisher == "ESA":
            self.publisher = "European_Space_Agency"
        else:
            self.publisher = publisher

        self.concept_utilities = SKOSconcepts()  # instance of the concept utilities

    def store_webpage_URLs(self):
        from base64 import b64encode, b64decode

        from tagmeapi.tagMeService import TagMeService
        from objectsapi.ResourceObjects.repoDocs import PublicRepoDocument

        mission = None
        if self.obj is not None:
            mission = self.obj["mission"]

        def store_single_url(link, title, abstract, single_keyword=None):
            """
            This method can store a single webpage or a list.
            """
            import re

            if re.match(r"^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$", link):
                hashed = link
                try:
                    link = b64decode(link).decode(encoding='UTF-8')
                except Exception as e:
                    print(str(e) + link)
            else:
                to_hash = link.encode(encoding='UTF-8')
                avoid = '_-'.encode(encoding='UTF-8')
                hashed = b64encode(to_hash, avoid).decode(encoding='UTF-8')

            obj_id = PRAMANTHA_URL % ("urls", hashed)

            if self.db.urls.find_one({"@id": obj_id}) is not None:
                return

            # create basic webpage document
            doc = BasicDoc.blank_webpage()
            doc["@id"] = obj_id
            doc["chronos:base64"] = hashed
            doc["schema:url"]["@value"] = link
            doc["schema:headline"]["@value"] = title
            doc["schema:description"]["@value"] = abstract

            ####print(doc)
            print(hashed)
            check = self.db.webpages.find_one({"chronos:base64": hashed})
            if not check:
                #print("NEW PAGE")
                _id = self.db.webpages.insert(doc)
                url_doc = self.db.webpages.find_one(_id)

            else:
                url_doc = check

            if self.obj is not None:
                kwd = self.db.base.find_one({
                    "@id": PRAMANTHA_URL % ("keywords", self.obj["keyword"].lower().replace(' ', '+'))})
            else:
                kwd = self.db.base.find_one({
                    "@id": PRAMANTHA_URL % ("keywords", single_keyword)})
            if kwd is not None:
                try:
                    self.connection.append_link_to_mongodoc(url_doc, "schema:about", kwd, "webpages")
                    print("FIRST TRY: STORING Keyword Related in URLS and KWD: " + url_doc["@id"])
                except DocumentExists:
                    pass

            # set a string representing abstract and title of webpage
            if abstract is None:
                docstring = title
            else:
                docstring = abstract + ' ' + title

            docstring = docstring.lower().replace(' ', '+')

            def link_webpage_to_kwd_by_abstract(docstring):
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
                                       if float(l['rho']) > 0.26 and l['title'] not in agencies)
                        print(results)
                    except KeyError as e:
                        print("AgenciesWebPages.py line 174: " + str(e))
                        return
                    # for a in annotations: retrieve or store wiki doc
                    for a in results:
                        dbpedia = DBPEDIA_URL % a['title'].replace(' ', '_')
                        chronos_id = PRAMANTHA_URL % ("dbpediadocs", a['title'].replace(' ', '_'))
                        new = PublicRepoDocument(dbpedia=dbpedia)
                        try:
                            new_doc = new.store_wiki_resource()
                            if new_doc is None:
                                continue
                        except DocumentExists:
                            try:
                                new_doc = self.db.base.find_one({"@id": chronos_id})
                            except Exception as e:
                                print(str(e) + " link_webpage_to_kwd_by_abstract() no dbpediadocs found")
                                continue

                        if new_doc["chronos:relKeyword"]:
                            for n in new_doc["chronos:relKeyword"]:
                                # if wiki doc is linked to a keyword: store link URL_doc > keyword
                                try:
                                    self.connection.append_link_to_mongodoc(url_doc, "schema:about", n, "webpages")
                                    print("Annotations store in url document")
                                except DocumentExists:
                                    continue

                return None

            link_webpage_to_kwd_by_abstract(docstring=docstring)

            # loop for linking to Targets
            targets = self.db.base.find({"chronos:group": "targets"})
            for t in targets:
                search = t["skos:prefLabel"]
                if docstring.find(search) != -1:
                    t_doc = t
                    if t_doc is not None:
                        self.connection.append_link_to_mongodoc(url_doc, "chronos:relMission", t_doc, "webpages")

            ### loop for finding the mission for chronos:mission link
            # look for all missions
            if mission is not None:
                qm = self.db.base.find_one({"skos:prefLabel": mission})
                # update the skos:related property
                if qm is not None:
                    try:
                        self.connection.append_link_to_mongodoc(url_doc, "chronos:relMission", qm, "webpages")
                    except DocumentExists:
                        pass

        if self.cache_obj is None:
            for u in self.obj["urls"]:
                store_single_url(u["link"], u["abstract"], u["title"])
        else:
            #find single_url in crawling
            o = self.db.crawling.find_one({"hashed": self.cache_obj["hashed"]})
            #store_single_url(link, title, abstract)
            store_single_url(self.cache_obj["hashed"], o["title"], o["abstract"], o["keyword"])
            # flag the document in "crawling" as "stored"
            o["stored"] = True
            self.db.crawling.update({"hashed": self.cache_obj["hashed"]}, o)
            print("cache doc flagged as 'stored'")

        return None


if __name__ == "__main__":
    print("This is a useful module, not a stand-alone script")