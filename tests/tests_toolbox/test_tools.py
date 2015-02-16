__author__ = 'lorenzo'


from toolbox import tools
from pprint import pprint

### Found Error in DBpedia JSOND serialization for 'Sun'
#tools.retrieve_json('http://dbpedia.org/data/Sun.jsond')


import unittest


class Test(unittest.TestCase):
    """
    Class for testing the tools in the 'toolbox' package
    """
    # tests variables
    dbpedia_url = 'http://dbpedia.org/data/Spacecraft.jsond'
    dbpedia_url2 = 'http://dbpedia.org/data/Sun.jsond'
    dbpedia_sun = 'http://dbpedia.org/resource/Sun'
    title_slug = 'Spacecraft'

    def test_retrieve_json(self):
        """
        Tests the tools.retrieve_json() method against a DBpedia document
        :return:
        """
        result = tools.retrieve_json(self.dbpedia_url)  # retrieve the submitted test url
        print(result)

        pprint(result["http://dbpedia.org/resource/Spacecraft"]['http://purl.org/dc/terms/subject'])

        to_be_tested = result["http://dbpedia.org/resource/Spacecraft"]['http://purl.org/dc/terms/subject']
        test_value = [
            {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Category:Spacecraft"
            },
            {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Category:Astronautics"
            },
            {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Category:Pressure_vessels"
            }
        ]

        if to_be_tested == test_value:
            assert True
        else:
            assert False

    def test_retrieve_json2(self):
        """
        Tests the tools.retrieve_json() method against a DBpedia document
        :return:
        """
        result = tools.retrieve_json(self.dbpedia_url2)  # retrieve the submitted test url
        pprint(result)
        print(">>>>> ENCODING DONE properly")
        assert True

    def test_get_slug_from_jsond_url(self):
        """
        Tests a slug to url conversion
        :return:
        """
        result = tools.from_dbpedia_url_return_slug(self.dbpedia_url)

        if result == self.title_slug:
            assert True
        else:
            assert False

    def test_retrieve_from_sparql(self):

        found = None
        result = tools.retrieve_from_sparql(self.dbpedia_sun)

        for el in result['@graph']:
            if el['@id'] == 'http://dbpedia.org/resource/Sun':
                found = el['http://dbpedia.org/ontology/wikiPageExternalLink']

        if found:
            if 'http://www.suntrek.org/' in found:
                assert True
            else:
                assert False
        else:
            assert False

    def test_get_resource_url_from_jsond_url(self):
        print(tools.get_resource_url_from_jsond_url(self.dbpedia_url))

    def test_retrieve_umbel_res(self):
        res = tools.retrieve("http://umbel.org/umbel/rc/Meteoroid")
        pprint(res)


if __name__ == "__main__":
    t = Test()
    t.test_retrieve_from_sparql()
    t.test_get_resource_url_from_jsond_url()