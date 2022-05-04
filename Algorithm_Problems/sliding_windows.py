"""
Find Maximum of Minimums in Sliding Windows.
Given an integer array of size n, find the maximum of the minimum's for every window size in the array.
"""

def solution(list):
    new_list = [max(list)]
    minimums = []
    for i in range(2, len(list)):
        temp_list = []
        for j in range(i):
            for k in range(j):
                temp_list.append(list[k])
                minimums.append(min(temp_list))

        new_list.append(max(minimums))

    print(new_list)


list = [10,20,30,50,10,70,30]
solution(list)