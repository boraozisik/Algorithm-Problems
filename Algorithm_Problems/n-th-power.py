"""
Given a decimal number and a number that specifies the power of the decimal number.
Find this number's n. power.
"""


def solution(ran,num):
    result = 1
    for i in range(num):
        result *= ran

    return result


print(solution(3.500, 12))