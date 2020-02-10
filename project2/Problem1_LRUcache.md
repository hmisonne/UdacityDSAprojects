# Least Recently Used Cache (LRU):

For this project, I had to implement a LRU that has the following requirements:
- all operations must take O(1) time.
- the size of the cache must not exceed 5
- if the cache is full, discard the least recently used entry

## Data Structure & Time complexity

To track the least recently used entry, I chose the doubly linked list.
With this datastructure, I could insert and remove entries in O(1).
However, to retrieve a value based on a key, or to move a node located in the middle of the linked list could take O(n) since we would need to traverse the chain.

To allow instant lookup O(1) and avoid traversing all the nodes of the linked list, I decided to use a Hash Table.

When a new entry is set, it will create a new bucket in the hashtable with a value and a reference to the node of the linked list. With this reference, we can move any node of the linked list to the head.

The space complexity is O(n) since we need to the references of all the data stored to allow O(1) time complexity.