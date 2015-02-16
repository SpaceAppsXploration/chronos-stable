from bs4 import BeautifulSoup, NavigableString
from selenium import webdriver

#import json, io

import requests

#Converted to Python3.3

from selenium.common.exceptions import WebDriverException
from pprint import pprint


class WrongAgencyName(Exception):
    """
    Custom exception
    """
    pass


def clean_string(string):
    return string.replace('\\n', '').replace('\\t', '').strip()


def generate_nasa_url(keyword):
    """
    Generate NASA's search url from a keyword
    :param keyword: the keyword to use in order to create the url
    :type keyword: string
    :return: url generated
    :rtype: string
    """
    return "http://nasasearch.nasa.gov/search?affiliate=nasa&query=" + keyword.replace(" ", "+") + "&commit=Search"


def generate_jaxa_url(keyword):
    """
    Generate JAXA's search url from a keyword
    :param keyword: the keyword to use in order to create the url
    :type keyword: string
    :return: url generated
    :rtype: string
    """
    return "http://global.jaxa.jp/search.html?&q=" + keyword.replace(" ", "+") + "&sa=Search&siteurl=global.jaxa.jp"


def generate_esa_url(keyword):
    """
    Generate ESA's search url from a keyword
    :param keyword: the keyword to use in order to create the url
    :type keyword: string
    :return: url generated
    :rtype: string
    """
    return "http://www.esa.int/esasearch?q=" + keyword.replace(" ", "+")


def retrieve(url):
    """
    Retrieve the HTML page from an url
    :param url: the url to use in order to retrieve a page
    :type url: string
    :return: complete HTML page
    :rtype: string
    """
    print("retrieve(url)" + url)
    return requests.get(url).text


def retrieve_webdriver(url):
    """
    Retrieve the HTML page from an url with webdriver (used for dynamic page)
    :param url: the url to use in order to retrieve a page
    :type url: string
    :return: complete HTML page
    :rtype: string
    """
    print(url)

    try:
        driver = webdriver.PhantomJS()  # need to have PhantomJS installed on the system, alternative use Firefox()
    except WebDriverException:
        return None

    driver.get(url)
    page = driver.page_source
    driver.close()

    return page


