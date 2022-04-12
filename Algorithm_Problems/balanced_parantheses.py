"""
Given an expression string, write a python program to find whether a given string has balanced parentheses or not.
Example:
    Input: {()}[]{[]}
    Output: True

    Input: {()]}
    Output: False
"""


def solution(list):
    while True:
        if "()" in list:
            list = list.replace("()", "")
        elif "{}" in list:
            list = list.replace("{}", "")
        elif "[]" in list:
            list = list.replace("[]", "")

        else:
            return not list


print(solution("{()}[]{[]}"))
print(solution("{()]}"))