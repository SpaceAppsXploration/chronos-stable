import simplejson as json
from pprint import pprint

from datastoreapi.Wrapper import *
from toolbox import tools
from datastoreapi.datastoreErrors import DocumentExists
from objectsapi.XMLstringHandler.XMLtaxonomyUtilities import SKOSconcepts
from objectsapi.basicDocs import BasicDoc


class CHRONOSmission:
    """
    Take care of storing the totality of missions, merging missions from the old DB and DBpedia 'Launches' category

    :param obj: input dictionary

    :method store_mission: store from old database file, has typical fields to handle
    :method store_launch: store from DBpedia file, has typical fields to handle
    :method store_hasKeyword_to_missions: loops through stored missions looking for possible links
    """
    def __init__(self, build, obj):
        self.build = build  # instance of Build
        self.mission_obj = obj
        self.concept_utilities = SKOSconcepts(build=self.build)  # instance of the concept utilities

    def store_mission(self):
        # add missions from file
            # check slug
            # check name
            # check _ name
            # check codename
            # add sameAs
            # sub / in name for url
            # check target > add chronos:relTarget
            # black mission document

        # import blank document
        new = BasicDoc()
        doc = new.blank_mission()
        del new

        # set basic keys
        doc["chronos:missionEra"] = self.mission_obj["era"]
        doc["chronos:oldId"] = self.mission_obj["id"]
        doc["chronos:imageUrl"]["@value"] = self.mission_obj["image_url"]
        doc["schema:url"]["@value"] = self.mission_obj["link_url"]

        try:
            label = self.mission_obj["slug"]
            doc["chronos:slug"] = label
        except KeyError:
            label = self.mission_obj["name"].replace(' ', '_')

        if label.find('/') != -1:
            label = label.replace('/', '-')

        doc["skos:prefLabel"] = self.mission_obj["name"]
        doc["chronos:codename"] = self.mission_obj["codename"]
        doc["@id"] = RESOURCE_URL % ("missions", label)

        dbpedia = DBPEDIA_URL % label

        doc["owl:sameAs"].append({"@value": dbpedia, "@type": RDF_RESOURCE})
        xml = tools.get_resource_url_from_jsond_url(dbpedia)
        doc["owl:sameAs"].append({"@value": xml, "@type": RDF_RESOURCE})

        from toolbox.pediacache import DBpediaCache
        new = DBpediaCache()
        try:
            new.get_or_retrieve_and_store(label)
        except Exception:
            print("CANNOT FIND SPARQL FOR CACHING!")
            pass

        if self.build.mongod.base.find_one({"@id": doc["@id"]}) is None:
            pprint("STORE MISSION: " + str(self.mission_obj["name"]))
            # print(doc)
            id_ = self.build.mongod.base.insert(doc)
            this_doc = self.build.mongod.base.find_one({"_id": id_})

            for t in self.mission_obj['target']:
                target = self.build.mongod.base.find_one({"skos:prefLabel": t})
                if target is not None:
                    try:
                        self.build.append_link_to_mongodoc(this_doc, "chronos:relTarget", target, "base")
                    except DocumentExists:
                        pass
                    pprint("STORE TARGET in mission")
        return None

    def store_launch(self, year):
        # add Launches from Launches_By_Year file
        # add launches from file
            # for m in missions: if json-url == sameAs SKIP
            # else store launch

        print("ADDING: LAUNCH (launch not stored yet)")
        url = self.mission_obj["json-uri"]
        instrumentation = self.mission_obj["instrumentation"]

        # find mission name from url
        slug = tools.from_dbpedia_url_return_slug(url)
        name = slug.replace("_", " ")
        # pprint(name)

        # load res
        try:
            res = tools.retrieve_json(self.mission_obj["json-uri"])
        except (ConnectionError, json.JSONDecodeError):
            print("ERROR: LAUNCH >>> " + str(self.mission_obj["json-uri"]) + " >>> DBPEDIA IS PROBABLY DOWN")
            return

        to_find = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"

        #find rdf:type of the launch
        types = []
        for n, v in res.items():
            if to_find in v.keys():
                types = v[to_find]
                break

        # if mission exist, dont store the launch, but add to the mission
        check = self.build.mongod.base.find_one({"owl:sameAs": {"$elemMatch": {"@value": url}}})
        if check is not None:
            if len(instrumentation) != 0:
                up = check
                if not up["chronos:payload"] and not up["rdf:type"]:
                    up["chronos:payload"] = instrumentation
                    up["rdf:type"] = types
                    self.build.mongod.base.update({"_id": check["_id"]}, up)
                    pprint("INSTRUMENTS ADDING TO EXISTING MISSION >>>>:" + str(instrumentation))
                    pprint("MISSION UPDATED >>>>: " + str(check["@id"]))
                else:
                    pprint("INSTRUMENTS ALREADY ADDED TO MISSION >>>>:" + str(check["@id"]))
                return None

        if not self.build.mongod.base.find_one({"@id": RESOURCE_URL % ("missions", slug)}):
            # create the basic document about the launch
            new = BasicDoc()
            doc = new.blank_launch()
            del new

            doc["@id"] = RESOURCE_URL % ("missions", slug)
            doc["skos:prefLabel"] = name
            doc["chronos:year"] = year
            doc["chronos:slug"] = slug
            doc["chronos:payload"] = instrumentation,

            # store the doc

            print("LAUNCH STORED: " + doc["@id"])

            doc["owl:sameAs"].append({"@value": url, "@type": RDF_RESOURCE})
            xml = tools.get_resource_url_from_jsond_url(url)
            doc["owl:sameAs"].append({"@value": xml, "@type": RDF_RESOURCE})
            # add launch types
            for t in types:
                doc["rdf:type"].append(t["value"])
            id_ = self.build.mongod.base.insert(doc)

        return None


