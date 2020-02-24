# HTTPRouter using a Trie

For this problem, I used a Trie to represent a path. 
n = number of element in the path separated by a "/" 
The time complexity is O(n) to find or insert a path. For each operation, we will go to each node that corresponds to the proper element

m = number of nodes in the tree (number of subelements in paths)
The space complexity is O(m).