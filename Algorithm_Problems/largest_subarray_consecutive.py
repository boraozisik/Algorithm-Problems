"""
Find largest subarray with consecutive elements

Example:
    Given Array: [2,0,2,1,4,3,1,0,6,9,12,12,8,7,7,4,4,4,12,15]
    Output: [0, 1, 2, 3, 4, 6, 7, 8, 9, 12, 15]
"""

def solution(arr):
    arr.sort()

    for i in arr:
        count = arr.count(i)
        for j in range(count - 1):
            arr.remove(i)

    print(arr)


solution([2,0,2,1,4,3,1,0,6,9,12,12,8,7,7,4,4,4,12,15])