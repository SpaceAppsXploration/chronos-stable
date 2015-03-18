"""
Base Class to create an instance of type ChronosTarget from a static JSON file
and store it into the MongoDB instance
"""

from datastoreapi.Wrapper import *
from toolbox import tools
from datastoreapi.datastoreErrors import DocumentExists
from objectsapi.XMLstringHandler.XMLtaxonomyUtilities import SKOSconcepts


class CHRONOStarget:
    def __init__(self, build, obj):
        self.build = build  # instance of Build running the building process
        self.obj = obj
        # create a blank node to handle the collection of divisions
        self.coll = {
            "@language": "en",
            "@type": SKOS_COLLECTION,
            "schema:provider": [dict({
                "@value": "http://projectchronos.eu/org",
                "@type": RDF_RESOURCE
            })],
            "@id": "_:bodies1",
            "skos:prefLabel": "celestial bodies collection",
            "skos:editorialNote": {
                "@value": "Collection of celestial bodies targeted by Missions",
                "@type": RDF_PLAIN_LITERAL
            }, "skos:memberList": []
        }

        self.concept_utilities = SKOSconcepts(build=self.build)  # instance of the concept utilities

    def store_target(self):
        """
        store a target instance in Mongo
        :return: the name of the target/astronomical object
        """

        # import blank document
        from objectsapi.basicDocs import BasicDoc
        new = BasicDoc()
        doc = new.blank_target()
        del new

        from toolbox.pediacache import DBpediaCache
        new = DBpediaCache()
        try:
            new.get_or_retrieve_and_store(self.obj["slug"])
        except Exception:
            print("CANNOT FIND SPARQL FOR CACHING!")
            pass
        del new

        # set basic keys
        doc["@id"] = RESOURCE_URL % ("targets", self.obj["slug"])
        doc["@type"] = self.obj["body_type"]
        doc["owl:sameAs"][0]["@value"] = DBPEDIA_URL % (self.obj["slug"])
        xml = tools.get_resource_url_from_jsond_url(self.obj["slug"])
        doc["owl:sameAs"][1]["@value"] = xml
        doc["skos:prefLabel"] = self.obj["name"]
        doc["chronos:slug"] = self.obj["slug"]
        doc["chronos:idFromDb"] = self.obj["id"]
        doc["chronos:abstract"]["@value"] = self.obj["characteristics"]
        doc["chronos:imageUrl"]["@value"] = self.obj["image_url"]
        doc["chronos:curiosities"]["@value"] = self.obj["curiosities"]
        doc["chronos:simRelated"]["@value"] = self.obj["sim_related"]
        doc["chronos:useInSim"]["@value"] = self.obj["use_in_sim"]

        check = self.build.mongod.base.find_one({"@id": doc["@id"]})
        if check is None:
            # body is not in the KB, create resource
            body_id = self.build.mongod.base.insert(doc)
            body_doc = self.build.mongod.base.find_one({"_id": body_id})
            print(body_doc["@id"])

            # append to memberList of collection
            blank = self.concept_utilities.find_or_create_collection("_:bodies1", self.coll)
            try:
                self.build.append_link_to_mongodoc(blank, "skos:memberList", body_doc, "base")
            except DocumentExists:
                pass

            return body_doc

        return check