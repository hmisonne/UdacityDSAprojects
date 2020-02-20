from test import test
import heapq 
import math

def calculate_distance(M,a,b):
    #     estimate distance based on coordinates (search admissible)
    a_x, a_y = M.intersections[a]
    b_x, b_y = M.intersections[b]
    return math.sqrt((b_x - a_x)**2 + (b_y - a_y)**2)

def shortest_path(M,start,goal):
    print("shortest path called")
    
    # Estimated distance from start to goal
    h = calculate_distance(M, start, goal)
    # Actual distance from start
    g = 0
    # Initialization of variables     
    f = g + h
    path = [(f, g, [start])]
    current_intersection = start
    explored_intersections = {}
    heapq.heapify(path) 
    if start == goal:
        return [goal]
    
    while True:
        current_path = heapq.heappop(path)
        current_intersection = current_path[2][-1]
        if current_intersection != goal:
            #  Mark current intersection as visited
            explored_intersections[current_intersection] = True

            # Get the shortest path and distance from start     
            current_distance = current_path[1]

            # Loop through intersections of current_instersection
            for intersection in M.roads[current_intersection]:
                if intersection not in explored_intersections:
                    # Add a new path
                    g = current_distance + calculate_distance(M, current_intersection, intersection)
                    h = calculate_distance(M, intersection, goal)
                    f = g + h
                    new_path = current_path[2]+[intersection]
                    heapq.heappush(path,(f, g, new_path))

        else:
            return current_path[2]
                 
        

test(shortest_path)