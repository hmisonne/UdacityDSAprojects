# Finding the Square Root of an Integer

For this problem, I chose to implement a binary search to achieve the O(log(n)) requirement.
At each iteration, we will cut in half the area of search and move closer to the target.
The space complexity is O(1) since we are only comparing one number at a time.