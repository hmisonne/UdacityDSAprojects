from test import test

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
    
    if start == goal:
        return [goal]
    
    while current_intersection != goal:
        #  Mark current intersection as visited
        explored_intersections[current_intersection] = True
        
        # Get the shortest path and distance from start     
        current_path = path.pop(0)
        current_distance = current_path[1]

        # Loop through intersections of current_instersection
        for intersection in M.roads[current_intersection]:
            if intersection not in explored_intersections:
                # Add a new path
                g = current_distance + calculate_distance(M, current_intersection, intersection)
                h = calculate_distance(M, intersection, goal)
                f = g + h
                new_path = current_path[2]+[intersection]
                path.append((f, g, new_path)) 
        # Sort the list to get the shortest path on the first position
        path = sorted(path)
        # Update the current_intersection to match the current shortest path
        current_intersection = path[0][2][-1]     
        
    shorted_path = sorted(path)[0][2]
    return shorted_path




test(shortest_path)