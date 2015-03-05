__author__ = ['lorenzo@pramantha.net']

from html.parser import HTMLParser

from toolbox.pediacache import DBpediaCache
from toolbox.tools import from_dbpedia_url_return_slug, retrieve_from_sparql
import toolbox.customErrors as customErrors
from tagmeapi.tagMeService import TagMeService, BadRequest
from tagmeapi.tagMeOperation import TagMeOperation


class JsonLD(DBpediaCache):
    """
    This class is for traversing JSON-LDs and finding/fetching values from their keys
    """
    def __init__(self):
        super().__init__()

    def get_body_text_from_dbpedia_jsonld(self, url):
        """
        From the url returns the text in the term's body traversing the JSON-LD
        :param url: a /data/*.jsond url
        :returnType: bytes
        :return: the text in the document body or None if there is no abstract
        """

        title = from_dbpedia_url_return_slug(url)          # return the title from the url

        try:
            json_ld = self.get_or_retrieve_and_store(title)     # look for the title in DBpediacache or retrieve
        except (customErrors.CannotSPARQL, ConnectionError, UnicodeEncodeError):
            return None

        text = None
        if "@graph" in json_ld.keys():
            for el in json_ld["@graph"]:
                for key, value in el.items():
                    if key == "http://dbpedia.org/ontology/abstract":
                        for l in value:
                            if l["@language"] == "en":
                                h = HTMLParser()
                                text = h.unescape(l["@value"])
                                text = text.encode('utf-8')
                                break

        if text:
            return text

        try:
            found = TagMeService.retrieve_taggings(title)
        except BadRequest:
            print(BadRequest('retrieve_taggings in get_body_text_from_dbpedia_jsonld()'))
            return None

        scopes = TagMeOperation.return_gen_lowered()
        if found["annotations"]:
            for f in found["annotations"]:
                if "rho" in f.keys() and 0.32 < float(f["rho"]) < 0.72 and any([True for c in f["dbpedia_categories"] for w in c.split() if w.lower() in scopes]):
                    print(f["rho"])
                    if 'abstract' in f:
                        return f['abstract']

        print(Exception('Cannot find dbpedia body with get_body_text_from_dbpedia_jsonld()'))
        return None
