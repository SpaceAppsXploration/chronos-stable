#
# Base Class to create an instance of type NASA-STI Division from the bs4 SKOS-XML taxonomy
# and store it into the MongoDB instance
#

from datastoreapi.Wrapper import *
from datastoreapi.datastoreErrors import DocumentExists
from objectsapi.XMLstringHandler.XMLtaxonomyUtilities import SKOSconcepts


class STIdivision():
    def __init__(self, obj):
        self.connection = Wrapper()
        self.mongod = self.connection.return_mongo()
        # concept object from xml to convert
        self.obj = obj
        self.code = str(obj.find("nt2:code").string)

        # blank collection
        # import blank document
        from objectsapi.basicDocs import BasicDoc

        self.div_collection = BasicDoc.blank_division_collection()

        # blank division
        self.division = BasicDoc.blank_division()
        self.division["chronos:code"] = self.code
        self.provider = self.mongod.base.find_one({
            "@id": PRAMANTHA_URL % ("organization", "NASA+Sientific+and+Technical+Information+Program")
        })

        self.concept_utilities = SKOSconcepts()  # instance of the concept to store into a document

    def store_division_concept(self):
        pref_label, this_id = self.concept_utilities.make_id_from_concept(self.obj, "divisions")

        check = self.mongod.base.find_one({"@id": this_id})
        if not check:
            self.division["@id"] = this_id
            self.division["skos:prefLabel"] = pref_label
            self.division["skos:scopeNote"][0]["@value"] = self.obj.find("skos:scopenote").string
            id_ = self.mongod.base.insert(self.division)
            this_doc = self.mongod.base.find_one({"_id": id_})
            try:
                self.connection.append_link_to_mongodoc(this_doc, "schema:provider", self.provider, "base")
            except DocumentExists:
                pass

            new_collection = self.concept_utilities.find_or_create_collection("_:allDivisions", self.div_collection)
            try:
                self.connection.append_link_to_mongodoc(new_collection, "skos:memberList", this_doc, "base")
            except DocumentExists:
                pass

        raise DocumentExists
