"""
Given two binary numbers, write a Python program to compute their sum.
Result must be also binary.

Example:
    Given: "1011" and "1010"
    Result: "10101"
"""




def solution(binary1,binary2):
    binary1_list = list(binary1)
    binary1_list.reverse()
    value_binary1 = 0
    index1 = 0
    binary2_list = list(binary2)
    binary2_list.reverse()
    value_binary2 = 0
    index2 = 0
    total_value = 0
    while index1 < len(binary1_list):
        for i in binary1_list:
            value_binary1 += int(i) * int(2**index1)
            index1 += 1

    while index2 < len(binary2_list):
        for i in binary2_list:
            value_binary2 += int(i) * int(2**index2)
            index2 += 1

    total_value = value_binary1 + value_binary2

    binary_value = format(total_value, "b")

    print(binary_value)


solution("1011", "1010")