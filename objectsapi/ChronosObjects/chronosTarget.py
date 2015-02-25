"""
Base Class to create an instance of type ChronosTarget from a static JSON file
and store it into the MongoDB instance
"""

from datastoreapi.Wrapper import *
from toolbox import tools
from datastoreapi.datastoreErrors import DocumentExists
from objectsapi.XMLstringHandler.XMLtaxonomyUtilities import SKOSconcepts


class CHRONOStarget:
    def __init__(self, obj):
        self.connection = Wrapper()
        self.db = self.connection.return_mongo()
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

        self.concept_utilities = SKOSconcepts()  # instance of the concept utilities

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

        # set basic keys
        doc["@id"] = PRAMANTHA_URL % ("targets", self.obj["slug"])
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

        check = self.db.base.find_one({"@id": doc["@id"]})
        if not check:
            # body is not in the KB, create resource
            body_id = self.db.base.insert(doc)
            body_doc = self.db.base.find_one({"_id": body_id})
            print(body_doc["@id"])

            # append to memberList of collection
            blank = self.concept_utilities.find_or_create_collection("_:bodies1", self.coll)
            try:
                self.connection.append_link_to_mongodoc(blank, "skos:memberList", body_doc, "base")
            except DocumentExists:
                pass

            return body_doc

        return check