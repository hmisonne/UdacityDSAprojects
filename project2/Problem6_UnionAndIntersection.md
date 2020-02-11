# Union and Intersection of Two Linked Lists

## Data Structure
For both algorithms I used a set which automatically removes duplicates.

## Time Complexity
n: number of elements in a list
**union**
This algorithm is first traversing both input linked list to append elements to a set (to remove duplicates) and then it going through the set to append unique elements to a new linked list which takes O(n).

**intersection**
I used a set to store all the elements of the first input list which takes O(n). Then I iterated over the elements of the 2nd list to compare each value with the content of the 1st list. I will then do n iterations of the second input list, and for each iteration compare with n elements of the first list. Which means that worst case scenario we will have O(n^2)  

## Space Complexity
**union**
The space complexity is O(n). We are using memory to store 2 linkedlist of n elements and 1 set of n elements.
We are then building a new linkedlist of 2n elements if the lists do not share common elements (worst case scenario).

**intersection**
The space complexity is O(n). We are using memory to store 2 linkedlist of n elements and 1 set of n elements.
We are then building a new linkedlist of n elements if linkedlist contains the same exact elements (worst case scenario).

