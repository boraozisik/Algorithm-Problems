"""
Calculate the value of a given expression in Reverse Polish Notation.
"""

import math


def rpn(list):
    stack = []
    operators = {"+", "-", "*", "/"}

    if len(list) == 1:
        return int(list[0])

    for i in list:
        if i not in operators:
            stack.append(int(i))

        else:
            trsc = 0
            second_operand = stack.pop()
            first_operand = stack.pop()
            if i == "+":
                trsc = first_operand + second_operand

            elif i == "-":
                trsc = first_operand - second_operand

            elif i == "*":
                trsc = first_operand * second_operand

            elif i == "/":
                trsc = first_operand / second_operand
                trsc = math.trunc(trsc)

            stack.append(trsc)
    result = stack.pop()
    return result


liste = ["5", "2", "+", "6", "*"]

print(rpn(liste))
