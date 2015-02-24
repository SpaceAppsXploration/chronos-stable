__author__ = ['lorenzo@pramantha.net']




"""
assertDictEqual, assertEqual, assertTrue, assertFalse, assertGreater,
assertGreaterEqual, assertIn, assertIs, assertIsIntance, assertIsNone, assertIsNot,
assertIsNotNone, assertItemsEqual, assertLess, assertLessEqual, assertListEqual,
assertMultiLineEqual, assertNotAlmostEqual, assertNotEqual, assertTupleEqual,
assertRaises, assertRaisesRegexp, assertRegexpMatches
"""

##### Examples

import unittest

try:
    import mylib
except ImportError:
    mylib = None


class TestSkipped(unittest.TestCase):
    @unittest.skip("Do not run this")
    def test_fail(self):
        self.fail("This should not be run")

    @unittest.skipIf(mylib is None, "mylib is not available")
    def test_mylib(self):
        self.assertEqual(mylib.foobar(), 42)

    def test_skip_at_runtime(self):
        if True:
            self.skipTest("Finally I don't want to run it")


class TestMock(unittest.TestCase):
    def test_1(self):
        try:
            from unittest import mock
        except ImportError:
            try:
                import mock

                assert True
            except ImportError:
                assert False

        assert True



"""Mock Patching
--------------
"""
import unittest
import mock
import requests

class WhereIsPythonError(Exception):
    pass

def is_python_still_a_programming_language():
    try:
        r = requests.get("http://python.org")
    except IOError:
        pass
    else:
        if r.status_code == 200:
            return 'Python is a programming language' in r.content

    raise WhereIsPythonError("Something bad happened")

def get_fake_get(status_code, content):
    m = mock.Mock()
    m.status_code = status_code
    m.content = content

    def fake_get(url):
        return m

    return fake_get

def raise_get(url):
    raise IOError("Unable to fetch url %s" % url)

class TestPython(unittest.TestCase):
    @mock.patch('requests.get', get_fake_get(
                        200, 'Python is a programming language for sure'))
    def test_python_is(self):
        self.assertTrue(is_python_still_a_programming_language())
    @mock.patch('requests.get', get_fake_get(
                        200, 'Python is no more a programming language'))
    def test_python_is_not(self):
        self.assertFalse(is_python_still_a_programming_language())
    @mock.patch('requests.get', get_fake_get(
                                                404, 'Whatever'))
    def test_bad_status_code(self):
        self.assertRaises(WhereIsPythonError,
                            is_python_still_a_programming_language)
    @mock.patch('requests.get', raise_get)
    def test_ioerror(self):
        self.assertRaises(WhereIsPythonError,
                        is_python_still_a_programming_language)

