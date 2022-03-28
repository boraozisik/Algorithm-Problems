"""
Given a number that specifies sum and given an array of numbers
Find the pair of numbers that their sum is equal to parameter sum and print these numbers's index

Example:
    Given: (10,[8,7,2,5,3,1])
    Result: [0, 2]
            => index 0 = 8 and index 2 = 2 ==> 8 + 2 = 10
"""



def solution(sum, arr):
    list = []
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            if arr[i] + arr[j] == sum:
                list.append(arr.index(arr[i]))
                list.append(arr.index(arr[j]))
        break


    print(list)


solution(10,[8,7,2,5,3,1])