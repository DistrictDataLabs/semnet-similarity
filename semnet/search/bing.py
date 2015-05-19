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
import string
from base import BaseSearch

#############################################################
## Bing Search API
#############################################################

class BingSearch(BaseSearch):
    """
    Implements the Bing search API.
    """

    HOST = "https://api.datamarket.azure.com/Data.ashx/Bing/Search/v1/Composite?"
    
    def __init__(self, key):
        self.key = key
        
    def search(self, sources, query, params):
    	"""
    	Search for the query on Bing
    	"""
    	request = 'Sources=%27' + sources + '%27'
    	request += '&Query=%27' + str(query) + '%27'
    	for key,value in params.iteritems():
    		request += '&' + key + '=' + str(value) 
        request = self.HOST + request
        return requests.get(request, auth=(self.key, self.key))

if __name__ == "__main__":
	my_key = raw_input("Enter your API key: ")
	query_string = raw_input ("Enter your search terms: ")
	bing = BingSearch(my_key)
	params = {'$format': 'json',
			  '$top': 10,  # change to 1000
			  '$skip': 0}
	print bing.search('web',query_string,params).json()