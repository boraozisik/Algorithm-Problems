"""
Given a limited range array of size n where array contains elements between 1 to n-1 with one element repeating,
find the duplicate number in this array.

Example:
    given: [1,2,3,2,4] return:2
    given: [1,2,3,4,4] return:4

"""


def solution(array):

    duplicate_element = 0
    for i in range(len(array)):
        temp_element = array[i]
        count = 0
        for j in array:
            if j == temp_element:
                count += 1
            if count == 2:
                duplicate_element = j
                count = 0

    print(duplicate_element)


solution([1,2,3,2,4])
