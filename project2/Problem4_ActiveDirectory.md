## Active Directory

For this problem, I needed to implement a lookup function to find if a user is in a group or subgroup directory.

I used recursion to go in the subfolder. The time complexity of this algorithm is O(n) (n being the total number of groups)
The space complexity is O(n) (equal to the number of return statements)