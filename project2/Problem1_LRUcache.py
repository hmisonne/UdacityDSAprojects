# Your work here
import collections
de = collections.deque([])

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.count_of_elements = 0
        self.storage = {}

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.storage:
            return -1
        else:
            new_de = collections.deque([])
            return self.storage[key]

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key not in self.storage:
            if self.count_of_elements < self.capacity:
                self.count_of_elements += 1
            else:
                key_to_remove = de.popleft()
                print('key_to_remove',key_to_remove)
                del self.storage[key_to_remove]
            self.storage[key] = value
            de.append(key)
        else:
            self.storage[key] = value
