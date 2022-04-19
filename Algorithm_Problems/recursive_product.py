"""
Write a recursive function that calculates product of two number with only summation.
Note: Inputs will ve ALWAYS positive numbers.
"""


def solution(number1, number2):
   if number2 == 1:
           return number1
   else:
           return number1 + solution(number1, number2 - 1)


print(solution(10, 12))