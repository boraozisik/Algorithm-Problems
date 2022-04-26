"""
Given a number:
Reverse this number and return the result.
Ex:
Given: 12356789
Result: 98765321
"""


def solution(number):
    number = str(number)
    list_number = list(number)
    list_number.reverse()
    new_string = ""
    for i in list_number:
        new_string += i

    new_string = int(new_string)

    print(new_string)


solution(12356789)
