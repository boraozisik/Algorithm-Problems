"""
A Hippodrome is organizing a new type of horse racing: duals.
During a dual, only two horses will participate in the race.
Print max two horse
"""


def solution(list):

    list.remove(list[0])
    max_horses = []
    max_horse = max(list)
    max_horses.append(max(list))
    list.remove(max_horse)
    max_horse2 = max(list)
    max_horses.append(max_horse2)
    print(max_horses)
    print(max_horse - max_horse2)

solution([7,5,7,6,5,6,6,5])