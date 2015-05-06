# search.base
# Base API for search related corpus harvesting
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Tue May 05 19:19:00 2015 -0400
#
# Copyright (C) 2015 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: base.py [] benjamin@bengfort.com $

"""
Base API for search related corpus harvesting
"""

##########################################################################
## Imports
##########################################################################


class BaseSearch(object):
    """
    Base class that defines the interface for the search APIs.
    """

    def __init__(self, path_or_list_nouns):
        """
        Pass in a path to a newline delimited list of nouns or an actual
        Python list of nouns with which to perform the search.
        """

        if isinstance(path_or_list_nouns, basestring):
            with open(path_or_list_nouns, 'r') as f:
                self.nouns = [n.strip() for n in f.read().split("\n")]

        else:
            self.nouns = path_or_list_nouns

    def __iter__(self):
        for query in self.queries:
            for result in self.search(query):
                yield result

    @property
    def queries(self):
        """
        Returns all the search queries based on the list of nouns, e.g. both
        IND and AND queries for the entire list.

        TODO: add conjunctive queries
        """
        # equivalent to return [n for n in self.nouns]
        for noun in self.nouns:
            yield noun

    def search(self, query):
        """
        All search apis (Google, Yahoo, Bing) implement the harvest method
        to do the actual fetching of results. It must return an iterable of
        results, expected to be the top 1000 web snippets associated with the
        query. E.g. return a generator of each of the 1000 web snippets.
        """
        raise NotImplementedError(
            "Subclasses must implement the search method"
        )

if __name__ == '__main__':
    search = BaseSearch(['apple', 'building', 'mana', 'cards'])
    for result in search:
        # do something with results
        pass
