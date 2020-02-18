# Rearrange Array Elements

n = length of the array
For this problem, I used the merge sort algorithm to achieve the O(nlog(n)) time complexity. This merge sort algorithm is using recursion to divide the array in half and sort.

I sorted the array from the highest to lowest number and on the final merge, instead of returning on sorted list I returned the 2 highest numbers

The space complexity is O(n)