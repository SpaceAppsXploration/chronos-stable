__author__ = 'lorenzo'

"""
Base Class to create an instance of type ChronosEvent
and store it into the MongoDB instance
"""

from base64 import b64encode
from bson.objectid import ObjectId

from datastoreapi.wrapper import *
from datastoreapi.datastoreErrors import DocumentExistNot
from objectsapi.basicDocs import BasicDoc

avoid = '_-'.encode(encoding='UTF-8')
exceptions = {"ARTEMIS": "THEMIS", "MAFL": "Astrobiology_Field_Laboratory", "Sputnik": "Sputnik_1",
              "Lunar Recon Orbiter": "Lunar_Reconnaissance_Orbiter", "Mariner 7": "Mariner_6_and_7",
              "Ranger 01": "Ranger_1", "Ranger 02": "Ranger_2", "Surveyor 03": "Surveyor_3",
              "Surveyor 01": "Surveyor_1", "Surveyor 02": "Surveyor_2", "Surveyor 04": "Surveyor_4",
              "Surveyor 05": "Surveyor_5", "Surveyor 06": "Surveyor_6", "Surveyor 07": "Surveyor_7",
              "Mariner 6": "Mariner_6_and_7", "KAGUYA": "SELenological and ENgineering Explorer KAGUYA \(SELENE\)"}


class CHRONOSEvent:
    def __init__(self, old_id, obj):
        self.connection = Wrapper()
        self.db = self.connection.return_mongo()
        self.js_obj = obj
        self.old_id = old_id

    def store_event(self):
        """
        Stores and event object taken from the old APIs
        :return:
        """
        first = self.js_obj[0]["mission"]
        name = first[0:first.find(' - ')]
        target = first[first.find(' - ')+3:].strip()
        print(name, target, self.old_id)

        mssn = self.db.base.find_one({"chronos:group": "missions", "chronos:oldId": self.old_id})
        if mssn is None:
            mssn = self.db.base.find_one({"chronos:group": "missions", "chronos:slug": name})
            if mssn is None:
                mssn = self.db.base.find_one({"chronos:group": "missions", "chronos:codename": name})
                if mssn is None:
                    mssn = self.db.base.find_one({"chronos:group": "missions", "skos:prefLabel": "\/"+name+"\/i"})
                    if mssn is None and name in exceptions.keys():
                        mssn = self.db.base.find_one({"chronos:group": "missions", "skos:prefLabel": exceptions[name]})
                        if mssn is None and name in exceptions.keys():
                            mssn = self.db.base.find_one({"chronos:group": "missions", "chronos:slug": exceptions[name]})
    
        for e in self.js_obj:
            hashed = b64encode(str(e["mission"]+str(e["id"])).encode(encoding='UTF-8'), avoid).decode(encoding='UTF-8')
            this_id = PRAMANTHA_URL % ("events", hashed)

            # basic event document
            event = BasicDoc.blank_event()
            event["@id"] = this_id
            event["chronos:eventdate"] = e["date"]
            event["chronos:eventType"] = e["detail_type"]
            event["chronos:oldId"] = e["id"]
            event["chronos:oldString"] = e["mission"]
            event["chronos:eventHeader"] = e["header"]
            event["chronos:eventImageLink"] = e["image_link"]

            content = e["body"]
            if content[:4] == 'http:':
                event["chronos:eventContent"] = {
                    "@type": "https://schema.org/URL",
                    "@value": content,
                }
            else:
                event["chronos:eventContent"] = {
                    "@type": "https://schema.org/Text",
                    "@value": content,
                }

            if not self.db.base.find_one({"@id": this_id}):
                id_ = self.db.base.insert(event)
                this_doc = self.db.base.find_one({"_id": ObjectId(id_)})
                if mssn is not None:
                    self.connection.append_link_to_mongodoc(this_doc, "chronos:relMission", mssn, "base")
                else:
                    raise DocumentExistNot("EVENTS API: This mission is not in the DB")