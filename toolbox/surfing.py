__author__ = 'lorenzo'

from html.parser import HTMLParser

from datastoreapi.wrapper import Wrapper
from toolbox.pediacache import DBpediaCache
from toolbox.tools import from_dbpedia_url_return_slug
import toolbox.customErrors as customErrors


class JsonLD(DBpediaCache, Wrapper):
    """
    This class is for traversing JSON-LDs and finding/fetching values from their keys
    """
    def __init__(self, unittest=False):
        super().__init__(unittest=unittest)

    def get_body_text_from_dbpedia_json(self, url):
        """
        From the url returns the text in the term's body
        :param url: a /data/*.jsond url
        :returnType: bytes
        :return: the text in the document body or None if there is no abstract
        """

        title = from_dbpedia_url_return_slug(url)          # return the title from the url

        try:
            json_ld = self.get_or_retrieve_and_store(title)     # look for the title in DBpediacache or retrieve
        except customErrors.CannotSPARQL:
            return None

        text = None
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

        print(Exception('Cannot find dbpedia body with get_body_text_from_dbpedia_json()'))
        return None
