"""
Given a side of a equilatral triangle:
Find the area of this triangle.
"""

import math


def solution(side):

    area = ((side * side) * math.sqrt(3)) / 4

    print(area)


solution(4)
