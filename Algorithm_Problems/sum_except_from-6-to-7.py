"""
Return the sum of the numbers in the array, except ignore sections
of numbers starting with a 6 and extending to the next 7
(every 6 will be followed by at least one 7). Return 0 for no numbers.

Example:
    Given:[1,2,3,6,92,97,7,4,5,4]
    The result is 19 because we are ignoring from 6 to 7(ignore 6,92,97,7).
"""

def solution(list):
    sum = 0
    sum2 = 0
    last_sum = 0
    for i in list:
        sum += i

    for i in range(len(list)):
        if list[i] == 6:
            for j in range(list.index(6), list.index(7) + 1):
                sum2 += list[j]

    last_sum = sum - sum2
    print(last_sum)


solution([1,2,3,6,92,97,7,4,5,4])