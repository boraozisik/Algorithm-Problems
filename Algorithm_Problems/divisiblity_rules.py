"""
Given two integer:
Write a program which will find all such numbers which are divisible by 2 but are not a multiple of 5,
between number one and number two
"""


def solution(start_number,end_number):
    new_list = []
    for i in range(start_number, (end_number + 1)):
        if i % 2 == 0 and i % 5 != 0:
            new_list.append(i)

    print(new_list)


solution(2500, 4000)