def store_to_cache_collection(key, keyword, html, agency, db):
    """
    Store in a MongoDB instance ("crawling" collection) a document about a webpage
    :param key: full keyword, with space and parenthesis
    :param keyword: slug of the keyword (quote_plus)
    :param html: html node (bs4) of the results' page
    :param agency: string name of the agency which the page is from
    :param db: MongoDB database
    :return: None
    """
    def parse_nasa_page(html):
        """
        This function parses the NASA's HTML page
        :param html: the HTML page to parse
        :type html: string
        :return: a list of all objects parsed
        :rtype: list
        """
        soup = BeautifulSoup(html)

        keys = ["title", "link", "abstract"]

        data = []

        results = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['searchresult'])

        try:
            for result in results:
                titles = []
                links = []
                abstracts = []

                elements = []

                link = result.find("a")
                titles.append(link.text)
                links.append(link['href'])

                i = 0
                for abstract in result.find_all("h3"):
                    if i % 2 != 0:
                        abstracts.append(abstract.text)
                    i += 1

                for i in range(0, len(titles)):
                        elements.append([titles[i], links[i], abstracts[i]])

                #for element in elements:
                    #data.append(dict(zip(keys, element)))
                data = elements

        except AttributeError:
            print("No results")

        return data

    def parse_jaxa_page(html):
        """
        This function parses the JAXA's HTML page
        :param html: the HTML page to parse
        :type html: string
        :return: a list of all objects parsed
        :rtype: list
        """
        try:
            soup = BeautifulSoup(html)
        except:
            return None

        #keys = ["title", "link", "abstract"]
        titles = []
        links = []
        abstracts = []

        elements = []

        data = []

        j = 0
        for link in soup.find_all("a", class_="gs-title"):
            j += 1

            if j % 2 == 0 and link.has_attr("href"):
                titles.append(link.text)
                links.append(link['href'])

        for div in soup.find_all("div", class_="gs-bidi-start-align gs-snippet"):
            abstracts.append(" ".join(div.text.split()))

        for i in range(0, len(titles)):
            elements.append([titles[i], links[i], abstracts[i]])

        #for element in elements:
            #data.append(dict(zip(keys, element)))

        data = elements

        return data

    def parse_esa_page(html):
        """
        This function parses the ESA's HTML page
        :param html: the HTML page to parse
        :type html: string
        :return: a list of all objects parsed
        :rtype: list
        """
        soup = BeautifulSoup(html)

        elements = []

        results = soup.find("div", class_="sr")
        #print(results.find_all("p"))

        try:
            """for link in results.find_all("a"):
                titles.append(link.text)
                links.append(link["href"])
                link.extract()"""
            for abstract in results.find_all("p"):
                elm = []
                if len(str(abstract.text.strip())) == 0:
                    print("abstract is VOID")
                    ### normal link
                    # navigate the node above <h4> and get the pdf link and title
                    # abstract is in <p>
                    h4 = abstract.fetchPreviousSiblings()[0]
                    for tag in h4:
                        if tag.name == 'a':
                            elm.append(clean_string(tag.text))
                            if tag.get('href')[0] == '/':
                                l = 'http://www.esa.int'+tag.get('href')
                            else:
                                l = tag.get('href')
                            elm.append(l)

                    #div = abstract.fetchNextSiblings()[0].fetchNextSiblings()
                    #print("next SIBLING: " + str(div))
                    elm.append(None)

                else:
                    ### pdf link and title
                    # abstract is in <div class=image> content
                    print("abstract is NOT VOID")
                    h4 = abstract.fetchPreviousSiblings()[0]
                    for tag in h4:
                        if tag.name == 'a':
                            elm.append(clean_string(tag.text))
                            if tag.get('href')[0] == '/':
                                l = 'http://www.esa.int'+tag.get('href')
                            else:
                                l = tag.get('href')
                            elm.append(l)

                    elm.append(clean_string(abstract.text))

                elements.append(elm)

            return elements

        except Exception as e:
            print("No results" + ", exception: " + str(e))

        return elements

    def __get_abstracts_between_img(source):
        abstracts = []
        starts = []

        pieces = source.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['img'])

        for piece in pieces:
            start = piece.nextSibling
            starts.append(start)

        i = 1
        for piece in pieces:
            abstract = []
            if i < len(starts):
                while (piece.nextSibling) != starts[i]:
                    text = ((piece.nextSibling).string).replace("\n", "").replace("\t", "").replace("  ", " ").strip()
                    if text != "None":
                        abstract.append(text)
                    piece = piece.nextSibling
                i += 1
            abstracts.append(" ".join(abstract).strip())

        return abstracts

    from base64 import b64encode
    collection = db['crawling']

    if agency == "NASA":
        parsed = parse_nasa_page(html)
    elif agency == "ESA":
        parsed = parse_esa_page(html)
    elif agency == "JAXA":
        parsed = parse_jaxa_page(html)
    else:
        raise WrongAgencyName

    if parsed is None:
        return

    for element in parsed:
        try:
            to_hash = element[1].encode(encoding='utf-8')
        except IndexError:
            return None
        avoid = '_-'.encode(encoding='UTF-8')
        hashed = b64encode(to_hash, avoid).decode(encoding='utf-8')

        if collection.find_one({"hashed": hashed}) is None:
            collection.insert({
                "key": key,
                "hashed": hashed,
                "abstract": element[2],
                "title": element[0],
                "keyword": keyword,
                "url": element[1],
                "home": agency,
                "stored": False,  # document is in cache but not as a doc in "webpages" collection
                "complete": False  # complete text in the webpage has not been searched for keywords
            })
        return None

if __name__ == "__main__":
    print("This is a useful module, not a stand-alone script")
