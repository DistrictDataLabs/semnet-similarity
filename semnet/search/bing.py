# semnet.search.bing
# Implements Bing API search
#
# Author: Rebecca Bilbro <bilbro@gmail.com>
# Created: Wed May 13 11:04:22 2015 -0400
#
# Copyright (C) 2015 District Data Labs
# For license information, see License.txt
#
# ID: bing.py [] bilbro@gmail.com

"""
Implements Bing API Search
"""

#############################################################
## Imports
#############################################################

import requests
import os   # to access API key
from base import BaseSearch

#############################################################
## Bing Search API
#############################################################

def quote(s):
    """
    strip single and double quotation marks from a string,
    then add single quotation marks to format for Bing
    """
    return "'%s'" % s.strip("\"'")

class BingSearch(BaseSearch):
    """
    Implements the Bing search API.
    """
    
    HOST = "https://api.datamarket.azure.com/Data.ashx/Bing/Search/v1/Composite"
    
    def __init__(self, key, format='json', top=10, skip=0):
        self.key    = key
        self.top    = top
        self.skip   = skip
        self.format = format
        
    def search(self, sources, query, **params):
        """
        Search for the query on Bing
        """
        data = {
            'Sources' : quote(sources),
            'Query'   : quote(query),
        }
        
        data.update(self.parse_default_params(params)) # merge params into data dictionary
        response=requests.get(self.HOST, params=data, auth=(self.key, self.key)) # send request

        response.raise_for_status() 
        return response # return REST status if error
    
    def parse_default_params(self, params):
        """
        Take default params and format them for Bing
        """
        defaults = {
            'format' : self.format,
            'top'    : self.top,
            'skip'   : self.skip,
        }
        
        defaults.update(params)
        return dict(("$" + key, val) for key,val in defaults.items())
 
    
#   ## Eventually we will want a function to handle multiple pages of results
#
#   def paginated_search(self, sources, query, **params):
#       while True:
#           yield self.search(sources, query, **params)
#           self.skip = self.skip + self.top        


if __name__ == "__main__":
    my_key = os.environ["BING_API_KEY"] # key stored in os path
    query_string = "bread and honey"
    bing = BingSearch(my_key)
    print bing.search('web', query_string).json()