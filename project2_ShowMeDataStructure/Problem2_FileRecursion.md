# Finding Files

## Data Structure
For this project, I had to implement a depth-first search algorithm to find all the paths of files under a directory of files (that can be considered as a tree where files act as leaves and directories act as internal nodes) that end with a specifix suffix. 
n = total number of files and directories in the entire tree.

## Time complexity
Traversing the tree recursively will take O(n) since we are visiting each single node.

## Space complexity
Since I am using recursion to find all the paths, in the worst case scenario, the return statement of list_of_paths will contain all the filesnames found.
The recursion, despite allowing a more "compact code", requires generally more space than an iterative function. Each time a recursive function is called, it will be added to the call stack and will only be executed until all the subsequent calls of the same functions finished executing.
On this problem, a recursive function is called each time a folder is found. In the worst case scenario, all the subfolders are nested. If d = number of directories, the space required will be O(d)