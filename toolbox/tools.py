"""
This module contains general tools for various basic operations performed by different packages in the repository.
Tests for all methods in tests/test_toolbox.py
"""

__author__ = 'lorenzo'

import requests
from urllib.parse import quote
from bs4 import BeautifulSoup
import simplejson as json
import html.parser
from codecs import raw_unicode_escape_decode

# resource repositories links
DBPEDIA_URL = "http://dbpedia.org/data/%s.jsond"        # string-substitute with wikipage title (slug)
DBPEDIA_RESOURCE = "http://dbpedia.org/resource/%s"     # string-substitute with wikipage title (slug)
PRAMANTHA_URL = "http://pramantha.eu/%s/%s"             # domain for local resources (chronos:group, slug)


def retrieve(url):
    """
    Utility: URL's body fetching
    :rtype : basestring
    :param url: URL to fetch
    :return: body of the url in unicode with parsed HTML entities
    """
    try:
        response = requests.get(url)
    except requests.RequestException as e:
        raise ConnectionError("retrieve() encountered and error: " + str(e))

    h = html.parser.HTMLParser()
    try:
        doc = h.unescape(response.text)
        doc = str(doc.encode('utf-8'))
    except (TypeError, UnicodeEncodeError) as e:
        raise Exception("retrieve() could not decode page content: " + str(e))
    return doc


def retrieve_json(url, method='GET', data=None):
    """
    Utility: URL's body fetching
    :rtype : dict()
    :param url: URL to fetch
    :param method: the method to use for the request
    :param data: if method is POST, pass also some data for request's body
    :return: dictionary from the response's body
    """
    print(url)
    if method == 'GET':
        try:
            # avoid HTML escaping problems using bs4
            return json.loads(str(BeautifulSoup(requests.get(url).text)))
        except json.JSONDecodeError:
            # avoid unicode escaping problems (double backslash encoding)
            h = html.parser.HTMLParser()
            text = h.unescape(requests.get(url).text)
            return json.loads(raw_unicode_escape_decode(text)[0])
    elif method == 'POST':
        if data is not None:
            try:
                return json.loads(str(BeautifulSoup(requests.post(url, data=data).text)))  # using bs4 to treat html entities
            except json.JSONDecodeError:
                h = html.parser.HTMLParser()
                text = h.unescape(requests.post(url, data=data).text)
                return json.loads(raw_unicode_escape_decode(text)[0])  # using bs4 to treat html entities
        else:
            raise Exception('retrieve_json(): data for POST cannot be None')
    else:
        raise Exception('retrieve_json(): Wrong Method')


def retrieve_from_sparql(url):
    """
    Utility: JSON-LD fetching from DBpedia SPARQL endpoint
    :rtype : dict()
    :param url: wikipedia url of the resource (/resource/*)
    :return: dictionary from the response's body
    """

    h = html.parser.HTMLParser()
    url = h.unescape(url)                   # treat HTML entities
    url = quote(url.encode('utf8'))         # parse url parameters
    sparql = "http://dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.org&query=DESCRIBE+%3C" + \
        url + \
        "%3E&output=application%2Fld%2Bjson"
    print(sparql)
    try:
        req = h.unescape(requests.get(sparql).text)
    except Exception:
        raise ConnectionError('retrieve_from_sparql(): DBPEDIA is not reachable')

    try:
        return json.loads(raw_unicode_escape_decode(req)[0])
    except json.JSONDecodeError:
        raise Exception('retrieve_from_sparql(): JSON response badly encoded or DBpedia SPQRL endpoint is down')


def from_dbpedia_url_return_slug(url):
    """
    Returns the DBpedia slug from the XML or jsond url
    :rtype: str()
    :param url: a dbpedia url
    :return: a slug
    """

    def __get_slug_from_jsond_url(jsond_url):
        """
        From a DBpedia.jsond url returns the dbpedia slug of the term
        """
        pos = jsond_url.rfind('/data/')
        if pos == -1:
            raise Exception("get_slug_from_jsond_url(): Wrong argument, it has to be a /data/*.jsond kind")

        slug = jsond_url[pos + 6:-6]
        return slug

    def __get_slug_from_resource_url(res_url):
        """
        From a DBpedia (page or resource) url returns the dbpedia slug of the term
        """
        pos0 = res_url.rfind('/resource/')
        pos1 = res_url.rfind('/page/')

        if pos0 != -1:
            slug = res_url[pos0 + 10:]
            return slug
        elif pos1 != -1:
            slug = res_url[pos1 + 6:]
            return slug

        raise Exception("get_slug_from_jsond_url(): Wrong argument, it has to be a /resource/* or a /page/* kind")

    if url[-5:] == "jsond":
        # if Odata makes resource url and then cache @id
        title = __get_slug_from_jsond_url(url)
    elif url.find("/resource/") or url.find("/page/"):
        # if resource url makes cache @id url
        title = __get_slug_from_resource_url(url)

    return title


def get_slug_from_pramantha_dbpediadocs(url):
    """
    From a Chronos @id returns the dbpedia slug of the term
    """
    pos = url.find('/dbpediadocs/')
    if pos == -1:
        raise Exception("get_slug_from_pramantha_url: Wrong argument, it has to be a pramantha.eu/dbpediadocs/* kind")

    slug = url[pos + 13:]
    return slug


def make_pramantha_url_from_slug(kind, trm):
    """
    Turns a term into pramantha.eu/<kind>/<trm> url
    :param kind: the chronos:group property of the document
    :param trm: a title or slug
    :return: a DBpedia's resource url
    """
    return PRAMANTHA_URL % (kind, trm)


def make_resource_url_from_slug(trm):
    """
    Turns a Wikipedia title/slug into a DBpedia url
    :param trm:
    :return: a DBpedia's resource url
    """
    return DBPEDIA_RESOURCE % trm


def make_jsond_url_from_slug(trm):
    """
    Turns a Wikipedia title/slug into a DBpedia url
    :param trm:
    :return: a DBpedia's resource url
    """
    return DBPEDIA_URL % trm

def get_resource_url_from_jsond_url(url):
    """
    Turns a data/*.jsond (OData) url into a resource/* (XML) url that can be used in sparwl queries
    :param url: a .jsond url
    :return: str
    """
    url = url[:-6].replace("/data/", "/resource/")
    return url