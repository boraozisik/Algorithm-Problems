"""
Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of
elements at higher indexes.

Given an array of integers.

Find equilibrium indexes.

Example:
    Given: [0,-3,5,-4,-2,3,1,0]
    Result: [0, 3]

"""


def solution(list):
    final_list = []
    for i in range(len(list)):
        sum1 = 0
        sum2 = 0
        for j in range(i):
            sum1 += list[j]

        for j in range(i + 1, len(list) - 1):
            sum2 += list[j]

        if sum1 == sum2:
            final_list.append(list.index(list[i]))

    print(final_list)


solution([0, -3, 5, -4, -2, 3, 1, 0])
