__author__ = 'lorenzo'

from pprint import pprint

from bs4 import BeautifulSoup
from datastoreapi import datastoreErrors

from main.mongod import get_connection
from toolbox import tools
from datastoreapi.buildDatastore import Build


class XMLskos(Build):
    """
    Utilities to handle the operations on JPL's SKOS-XML document
    -------------------------------------------------------------
    :method find_concept: find a given Subject by looping therdf:aabout property in the skos:Concept tag
    :method return_raw_doc: return the raw bs4 document object
    :method store_STI_document: select and format a BS4 XML tag <skos:Concept> and properly store it
    """

    def __init__(self, xml_string):
        super().__init__(mongod=get_connection())
        self.xml_string = xml_string
        self.provider = self.mongod.base.find_one({
            "@id": self.PRAMANTHA_URL % ("organization", "NASA+Sientific+and+Technical+Information+Program")
        })

    def find_concept(self, code):
        for cc in self.return_soup().find_all("skos:concept"):
            if cc["rdf:about"] == "subj:"+code:
                return cc

    def return_soup(self):
        return BeautifulSoup(self.xml_string)

    def add_root(self):
        # the first concept to be inserted is the STI itself
        nasa_sti = self.return_soup().find("skos:concept", {"rdf:about": 'subj:100'})
        sti_code = nasa_sti.find("nt2:code").string
        self.store_sti_document(nasa_sti, sti_code)

    def store_sti_document(self, concept, code):
        """
        Define a different behaviour depending on concept's code. Store the concept with the right document format.
        :param concept: bs4 object from the DOM
        :param code: code of the concept taken from XML property
        :return: Mongo doc "_id" of the resource
        """
        from datastoreapi.XMLstringHandler.STIdivisions import STIdivision
        from datastoreapi.XMLstringHandler.STIsubjectsAndKeywords import STIsubject

        int_code = int(code)
        if int_code == 100:
            # concept is the STI itself
            doc_id = self.PRAMANTHA_URL % ("organization", "NASA+Sientific+and+Technical+Information+Program")
            doc = {
                "@language": "en",
                "@type": self.SKOS_CONCEPT,
                "chronos:group": "STI",
                "chronos:code": code,
                "schema:provider": {"@type": self.RDF_RESOURCE, "@value": doc_id},
                "skos:prefLabel": concept.find("skos:preflabel").string,
                "skos:scopeNote": concept.find("skos:scopenote").string,
                "@id": doc_id,
                "skos:narrower": [],
                "owl:sameAs": [
                    {
                        "@type": self.RDF_RESOURCE, 
                        "@value": self.STI_LD_LINK
                    },
                    {
                        "@type": self.RDF_RESOURCE, 
                        "@value": tools.get_resource_url_from_jsond_url(self.STI_LD_LINK)
                    }
                ],
                "schema:url": {"@type": "http://schema.org/URL", "@value": "http://www.sti.nasa.gov/"}
            }
            check = self.mongod.base.find_one({"@id": doc["@id"]})
            if check is None:
                return self.mongod.base.insert(doc)
            return check
        elif int_code == 3056:
            # "General" category
            doc_id = self.PRAMANTHA_URL % ("general", "General")
            doc = {
                "@language": "en",
                "@type": self.SKOS_CONCEPT,
                "chronos:group": "STI",
                "chronos:code": code,
                "schema:provider": {},
                "skos:prefLabel": concept.find("skos:preflabel").string,
                "skos:scopeNote": concept.find("skos:scopenote").string,
                "@id": doc_id,
                "skos:narrower": [],
                "skos:broader": {}
            }

            check = self.mongod.base.find_one({"@id": doc["@id"]})
            if check is None:
                return self.mongod.base.insert(doc)
            return check["_id"]
        elif int_code > 1000:
            # concept is a Division
            new = STIdivision(obj=concept)
            try:
                new.store_division_concept()
            except datastoreErrors.DocumentExists:
                return
        elif int_code < 100:
            # concept is a Subject
            new = STIsubject(obj=concept)
            top_concept = new.store_top_concept()
            for kw in concept.find_all('skos:altlabel'):
                #print(kw)
                new.add_keyword(kw.string, top_concept)
            return None
        elif 100 < int_code < 1000:
            # concept is a Area
            pref_label = concept.find("skos:preflabel").string
            pprint("AREA >>>>>>>>>>>>>>:" + str(pref_label))
            doc = {
                "@language": "en",
                "@type": self.SKOS_CONCEPT,
                "chronos:group": "areas",
                "chronos:code": code,
                "schema:provider": {},
                "skos:prefLabel": pref_label,
                "skos:broader": {},
                "skos:narrower": [],
                "skos:scopeNote": concept.find("skos:scopenote").string,
                "@id": self.PRAMANTHA_URL % ("areas", pref_label.replace(' ', '+').lower()),
                "owl:sameAs": {}
            }

            check = self.mongod.base.find_one({"@id": doc["@id"]})
            if check is None:
                return self.mongod.base.insert(doc)
            return check["_id"]

    def link_sti_document(self, obj):
        """
        Links all the keywords in a Divisions>Subjects>Keywords hierarchy
        :param obj:
        :return:
        """
        from datastoreapi.XMLstringHandler.XMLtaxonomyUtilities import SKOSconcepts

        concept_utilities = SKOSconcepts()
        pref_label = obj.find("skos:preflabel").string

        doc = self.mongod.base.find_one({"skos:prefLabel": pref_label})

        if doc is None:
            id_ = self.store_sti_document(obj, obj.find("nt2:code").string)
            doc = self.mongod.base.find_one({"_id": id_})

        self.append_link_to_mongodoc(doc, "schema:provider", self.provider, "base")

        if obj.find_all('skos:broader') is not None:
            for broad in obj.find_all('skos:broader'):
                c = [s for s in broad["rdf:resource"] if s.isdigit()]
                code = str.join('', c)
                cc = self.find_concept(code)
                print("broad >>>> " + code)
                concept_utilities.store_broader(obj, cc)

        if obj.find_all('skos:narrower') is not None:
            for narrow in obj.find_all('skos:narrower'):
                c = [s for s in narrow["rdf:resource"] if s.isdigit()]
                code = str.join('', c)
                print("narrow >>>> " + code)
                if code == '225' or code == '226':
                    continue
                cc = self.find_concept(code)
                concept_utilities.store_narrower(obj, cc)

    def check_concept_complete(self):
        # check if all concept has a 'provider'
        for obj in enumerate(self.mongod.base.find({"chronos:group": "keywords"})):
            doc = self.mongod.base.find_one({"_id": obj[1]["_id"]})
            self.append_link_to_mongodoc(doc, "schema:provider", self.provider, "base")


if __name__ == "__main__":
    print("This is a useful module, not a stand-alone script")