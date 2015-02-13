__author__ = 'lorenzo'

from datastoreapi.wrapper import Wrapper

from toolbox import tools
from pymongo.errors import DuplicateKeyError, DocumentTooLarge
import toolbox.customErrors as customErrors


class DBpediaCache(Wrapper):
    """
    This class manages operations of storing/retrieving/fetching on the DBpediacache collection
    """
    def __init__(self, unittest=False):
        super().__init__(unittest=unittest)

    def get_or_retrieve_and_store(self, slug):
        """
        Checks the DBpediacache collection and return or retrieve and return a dictionary with the resource
        :rtype: dict()
        :param slug: the wikipedia title in the url
        :return: dictionary of the resource, a json-ld in case of a DBpedia resource
        """

        at_id = tools.make_pramantha_url_from_slug('dbpediadocs', slug)

        def __insert_cache_doc(c_id, ld):
            # insert cache
            try:
                cache = dict()
                cache['body'] = str(ld)
                cache['@id'] = c_id
            except Exception as e:
                print("URL " + str(c_id))
                raise Exception(e)

            try:
                self.return_connection().DBpediacache.insert(cache)
                print("DBPEDIA CACHE INSERTED <<<<<<<<<<<<<<<")
            except (DuplicateKeyError, DocumentTooLarge):
                return None

        doc = self.return_connection().DBpediacache.find_one({"@id": at_id})

        if doc is None:
            # retrieve and store
            try:
                json_ld = tools.retrieve_from_sparql(tools.make_resource_url_from_slug(slug))
            except (customErrors.CannotSPARQL, Exception) as e:
                raise e

            __insert_cache_doc(at_id, json_ld)

            return json_ld

        try:
            import ast
            return ast.literal_eval(doc["body"])
        except Exception:
            raise UnicodeEncodeError("ast cannot decode the cache body")


