# tests.search_tests.base_tests
# Testing the Base API class
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Tue May 05 19:28:16 2015 -0400
#
# Copyright (C) 2015 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: base_tests.py [] benjamin@bengfort.com $

"""
Testing the Base API class
"""

##########################################################################
## Imports
##########################################################################

import os
import unittest

from semnet.search.base import BaseSearch

BASE_PATH = os.path.join(os.path.dirname(__file__), "..", "..")
FIXTURES  = os.path.join(BASE_PATH, "fixtures")

##########################################################################
## BaseSearch Unit Tests
##########################################################################


class BaseSearchTests(unittest.TestCase):

    def test_init_with_list(self):
        """
        Check that search can be instantiated with a list of nouns
        """
        search = BaseSearch(['apples', 'building', 'cards', 'phone'])
        self.assertTrue(isinstance(search.nouns, list))

    def test_init_with_path(self):
        """
        Check that search can be instantiated with a path
        """
        nouns_path = os.path.join(FIXTURES, "testdata", "nouns.txt")
        search = BaseSearch(nouns_path)
        self.assertTrue(isinstance(search.nouns, list))
