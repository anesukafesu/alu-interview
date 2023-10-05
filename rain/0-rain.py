#!/usr/bin/python3
"""Module for the rain function
"""
def rain(walls = []):
    """Calculates how much rain a series of walls can hold
    """
    number_of_walls = len(walls)

    # Return 0 if there are no walls
    if number_of_walls == 0:
        return 0
    
    # Finding the highest wall to the left of each of wall
    highest_left_walls = []
    max_so_far = 0

    for i in range(number_of_walls):
        wall = walls[i]
        if wall > max_so_far:
            max_so_far = wall
        
        highest_left_walls.append(max_so_far)


    # Finding the highest wall to the right of each wall
    highest_right_walls = []
    max_so_far = 0

    for i in range(number_of_walls - 1, -1, -1):
        wall = walls[i]
        if wall > max_so_far:
            max_so_far = wall
        
        highest_right_walls.append(max_so_far)
    
    total_volume = 0
    
    # Calculate the amount of water held by each element
    for i in range(number_of_walls):
        highest_left_wall = highest_left_walls[i]
        highest_right_wall = highest_right_walls[i]
        wall_height = walls[i]

        volume = min(highest_left_wall, highest_right_wall) - wall_height

        total_volume += volume

    return total_volume