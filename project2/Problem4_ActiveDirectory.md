# Active Directory

For this problem, I needed to implement a lookup function to find if a user is in a group or subgroup directory which can be visualized as a tree.

## Time complexity
I used recursion to go in the subfolder. 
n = total number of groups
m = total number of users
The time complexity of this algorithm is O(n + m) in the worst case scenario, where the user is located on the furthest subfolder.

## Space complexity
Since we are using recursion, each time a subfolder is found a new function will be added to the stack thus and will be removed from the stack only when the subsequent function is executed. Worst case scenario, all the groups are being nested: the space complexity is O(n) 