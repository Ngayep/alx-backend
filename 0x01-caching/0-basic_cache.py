#!/usr/bin/env python3
""" BasicCache module """


ifrom base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class that inherits from BaseCaching and
        acts as a basic caching system without any limit.
    """

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
