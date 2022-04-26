"""
Given an array of integers, replace each element of the array with the product of every other element in the array.
Return the modified array.
"""


def solution(list):
    final_list = []
    for i in range(len(list)):
        temp_list = []
        sum = 1
        for j in list:
            temp_list.append(j)

        temp_list.remove(list[i])

        for j in temp_list:
            sum *= j

        final_list.append(sum)

    print(final_list)


solution([1,2,3,4,5])



