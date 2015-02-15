#
# This module contains all the documents' structure for each type of document to be stored
# ----------------------------------------------------------------------------------------
#
# Notes:
#    for dbpediadocs skos:altLabel is the wikipedia title of the term (i.e. "Clementine_(Spacecraft)")
#    for dbpediadocs skos:prefLabel is always 'None'
#
#    for targets chronos:slug is the wikipedia title of the term (i.e. "Clementine_(Spacecraft)")
#    for dbpediadocs skos:prefLabel is the full English name
#

__author__ = 'lorenzo'

from datastoreapi.wrapper import *


class BasicDoc(Wrapper):
    def __init__(self, unittest=False):
        super().__init__(unittest=unittest)

    def blank_dbpediadoc(self):
        """
        This the base doc for the DBPEDIADOCS group. They save locally the reference
        to a term that is in DBpedia/Wikipedia
        :return: a basic doc of kind "dbpediadoc"
        """
        return {
            "@id": None,
            "@type": self.PRAMANTHA_URL % ("ontology", "dbpediadoc"),
            "@language": "en",
            "schema:provider": [dict({
                "@value": "http://dbpedia.org/data/DBpedia.jsond",
                "@type": self.RDF_RESOURCE
            })],
            "chronos:group": "dbpediadocs",
            "chronos:dbpediaCategories": [],
            "chronos:relEvent": [],
            "chronos:relMission": [],
            "chronos:relTarget": [],
            "skos:exactMatch": [],                                   # link to a document among ontology documents that has the same semantic context
            "chronos:relatedMatch": [],                              # link semantically to another doc of dbpedia type
            "chronos:tagMeAbs": None,
            "dbpedia:abstract": None,
            "chronos:relKeyword": [],
            "skos:altLabel": None,                                   # for dbpediadocs altLabel is the wikipedia title of the term
            "skos:prefLabel": None,                                  # for dbpediadocs prefLabel is always 'None'
            "owl:sameAs": [
                {
                    "@value": None,                                  # slot [0] for dbpedia resource in jsond format
                    "@type": self.RDF_RESOURCE,
                    "rdfs:comment": "this link can be used as it is to retrieve in JSOND (ODATA) format"
                },
                {
                    "@value": None,                                  # slot [1] for XML resource,
                    "@type": self.RDF_RESOURCE,                       # see the tools. retrieve_from_sparql(url) method
                    "rdfs:comment": "this link supply an XML, but it can be used in a SPARQL \
                                     query to DBpedia to request a JSON-LD or do the request through ChronosAPIs' cache"
                }
            ]
        }

    def blank_mission(self):
        """
        This the base doc for the MISSIONS group. They save locally the data about a mission or a launch.
        it links to DBpedia term with the "owl:sameAs" property.
        :return: a basic doc of kind "mission"
        """
        return {
            "@id": None,                                             # 'subject' of the RDF triple: in this doc CHRONOS_URL % ("missions", <slug>)
            "skos:prefLabel": None,                                  # full name of mission: "Apollo 11"
            "@type": self.PRAMANTHA_URL % ("ontology", "mission"),      # type of the document, in this case chronos:mission
            "rdf:type": [],                                          # rdf types as found in wikipedia
            "chronos:slug": None,                                    # if mission in wikipedia, this is the wikipedia title. Else is None
            "chronos:missionEra": None,                              # string: present, apst, future, concept
            "chronos:group": "missions",                             # group it belongs in the database
            "chronos:oldId": None,                                   # id it had in the old db, for legacy purpose
            "chronos:payload": [],                                   # list of payloads (now strings, in future documents)
            "owl:sameAs": [],                                        # references to other URI with the same meaning
            "chronos:imageUrl": {                                    # url of an image of mission
                "@value": None,
                "@type": "https://schema.org/URL"
            },
            "schema:url": {                                          # url of the official mission page
                "@value": None,
                "@type": "https://schema.org/URL"
            },
            "chronos:relTarget": []                                     # bodies the mission visited

        }

    def blank_launch(self):
        """
        Launches are joined to missions in the MISSIONS group. They save locally the data about a mission or a launch.
        it links to DBpedia term with the "owl:sameAs" property.
        :return: a basic doc of kind "launch"
        """
        return {
            "@id": None,
            "skos:prefLabel": None,
            "@type": self.PRAMANTHA_URL % ("ontology", "launch"),
            "rdf:type": [],
            "chronos:year": None,
            "chronos:slug": None,
            "chronos:group": "missions",
            "chronos:payload": [],
            "skos:inScheme": {},
            "owl:sameAs": [],
            "chronos:imageUrl": {},
            "chronos:relTarget": []

        }

    def blank_target(self):
        """
        This the base doc for the TARGETS group. They save locally the data about a celestial body.
        it links to DBpedia term with the "owl:sameAs" property.
        :return: a basic doc for different celestial bodies' types
        """
        return {
            "@id": None,
            "@type": None,                                           # can be 'Satellite', 'Planet' from wikipwdia ontology
            "@language": "en",
            "owl:sameAs": [{
                "@value": None,
                "@type": self.RDF_RESOURCE,                           # OData resource .jsond
                "schema:provider": {
                    "@value": "http://dbpedia.org/resource/DBpedia",
                    "@type": self.RDF_RESOURCE
                    }
                },
                {
                    "@value": None,                                  # XML resource usable for sparql querying the json-ld
                    "@type": self.RDF_RESOURCE
                }
            ],
            "skos:prefLabel": None,                                  # name of the body. "targets" have NO altLabel!
            "chronos:slug": None,
            "chronos:group": "targets",
            "chronos:idFromDb": None,
            "chronos:imageUrl": {
                "@value": None,
                "@type": "https://schema.org/URL"
            },
            "chronos:abstract": {
                "@value": None,
                "@type": "https://schema.org/Text"
            },
            "chronos:curiosities": {
                "@value": None,
                "@type": "https://schema.org/Text"
            },
            "chronos:simRelated": {
                "@value": None,
                "@type": "https://schema.org/Text"
            },
            "chronos:useInSim": {
                "@value": None,
                "@type": self.RDF_PLAIN_LITERAL
            },
        }

    def blank_division_collection(self):
        return {
            "@language": "en",
            "@type": self.SKOS_COLLECTION,
            "schema:provider": {},
            "@id": "_:allDivisions",
            "skos:prefLabel": "divisions collection",
            "skos:scopeNote": {
                "@value": "Collection of Divisions Concepts",
                "@type": self.RDF_PLAIN_LITERAL
            },
            "skos:memberList": []
        }

    def blank_division(self):
        return {
            "@language": "en",
            "@type": self.SKOS_CONCEPT,
            "schema:provider": {},
            "@id": None,
            "skos:prefLabel": None,
            "chronos:code": None,
            "chronos:group": "divisions",
            "skos:scopeNote": [dict({
                "@value": None,
                "@type": self.RDF_PLAIN_LITERAL
            })],
            "owl:sameAs": [],
            "skos:narrower": [],
            "skos:broader": {}
        }

    def blank_subject_collection(self):
        return {
            "@language": "en",
            "@type": self.SKOS_COLLECTION,
            "schema:provider": {},
            "@id": "_:allSubj",
            "skos:prefLabel": "subjects collection",
            "skos:scopeNote": {
                "@value": "Collection of Subjects TopConcepts from subjects' schemes",
                "@type": self.RDF_PLAIN_LITERAL
            }, "skos:memberList": []
        }

    def blank_subject_scheme(self):
        return {
            "@language": "en",
            "@type": self.SKOS_SCHEME,
            "schema:provider": {},
            "@id": None,
            "skos:prefLabel": None,
            "chronos:code": None,
            "chronos:group": "schemes",
            "skos:scopeNote": {
                "@value": "subject's scheme where keywords are aggregated",
                "@type": self.RDF_PLAIN_LITERAL
            },
            "skos:hasTopConcept": {}
        }

    def blank_subject_as_top_concept(self):
        return {
            "@language": "en",
            "@type": self.SKOS_CONCEPT,
            "schema:provider": {},
            "@id": None,
            "skos:prefLabel": None,
            "chronos:code": None,
            "chronos:group": "subjects",
            "skos:scopeNote": {
                "@value": "",
                "@type": self.RDF_PLAIN_LITERAL
            },
            "skos:topConceptOf": {},
            "owl:sameAs": [],  # link to DBpedia term
            "skos:broader": {}  # link to division
        }

    def blank_keyword(self):
        """
        This the base doc for the KEYWORDS group. They save locally the data about NASA's SKOS-XML keyword.
        dbpediadocs and missions refer to them with the "chronos:relKeyword" property
        :return: a basic doc of kind "skos:Concept" that holds a NASA-STI keyword
        """
        return {
            "@language": "en",
            "@type": self.PRAMANTHA_URL % ("ontology", "keyword"),
            "schema:provider": {},
            "chronos:group": "keywords",
            "skos:prefLabel": None,  # full keyword with parenthesis and commas
            "skos:altLabel": None,   # quote_plus(prefLabel)
            "@id": None,
            "chronos:toSearch": [],
            "skos:inScheme": {},  # in scheme with same subject
            "skos:exactMatch": [],  # semantical match with its subject
            "skos:scopeNote": []
        }

    def blank_webpage(self):
        """
        This the base doc for the URLS group. They save locally the data about a crawled url.
        It links to keywords with the "schema:about" property, and to missions with the "chronos:relMission" property.
        :return:
        """
        return {
            "@id": None,
            "chronos:base64": None,
            "@type": self.PRAMANTHA_URL % ("ontology", "webpage"),
            "schema:url": {
                "@value": None,
                "@type": "https://schema.org/URL"
            },
            "chronos:group": "urls",
            "schema:inLanguage": "English",
            "@language": "en",
            "schema:publisher": {
                "@value": None,
                "@type": self.RDF_RESOURCE
            },
            "schema:provider": {
                "@value": None,
                "@type": self.RDF_RESOURCE
            },
            "schema:headline": {
                "@value": None,
                "@type": "http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral"
            },
            "schema:description": {
                "@value": None,
                "@type": "http://schema.org/Text"
            },
            "schema:about": [],  # link to keywords instances
            "chronos:relMission": [],  # link to a mission instance
            "chronos:relTarget": []  # link to a target instance

        }

    def blank_event(self):
        return {
            "@id": None,
            "@type": self.PRAMANTHA_URL % ("ontology", "event"),
            "chronos:group": "events",
            "chronos:eventContent": None,
            "chronos:eventdate": None,
            "chronos:eventType": None,
            "chronos:oldId": None,
            "chronos:oldString": None,
            "chronos:eventHeader": None,
            "chronos:eventImageLink": None,
            "chronos:relMission": None
        }