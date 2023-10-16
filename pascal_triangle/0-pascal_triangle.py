#!/usr/bin/python3
""" Module with function to generate Pascal's Triangle
"""


def pascal_triangle(n):
    """ Function to generate Pascal's Triangle up to a given level, n
    args: n - the level up to which the triangle should be generated
    returns: [[]]
    """
    result = []

    if n >= 1:
        result.append([1])
    if n >= 2:
        result.append([1, 1])
    if n >= 3:
        # Loop to create result
        for i in range(3, n + 1):
            # Creating a reference to the previous row
            previous_row = result[-1]

            # Creating the current row
            current_row = []

            # Add the first element which is always a one
            current_row.append(1)

            # Looping throught the middle part of a row
            for j in range(1, i - 1):
                current_element = previous_row[j] + previous_row[j - 1]
                current_row.append(current_element)

            # Adding the last element of the row which is always a one
            current_row.append(1)

            # Adding the row to the result
            result.append(current_row)

    return result
