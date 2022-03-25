"""
Given a string:

Convert uppercase letters to lowercase and convert lowercase letters to uppercase.

Example:
    Given: "HeLlOworLD"
    Result: "hElLoWORld"
"""


def solution(string):
    new_list = list(string)
    str = ""
    for i in range(len(new_list)):
        if new_list[i].isupper():

           new_list[i] = new_list[i].lower()
        else:
           new_list[i] = new_list[i].upper()

    for i in new_list:
        str += i

    print(str)


solution("HeLlOworLD")