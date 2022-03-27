"""
Given an array of integers

Find maximum difference between two element but,
the index of the larger element must be greater than the index of the smaller element.

Example:
    Given: [2,7,9,5,1,3,5]
    Result: 7 (9 - 2)
"""


def solution(list):
    result = 0

    for i in range(len(list)):
        max_value = max(list)
        min_value = min(list)
        if list.index(max_value) > list.index(min_value):
            result = max_value - min_value
        else:
            list.remove(min_value)

    print(result)

solution([2,7,9,5,1,3,5])