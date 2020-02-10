# Union and Intersection of Two Linked Lists



**union**
For this function, I decided not to copy the head of one input list into a new one since doing so would also alter the input list. 
I initialized a new linked list and traverse both input linked list to append elements to the new linked list which takes O(n).

**intersection**
I used a list to store all the elements of the first input list which takes O(n). 
This allows me to determine if an element of the second input list is also on the first input list which takes O(n * m). 

The space complexity is O(1) since memory is only used one element at a time

