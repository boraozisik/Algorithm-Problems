"""
Given two arrays
Merge these arrays in ascending order
"""


def solution(arr1, arr2):
    count = 0
    for i in range(len(arr1)):
        if arr1[i] == 0:
            arr1[i] = arr2[count]
            count +=1

    arr1.sort()
    print(arr1)


array1 = [0,2,0,3,0,5,6,0,0]
array2 = [1,8,9,10,15]
solution(array1,array2)