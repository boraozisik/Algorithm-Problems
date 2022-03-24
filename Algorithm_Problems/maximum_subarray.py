"""
Given an array
Find  the highest sum of the subarrays.

"""


def solution(number_list):
    result = [[]]
    sum = 0
    max = 0

    for i in number_list:
        result = result + [j + [i] for j in result]

    for i in result:
        for j in i:
            sum += j
            if sum > max:
                max = sum
        sum = 0

    print(max)


solution([-2,1,-3,4,-1,2,1,-5,4])