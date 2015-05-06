# semnet.search.google
# Implements the Google API search
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Tue May 05 20:02:58 2015 -0400
#
# Copyright (C) 2015 District Data Labs
# For license information, see LICENSE.txt
#
# ID: google.py [] benjamin@bengfort.com

"""
Implements the Google API search
"""

##########################################################################
## Imports
##########################################################################

import requests

from base import BaseSearch


##########################################################################
## Google Search API
##########################################################################

class GoogleSearch(BaseSearch):
    """
    Implements the Google search API.
    """

    HOST = "http://ajax.googleapis.com/ajax/services/search/web"

    def search(self, query):
        """
        Search for the query on Google
        """
        response = requests.get(self.HOST, params={"v": "1.0", "q": query})

        for item in response.json()['responseData']['results']:
            yield item['content']

if __name__ == '__main__':
    search = GoogleSearch([])
    for result in search.search("Honeybadger"):
        print result
        print
