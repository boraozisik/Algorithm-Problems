"""
Given an array of integers, find the maximum length of the sub-array having the given sum.

Example Solution. Let array arr equal to [ 5, 6, -5, 5, 3, 5, 3, -2, 0] and sum 8.
Result is [5, -5, 5, 5, -2, 0] and length of this array is 6.
"""


def solution(list,sum):
    subarrays = [[]]
    result = []
    max_length = 0
    max_length_array = []

    for i in list:
        subarrays = subarrays + [j + [i] for j in subarrays]


    for i in subarrays:
        temp_sum = 0
        for j in range(len(i)):
            temp_sum += i[j]
        if temp_sum == sum:
            result.append(i)

    for i in result:
        if len(i) >= max_length:
            max_length = len(i)
            max_length_array = i

    print(max_length_array)
    print(max_length)


solution([5,6,-5,5,3,5,3,-2,0],8)