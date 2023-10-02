#!/usr/bin/python3
"""Module for the rain function
"""
def rain(walls):
    """Calculates how much rain a series of walls can hold
    """

    # Return 0 if there are no walls
    if len(walls) == 0:
        return 0
    
    # If there are walls
    current_volume = 0
    total_volume = 0
    current_left_wall = 0

    for wall in walls:
        if wall >= current_left_wall:
            total_volume += current_volume
            current_left_wall = wall
            current_volume = 0
        else:
            current_volume += current_left_wall - wall


    return total_volume