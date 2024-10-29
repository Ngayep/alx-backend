#!/usr/bin/python3
""" FIFOCache module """


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching and uses
        a First-In, First-Out (FIFO) caching system.
    """

    def __init__(self):
        """ Initialize the FIFOCache with a call
        to the parent class's initializer """
        super().__init__()
        self.order = []  # List to keep track of insertion order of keys

    def put(self, key, item):
        """ Add an item to the cache using FIFO eviction policy """
        if key is None or item is None:
            return  # Exit if either key or item is None

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the first item in the FIFO order
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

        # Add or update the item in the cache
        self.cache_data[key] = item
        if key not in self.order:
            self.order.append(key)  # Track the insertion order

    def get(self, key):
        """ Retrieve an item from the cache by key """
        return self.cache_data.get(key, None)
