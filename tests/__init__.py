# tests
# Testing for the Semantic Network Similarity application
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Mar 26 08:38:56 2015 -0400
#
# Copyright (C) 2015 District Data Labs
# For license information, see LICENSE.txt
#
# ID: __init__.py [] benjamin@bengfort.com $

"""
Testing for the Semantic Network Similarity application
"""

##########################################################################
## Imports
##########################################################################

import unittest

##########################################################################
## Initialization Tests
##########################################################################

EXPECTED_VERSION = "0.1"


class InitializationTests(unittest.TestCase):

    def sanity_test(self):
        """
        Assert the world is sane and 2+8=10
        """
        self.assertEqual(2 + 8, 10)

    def test_import(self):
        """
        Ensure that we can import semnet lib
        """
        try:
            import semnet
        except ImportError:
            self.fail("Could not import semnet library")

    def test_expected_version(self):
        """
        Ensure test version and library version match
        """
        import semnet
        self.assertEqual(semnet.__version__, EXPECTED_VERSION)
