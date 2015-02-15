import time
import json
from pprint import pprint

from main.mongod import get_connection
from datastoreapi.buildDatastore import Build
from toolbox import tools
from datastoreapi.datastoreErrors import DocumentExists
from datastoreapi.XMLstringHandler.XMLtaxonomyUtilities import SKOSconcepts
from datastoreapi.basicDocs import BasicDoc


class CHRONOSmission(Build):
    """
    Take care of storing the totality of missions, merging missions from the old DB and DBpedia 'Launches' category

    :param obj: input dictionary
    :param db: Mongo client

    :method store_mission: store from old database file, has typical fields to handle
    :method store_launch: store from DBpedia file, has typical fields to handle
    :method store_hasKeyword_to_missions: loops through stored missions looking for possible links
    """
    def __init__(self, obj):
        super().__init__(mongod=get_connection())
        self.mission_obj = obj
        self.db = self.mongod
        self.concept_utilities = SKOSconcepts()  # instance of the concept utilities

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
        doc = BasicDoc.blank_mission()

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
        doc["@id"] = self.PRAMANTHA_URL % ("missions", label)

        dbpedia = self.DBPEDIA_URL % label

        doc["owl:sameAs"].append({"@value": dbpedia, "@type": self.RDF_RESOURCE})
        xml = tools.get_resource_url_from_jsond_url(dbpedia)
        doc["owl:sameAs"].append({"@value": xml, "@type": self.RDF_RESOURCE})

        if self.db.base.find_one({"@id": doc["@id"]}) is None:
            pprint("STORE MISSION: " + str(self.mission_obj["name"]))
            #print(doc)
            id_ = self.db.base.insert(doc)
            this_doc = self.db.base.find_one({"_id": id_})

            for t in self.mission_obj['target']:
                target = self.db.base.find_one({"skos:prefLabel": t})
                if target is not None:
                    try:
                        self.append_link_to_mongodoc(this_doc, "chronos:relTarget", target, "base")
                    except DocumentExists:
                        pass
                    pprint("STORE TARGET in mission")
        return None

    def store_launch(self, year):
        # add Launches from Launches_By_Year file
        # add launches from file
            # for m in missions: if json-url == sameAs SKIP
            # else store launch

        # for each mission's page
        #pprint("Mission: " + str(self.mission_obj))

        print("ADDING: LAUNCH (launch not stored yet)")
        url = self.mission_obj["json-uri"]
        instrumentation = self.mission_obj["instrumentation"]

        # find mission name from url
        from urllib.parse import unquote
        i = url.rfind('/data/')
        if i == -1:
            i = url.rfind('/page/')
        label = url[i+6:-6]
        name = unquote(label.replace('_', ' '))
        time.sleep(0.1)
        #pprint(name)

        # load res
        try:
            res = tools.retrieve(self.mission_obj["json-uri"])
            res = json.loads(res)  # check for types
        except (ConnectionError, json.JSONDecoder, json.JSONEncoder):
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
        check = self.db.base.find_one({"owl:sameAs": {"$elemMatch": {"@value": url}}})
        if check is not None:
            if len(instrumentation) != 0:
                up = check
                if not up["chronos:payload"] and not up["rdf:type"]:
                    up["chronos:payload"] = instrumentation
                    up["rdf:type"] = types
                    self.db.base.update({"_id": check["_id"]}, up)
                    pprint("INSTRUMENTS ADDING TO EXISTING MISSION >>>>:" + str(instrumentation))
                    pprint("MISSION UPDATED >>>>: " + str(check["@id"]))
                else:
                    pprint("INSTRUMENTS ALREADY ADDED TO MISSION >>>>:" + str(check["@id"]))
                return None

        if self.db.base.find_one({"@id": self.PRAMANTHA_URL % ("missions", label)}) is None:
            # create the basic document about the launch
            doc = BasicDoc.blank_launch()

            doc["@id"] = self.PRAMANTHA_URL % ("missions", label)
            doc["skos:prefLabel"] = name
            doc["chronos:year"] = year
            doc["chronos:slug"] = label
            doc["chronos:payload"] = instrumentation,

            # store the doc

            print("LAUNCH STORED: " + doc["@id"])

            doc["owl:sameAs"].append({"@value": url, "@type": self.RDF_RESOURCE})
            xml = tools.get_resource_url_from_jsond_url(url)
            doc["owl:sameAs"].append({"@value": xml, "@type": self.RDF_RESOURCE})
            # add launch types
            for t in types:
                doc["rdf:type"].append(t["value"])
            id_ = self.db.base.insert(doc)

        return None

