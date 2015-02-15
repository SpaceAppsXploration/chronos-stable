"""
Base Class to create an instance of type NASA-STI Subject from the bs4 SKOS-XML taxonomy
and store it into the MongoDB instance
"""

from pprint import pprint

from main.mongod import get_connection
from datastoreapi.buildDatastore import Build
from datastoreapi.datastoreErrors import DocumentExists
from datastoreapi.XMLstringHandler.XMLtaxonomyUtilities import SKOSconcepts
# import blank documents
from datastoreapi.basicDocs import BasicDoc


class STIsubject(Build):
    def __init__(self, obj):
        super().__init__(mongod=get_connection())
        # html object to convert
        self.db = self.mongod
        self.obj = obj
        self.code = str(obj.find("nt2:code").string)
        # blank subject collection
        self.subj_collection = BasicDoc.blank_subject_collection()

        # blank scheme
        self.scheme = BasicDoc.blank_subject_scheme()
        self.scheme["chronos:code"] = self.code

        # blank subject (top concept)
        self.top_concept = BasicDoc.blank_subject_as_top_concept()
        self.top_concept["chronos:code"] = self.code

        self.provider = self.db.base.find_one({
            "@id": self.PRAMANTHA_URL % ("organization", "NASA+Sientific+and+Technical+Information+Program")
        })

        self.concept_utilities = SKOSconcepts()  # instance of the concept to store into a document

    def store_top_concept(self):
        """
        store Subjects as a TopConcept to wrap all the keywords related to the subject itself
        1 @id = http://domain/subjects/label
        2 add to Subjects skos:Collection _:allSubj
        3 skos:TopConceptOf = _:subjCODE
        4 ConceptScheme[skos:hasTopConcept] = TopConcept
        :return: None
        """

        pref_label, this_id = self.concept_utilities.make_id_from_concept(self.obj, "subjects")

        self.top_concept["@id"] = this_id
        self.top_concept["skos:prefLabel"] = pref_label
        self.top_concept["skos:scopeNote"]["@value"] = self.obj.find("skos:scopenote").string

        check = self.db.base.find_one({"@id": this_id})
        if check is None:
            # create subject's scheme
            new_scheme = self.concept_utilities.find_or_create_scheme("_:subj" + self.code, self.scheme)
            # add TopConcept to document
            self.top_concept["skos:topConceptOf"] = {
                "@id": new_scheme["@id"],
                "@type": new_scheme["@type"],
                "_id": new_scheme["_id"]
            }
            # insert document
            id_ = self.db.base.insert(self.top_concept)
            this_doc = self.db.base.find_one({"_id": id_})
            #append schema:provider
            try:
                self.append_link_to_mongodoc(this_doc, "schema:provider", self.provider, "base")
            except DocumentExists:
                pass
            # add hasTopConcept to the scheme
            try:
                self.append_link_to_mongodoc(new_scheme, "skos:hasTopConcept", this_doc, "base")
            except DocumentExists:
                pass
            # add document to subject's collection memberList
            new_collection = self.concept_utilities.find_or_create_collection("_:allSubj", self.subj_collection)
            try:
                self.append_link_to_mongodoc(new_collection, "skos:memberList", this_doc, "base")
            except DocumentExists:
                pass

            return this_doc

        return check

    def add_keyword(self, keyword, subject_top_doc):
        # blank keyword
        kw_doc = BasicDoc.blank_keyword()
        kw_doc["skos:altLabel"] = keyword.replace(' ', '+').replace(',', '')

        label, this_id = self.concept_utilities.make_id_from_slug(keyword, "keywords")

        kw_doc["skos:prefLabel"] = keyword
        kw_doc["@id"] = this_id
        #if len(m) == 0:
        kw_doc["chronos:toSearch"].append(label)

        if self.db.base.find_one({"@id": this_id}) is None:
            pprint(kw_doc)
            id_ = self.db.base.insert(kw_doc)
            this_doc = self.db.base.find_one({"_id": id_})
            this_scheme = self.db.base.find_one({"@id": "_:subj" + self.code})
            self.append_link_to_mongodoc(this_doc, "skos:inScheme", this_scheme, "base")
            self.append_link_to_mongodoc(this_doc, "skos:exactMatch", subject_top_doc, "base")

        return None
