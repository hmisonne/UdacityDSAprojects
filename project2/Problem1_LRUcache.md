# Least Recently Used Cache (LRU):

For this project, I had to implement a LRU that has the following requirements:
- all operations must take O(1) time.
- the size of the cache must not exceed 5
- if the cache is full, discard the least recently used entry

## Data Structure & Time complexity
The first data structure that comes in mind is the Hash Table. This would allow a fast look up of value given a unique key. However since the size of the cache was limited to 5 entries, I decided to use a dictionary that would also allowed an instant lookup and was easier to implement.

To track the least recently used entry, I chose the doubly linked list.
With this datastructure, I could in O(1) insert and remove entries. However, to move a node to the front of the list, it could take in a worst case scenario: O(n-2) if the node is located just before the tail (time needed to traverse the doubly linked list to find the node)

The space complexity is O(n) since the data is stored in a dictionary and in a linked list.