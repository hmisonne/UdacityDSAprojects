# Autocomplete with Tries

For this project, I built a Trie and used recursion to find suffixes.
For n = number of char, the time complexity is O(n) to find a prefix node since we are following the nodes of the tree based on the char of the prefix.
To find the suffixes for a prefix we need to traverse all the nodes until a leaf is found. If n is the number of nodes found after a prefix, the time complexity will be O(n).

m = number of nodes in the tree
The space complexity is O(m).