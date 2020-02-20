# Implementing a Route Planner

To implement a route planner I used a dictionary to have an instant lookup of visited intersections and I used a list of tuples to store all the potential paths. 
The first element of the tuple is the a combination of estimated and actual distance from start to goal, which allows me to get the shortest distance easily by sorting the tuples.

n = total number of edges
The time complexity of this algorithm is O(n) worst case if all the intersections are located in between start and finish.
m = number of potential paths between start and finish
The space complexity of this algorithm is O(m)

