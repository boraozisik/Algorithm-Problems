"""
Given a pattern containing only I’s and D’s. I for increasing and D for decreasing.
Device an algorithm to print the minimum number following that pattern.
Digits from 1-9.
"""


def solution(sequence):
    sequence_list = list(sequence)
    string = ""
    i = 1
    for j in range(len(sequence_list)):

            if sequence_list[j] == "D":
                string += str(i + 1)
                string += str(i)
                i += 1
            else:
                string += str(i + 2)
                string += str(i + 1)
                i += 1

    print(string)


solution("DIDI")