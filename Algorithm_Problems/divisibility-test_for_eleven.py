"""
Given an array of integers:

Find elements that divisible by eleven and take these elements average.
"""


def solution(list):
    div_eleven_list = []
    average = 0
    sum = 0
    for i in list:
        if i % 11 == 0:
            div_eleven_list.append(i)

    for i in div_eleven_list:
        sum += i

    average = sum / len(div_eleven_list)

    print(average)


solution([10,21,246,33,47,44,99])