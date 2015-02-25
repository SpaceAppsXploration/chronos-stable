__author__ = ['lorenzo@pramantha.net']


from datastoreapi.wrapper import Wrapper

from pprint import pprint

import unittest


class Test(unittest.TestCase):
    w = Wrapper()
    print(w.return_mongo())