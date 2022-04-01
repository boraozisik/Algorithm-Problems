"""
Given two multiplier and limit number,
From zero to limit number find multiples of these given two number and take their sum
Example:
    Given: 3,5,1000
    Result: 233168
"""



def solution(firstMultiplier, secondMultiplier, limit):
    multiple_list = []
    sum = 0

    for i in range(limit):
        if i % firstMultiplier == 0 or i % secondMultiplier == 0:
            multiple_list.append(i)

    for i in multiple_list:
        sum += i


    print(sum)


solution(3,5,1000)
