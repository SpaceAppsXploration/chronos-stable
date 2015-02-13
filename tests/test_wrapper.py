__author__ = 'lorenzo'


from datastoreapi.wrapper import Wrapper

from pprint import pprint

import unittest


class Test(unittest.TestCase):
    w = Wrapper(unittest=True)
    print(w.return_connection())
    print(w.return_client())