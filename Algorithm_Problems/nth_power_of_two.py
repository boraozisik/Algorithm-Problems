"""
Check that the number nth power of two.
"""


def solution(number):
    answer = False
    for i in range(1, number):
        if number == 2**i:
            answer = True
            print("This number is {}. power of two".format(i))

    return answer


print(solution(128))
