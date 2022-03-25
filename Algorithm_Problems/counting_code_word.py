"""
Given a string:

Find how many word => 'code' does this string contain.

"""


def solution(string):
    list_string = list(string)
    count = 0
    while len(list_string) > 3:
        temp = list_string[0] + list_string[1] + list_string[2] + list_string[3]
        if temp == "code":
            count += 1
            list_string.remove(list_string[0])
        else:
            list_string.remove(list_string[0])

    print(count)


solution("abdcodeadscodeasdrcodeyu")

solution("abdcodeadscodeasdrcodeyudfwfdsfcodefdsfsdcode")