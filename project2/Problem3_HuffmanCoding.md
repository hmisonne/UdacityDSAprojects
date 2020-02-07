# Huffman Coding

For this problem, I had to implement an algorithm for compressing data following the Huffman code.

## Time complexity
**Encoding function:**
To build a dictionary m unique char, it takes O(n) (n being the total number of char of the data). 
Then to iterate over the dictionary to build a list of tuple it takes O(m), and then to sort O(m log m)

To build a huffman tree, I iterated over the entire list of tuples m and then at each iteration sorted the list which would take O(m*(m log m))

To add binary code to the tree, since all the nodes of the trees are visited, it takes O(m)

To encode the data, it finally takes O(n)

So the overall time complexity is O(m^2 log m)

**Decoding function**
To decode the data, I iterated over all the numbers of the data which takes O(n)

## Data Structure

To solve this problem, I first used a dictionary to determine the frequency of each characted.
Then I used a list of tuples to sort each character from the lowest to the highest frequency.
This would then allow me pop the 2 tuples with the lowest frequency in O(1) to build new nodes for the huffman tree.

The binary tree is then a nice tool to generate unique prefix.

Once the tree is built, I used a dictionary to match the binary code with the letter. 


