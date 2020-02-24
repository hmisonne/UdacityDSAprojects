# Implementing a Route Planner

To implement a route planner I used a dictionary to have an instant lookup of visited intersections and I used a min priority list (implemented with a heap) to store all the potential paths. The potential paths are tuples with 3 elements: total distance, distance from start, list of intersections.
The first element of the tuple is the a combination of estimated and actual distance from start to goal, which allows me to get the shortest distance easily by popping the first element of the Heap (or Min Priority Queue).
Having a priority queue allows to reduce time complexity of getting the smallest element from O(n log(n)) of sorting an array to O(log(n))

n = total number of edges
The time complexity of evaluating the shortest path is O(n) worst case if all the intersections are located in between start and finish. 
m = number of potential paths between start and finish
The space complexity of this algorithm is O(m)

