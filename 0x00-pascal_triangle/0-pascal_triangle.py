#!/usr/bin/python3
"""
0. Pascal's Triangle
"""

def pascal_triangle(n):
    """Create a function that returns a list of lists
    of integers representing the Pascal’s triangle of n.
    
    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        List[List[int]]: A list of lists containing the rows of Pascal's triangle.
    """
    res = []
    if n > 0:
        for i in range(n):  # Start from 0
            level = []
            C = 1
            for j in range(i + 1):  # Iterate from 0 to i
                level.append(C)
                C = C * (i - j) // (j + 1)  # Corrected calculation
            res.append(level)
    return res
