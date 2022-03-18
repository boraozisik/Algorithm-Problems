"""
Given an array.
Find all subarrays that sum of their elements is equal to zero.

"""


def solution(list):
    subarrays = [[]]

    final_list = []
    for i in list:
        subarrays = subarrays + [j + [i] for j in subarrays]

    for i in subarrays:
        sum = 0
        for j in i:
            sum += j
        if sum == 0:
            final_list.append(i)

    print(final_list)


solution([3,4,-7,3,1,3,1,-4,-2,-2])