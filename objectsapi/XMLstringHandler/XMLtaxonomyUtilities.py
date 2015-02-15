from pprint import pprint

from datastoreapi.datastoreErrors import DocumentExists, DocumentExistNot
from datastoreapi.wrapper import *


class SKOSconcepts():
    """
    Collection of methods to process and store the JPL's NASA-STI XML-SKOS file

    :method find_or_create_scheme: look for a skos:ConceptScheme, if not found it creates the scheme
    :method find_or_create_collection: look for a skos:Collection, if not found it creates the collection
    :method make_id_from_concept: return a slug and an @id from a bs4 concept
    :method make_id_from_slug: return a slug and an @id from a string
    :method from_concept_to_document: return a cloud document from a BS4 XML tag
    :method store_broader: check and store a skos:broader link into a skos:Concept document in the cloud
    :method store_narrower: check and store a skos:narrower link into a skos:Concept document in the cloud
    """
    def __init__(self):
        self.connection = Wrapper()
        self.db = self.connection.return_connection()
        self.provider = self.db.base.find_one({
            "@id": PRAMANTHA_URL % ("organization", "NASA+Sientific+and+Technical+Information+Program")
        })

    def find_or_create_scheme(self, at_id, scheme):
        check = self.db.base.find_one({"@id": at_id})
        if check is None:
            pprint("Store" + str(scheme))
            scheme["@id"] = at_id
            scheme["skos:prefLabel"] = "reference scheme for subject number " + at_id
            self.db.base.insert(scheme)
            new_scheme = self.db.base.find_one({"@id": at_id})
            try:
                self.append_link_to_mongodoc(new_scheme, "schema:provider", self.provider, "base")
            except DocumentExists:
                pass
            return new_scheme

        return check

    def find_or_create_collection(self, at_id, collection):
        check = self.db.base.find_one({"@id": at_id})
        if check is None:
            pprint("Store" + str(collection))
            self.db.base.insert(collection)
            new_coll = self.db.base.find_one({"@id": at_id})
            try:
                self.append_link_to_mongodoc(new_coll, "schema:provider", self.provider, "base")
            except DocumentExists:
                pass

            return new_coll

        return check

    def make_id_from_concept(self, concept, category):
        """
        Create label and full URL from
        :param concept: a Concept's BS4 object
        :return: (pref_label, this_id)
        """
        pref_label = concept.find("skos:preflabel").string
        label = pref_label.lower()
        url_label = label.replace(' ', '+').replace(',', '')
        this_id = self.PRAMANTHA_URL % (category, url_label)

        return pref_label, this_id

    def make_id_from_slug(self, keyword, category):
        """
        Create label and full URL from
        :param keyword: a keyword string
        :return: (label, this_id)
        """
        label = keyword.lower()
        label = label.replace(' ', '+').replace(',', '')
        this_id = self.PRAMANTHA_URL % (category, label)

        return label, this_id

    def from_concept_to_document(self, concept):
        """
        Retrieve a database object from a concept
        :param concept: a Concept's BS4 object
        :return:
        """
        check = self.db.base.find_one({"skos:prefLabel": concept.find("skos:preflabel").string})
        if check is not None:
            return check

        raise DocumentExistNot

    def store_broader(self, document, concept):
        try:
            document = self.from_concept_to_document(document)
            concept = self.from_concept_to_document(concept)
        except DocumentExistNot:
            return

        try:
            return self.append_link_to_mongodoc(document, "skos:broader", concept, "base")
        except DocumentExists:
            return None

    def store_narrower(self, document, concept):
        try:
            document = self.from_concept_to_document(document)
            concept = self.from_concept_to_document(concept)
        except DocumentExistNot:
            return

        try:
            return self.append_link_to_mongodoc(document, "skos:narrower", concept, "base")
        except DocumentExists:
            return None
