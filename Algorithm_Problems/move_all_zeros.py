"""
Given an array
Move all zeros to the end of the array
"""


def solution(list):
    for i in range(len(list)):
        if list[i] == 0:
            temp = list[i]
            list.remove(temp)
            list.insert((len(list) + 1), temp)


    print(list)


solution([6,0,8,2,3,0,4,0,1])