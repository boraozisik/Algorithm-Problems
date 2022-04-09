"""
Find the largest number possible from a set of given numbers where the numbers append to each other
in any order to form the largest number.

For example,

Input:  { 10, 68, 75, 7, 21, 12 }

Output: 77568211210

"""


def solution(number_list):
    number_list.sort(reverse=True)
    string = ""
    temp_list = []
    max_value_list = list(str(max(number_list)))
    if min(number_list) >= int(max_value_list[0]):
        temp = min(number_list)
        number_list.remove(temp)
        number_list.insert(0, temp)

    for i in number_list:
        temp_list.append(str(i))

    for i in temp_list:
        string += i

    print(string)


solution([10, 68, 75, 7, 21, 12])