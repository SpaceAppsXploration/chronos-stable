

from bson.objectid import ObjectId
from urllib.parse import quote, unquote
from pprint import pprint

from datastoreapi.Wrapper import *
from datastoreapi.datastoreErrors import *
from objectsapi.ResourceObjects.repoDocs import PublicRepoDocument
from toolbox import tools
from tagmeapi.tagMeService import TagMeService, ConceptNotInDBpedia, BadRequest, TextNotSpotted


class TagMeOperation:
    """
    Contains methods that use TagMeService to operate on the database
    -----------------------------------------------------------------
    """
    def __init__(self, build):
        self.build = build  # instance of Build

    # return general arguments from the TagMeService class
    include = TagMeService.return_gen_scopes()


    @classmethod
    def return_gen_lowered(cls):
        return [x.lower() for x in cls.include]

    @classmethod
    def semantic_test(cls, annotation):
        if "rho" in annotation.keys() \
                and 0.40 < float(annotation["rho"]) < 0.72 \
                or any([True for c in annotation["dbpedia_categories"]
                        for w in c.split() if w.lower() in cls.return_gen_lowered()]):
            return True
        return False

    def insert_sections(self):
        """
        Take the titles of general scopes and insert them as a dbpedia docs in mongo
        :return: None
        """
        rlts = map(tools.make_resource_url_from_slug, TagMeService.return_gen_scopes())
        print("INSERTING SECTIONS")

        for i, t in enumerate(rlts):
            print(t)
            # insert resourcs in Mongo with "chronos:section": true
            inc = PublicRepoDocument(build=self.build, dbpedia=t)
            try:
                doc = inc.store_wiki_resource()
            except DocumentExists as e:
                # sections are probably already stored
                # doc = self.db.base.find_one({"@id": self.CHRONOS_URL % ("dbpediadocs", TagMeService.return_gen_scopes()[i])})
                return

            doc["chronos:section"] = True
            self.build.mongod.base.find_and_modify({"_id": doc["_id"]}, doc)

        return None

    @staticmethod
    def check_if_rho_fits_spaceknowledge(output, level=0.42):
        """
        Takes as input the results of a TagMeService.relate() function and check if the mean of resulting rhos is
        above a level. Used to check if a term is semantically related to a list of fields
        [refer to argument "comparing" in relate()]
        :param output: what returns the TagMeService.relate()
        :param level: the level at which to filter the mean of the rhos in the results
        :return: boolean
        """
        if output is not None:
            count = len(output)
            zeros = 0
            if count != 0:
                total = 0.0
                for o in output:
                    if float(o["rel"]) == 0.0000:
                        zeros += 1
                    else:
                        total += float(o["rel"])
                mean = total / count
                print(mean)
                if level < mean < 0.61 and zeros < 8:
                    return True
            return False
        return False

    def link_annotated_keywords_and_subjects(self, c):
        """
        Store to dbpedia docs the links taken from the annotation API:
        add dbpedia categories found annotating the keyword
        add abstract found annotating the keyword

        links to keywords and to subjects (using "chronos:relKeyword" property from dbpedia docs to keywords)
        --------------------------------------------------------------------------------------------------
        :param c: results from cls.relate_with_space_knowledge(term)
        :return: None
        """

        # keyword > clean keyword (no parenthesis, no commas)
        label = c["skos:prefLabel"].replace("(", "").replace(")", "").replace(",", "")
        print("KEYWORD FROM DB: " + label)
        check = TagMeService.check_spotting(label)  # return
        print("SPOTTING: " + str(check))
        if check["spotted"]:
            spotted = check["value"]["spots"]
            for sp in spotted:
                # for spot in keyword: retrieve taggings return annotations
                term = sp["spot"]
                try:
                    annotations = TagMeService.retrieve_taggings(term)["annotations"]
                except BadRequest as e:
                    raise e
                if annotations:
                    for a in annotations:
                        # make the wikipedia official title in url
                        slug = a["title"].replace(" ", "_")
                        print(term, slug)
                        # find if this term is related to space arguments

                        if self.check_if_rho_fits_spaceknowledge(TagMeService.relate(titles=slug, min_rho=0.39)):
                            #    # store or modify dbpediadoc with chronos:relKeyword to the keyword
                            # if self.semantic_test(a):
                            self.store_annotation_for_keyword(annotation=slug, keyword=c["skos:prefLabel"])
        else:
            raise TextNotSpotted('No terms in the text to spot')

        return label

    def store_annotation_for_keyword(self, annotation, keyword):
        """
        Take an annotation from the "tagging" API and create or modify a dbpediadoc in Mongo linking it with
        "chronos:relKeyword" property to the keyword
        ------------------------------------------------------------------------------------
        :param annotation: the annotation slug as sent by TagMe
        :param keyword: the full NASA keyword from which this annotation is taken
        :return: Mongo document ("chronos:group": "dbpediadocs") that is the new or modified document
        """
        print("------------------------------------------------------------------")
        print(annotation, keyword)

        # take the title from the API response and get the slug
        slug = annotation.replace(" ", "_")
        # dbpedia json url
        dbpedia = tools.make_resource_url_from_slug(slug)

        if slug in to_be_excluded:
            # slug is in the set of excluded pedia terms
            return

        # create the dbpediadocs to be stored
        to_store = PublicRepoDocument(build=self.build, dbpedia=dbpedia)

        try:
            doc = to_store.store_wiki_resource()
            print("DOC STORED")
        except DocumentExists as e:
            doc = self.build.mongod.base.find_one({"@id": RESOURCE_URL % ("dbpediadocs", slug)})
            print("DOC FETCHED: " + dbpedia)

        pprint(doc)  #complete doc

        # link dbpedia doc with narrowMatch to keyword
        kw = self.build.mongod.base.find_one({"skos:prefLabel": keyword,
                                    "$or": [
                                        {"chronos:group": "keywords"},
                                        {"chronos:group": "subjects"}
                                    ]})
        print("KEYWORD: ")
        if kw is not None:
            pprint(kw["@id"])
            try:
                id_ = self.build.append_link_to_mongodoc(doc, "chronos:relKeyword", kw, "base")["_id"]
            except DocumentExists:
                id_ = doc["_id"]
        else:
            print("KEYWORD NOT FOUND")
            return

        # return the dbpediadoc that has been created or modified
        print("MEAN OK: Store Annotation: " + str(doc["@id"]))
        return self.build.mongod.base.find_one({"_id": ObjectId(id_)})

    def store_annotations_for_targets_and_events(self, doc):
        """
        Establishes "chronos:relMission" or "chronos:relTarget" predicate to Targets and Missions documents
        :param doc:
        :return: None
        """

        event = False
        target = False

        if doc["chronos:group"] == "targets":
            abst = doc["chronos:abstract"]["@value"]
            target = True
        elif doc["chronos:group"] == "events":
            event = True
            if doc["chronos:eventContent"]["@type"] == "https://schema.org/Text":
                abst = doc["chronos:eventContent"]["@value"]
            else:
                # event abstract is a link
                return
        else:
            return
        print(abst)
        spotted = TagMeService.check_spotting(abst)
        if spotted["spotted"]:
            for sp in spotted["value"]["spots"]:
                if float(sp["lp"]) > 0.1:
                    print(sp)
                    annotations = TagMeService.retrieve_taggings(sp["spot"])
                    for a in annotations["annotations"]:
                        print(a)
                        try:
                            title = a["title"].replace(" ", "_")
                        except KeyError:
                            continue
                        # check if title is related to space knowledge
                        if TagMeOperation.check_if_rho_fits_spaceknowledge(
                                TagMeService.relate(titles=title, min_rho=0.39)
                        ):
                            check = self.build.mongod.base.find_one({"chronos:group": "dbpediadocs", "skos:altLabel": title})
                            if not check:
                                to_store = PublicRepoDocument(build=self.build, dbpedia=DBPEDIA_URL % title)
                                try:
                                    check = to_store.store_wiki_resource()
                                except DocumentExists:
                                    pass

                            if event:
                                try:
                                    self.build.append_link_to_mongodoc(check, "chronos:relEvent", doc, "base")
                                except DocumentExists:
                                    continue

                            to_link = self.build.mongod.base.find({"chronos:slug": title})
                            if to_link is not None:
                                for l in to_link:
                                    # if a type target or mission with the same title exists
                                    if l["chronos:group"] == "targets":
                                        prop = "chronos:relTarget"
                                    elif l["chronos:group"] == "missions":
                                        prop = "chronos:relMission"
                                    else:
                                        continue
                                    try:
                                        self.build.append_link_to_mongodoc(check, prop, l, "base")
                                    except DocumentExists:
                                        continue
                                continue

        return None

    def tag_and_link_resources_to_mission(self, mssn, txt):
        # retrieve_taggings(body of the resource)
        # find annotations in the db
        # store link: annotation objects["chronos:relMission"] = mission object
        import html.parser

        print("semantic_links_for_missions()" + str(mssn))

        try:
            found = TagMeService.retrieve_taggings(txt)
        except BadRequest:
            raise BadRequest('retrieve_taggings in semantic_links_for_missions() Failed')

        # print(found)
        if found["annotations"]:
            for f in found["annotations"]:
                try:
                    h = html.parser.HTMLParser()
                    slug = f["title"].replace(" ", "_")
                    slug = h.unescape(slug)
                    del h
                except KeyError:
                    continue
                if self.check_if_rho_fits_spaceknowledge(TagMeService.relate(titles=slug, min_rho=0.39)):
                    try:
                        alt_label = f["title"].replace(" ", "_")
                        print(alt_label)
                    except KeyError:
                        continue
                    doc = self.build.mongod.base.find_one({"skos:altLabel": alt_label})
                    if not doc:
                        # store resource and link resource[chronos:mission] = mission document
                        new_url = DBPEDIA_URL % alt_label
                        new = PublicRepoDocument(build=self.build, dbpedia=new_url)
                        new_doc = new.store_wiki_resource()
                        del new
                        if not new_doc:
                            continue
                        self.build.append_link_to_mongodoc(new_doc, "chronos:relMission", mssn, "base")

                    else:
                        # link resource[chronos:mission] = mission document
                        try:
                            self.build.append_link_to_mongodoc(doc, "chronos:relMission", mssn, "base")
                        except DocumentExists:
                            pass

        return None


to_be_excluded = ["Drives_(Lonnie_Smith_album)", "Internets", "Tunnels_(owarai)", "Manual_(music)",
                  "Blood_plasma", "Ambient_music", "The_Plotters", "Architecture", "2C_(psychedelics)",
                  "E4_(TV_channel)", "KLIM (Nestlé)"
]