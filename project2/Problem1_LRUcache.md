# Least Recently Used Cache (LRU):

For this project, I had to implement a LRU that has the following requirements:
- all operations must take O(1) time.
- the size of the cache must not exceed 5
- if the cache is full, discard the least recently used entry

## Data Structure & Time complexity
I decided to use a dictionary to allow an instant lookup. I could also have chosen to use a Hash Table but since there was only a maximum of 5 entries to store, a dictionary was easier to implement. 

To track the least recently used entry, I chose the doubly linked list.
With this datastructure, I could in O(1) insert and remove entries. However, to move a node to the front of the list, it could take in a worst case scenario: O(n-2) if the node is located just before the tail (time needed to traverse the doubly linked list to find the node)

The space complexity is O(1) since we are only using memory to store one data at a time.