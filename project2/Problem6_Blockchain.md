# Blockchain

To implement a blockchain, I needed to create a linked list of blocks. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data.

## Time Complexity

Adding a new block to the chain can be done in O(1) since a reference of the tail is kept.
Checking if the blockchain is valid takes O(n) since we are iterating over all the blocks of the chain.

