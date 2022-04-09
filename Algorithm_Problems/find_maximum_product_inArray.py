"""
Given an array of integers, find the maximum product of two integers in an array.
Return the elements of this array.
"""


def solution(arr):
    max = 0
    max_array = []
    for i in range(len(arr)):
        product = 1
        for j in range(i + 1,len(arr)):
            product = arr[j] * arr[i]
            if product > max:
                max = product
                max_array.append(arr[j])
                max_array.append(arr[i])


    print(max)
    print(max_array)

solution([-10,-3,5,6,-2])