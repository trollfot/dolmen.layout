"""Test setup for megrok.chameleon.
"""
import doctest
import unittest
import dolmen.layout

FLAGS = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)


def test_suite():
    """Get a testsuite of all doctests.
    """
    suite = unittest.TestSuite()
    for name in ['layout.txt']:
        test = doctest.DocFileSuite(
            name,
            package=dolmen.layout.tests,
            globs=dict(__name__="dolmen.layout.tests"),
            optionflags=FLAGS,
            )
        suite.addTest(test)
    return suite
