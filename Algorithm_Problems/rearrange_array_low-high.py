"""
Given an integer array, rearrange it such that every second element becomes greater than its left and right elements.
Assume no duplicate elements are present in the array.
"""


def solution(list):
   for index in range(1,len(list) - 1):
         if list[index] < list[index + 1]:
            temp = list[index + 1]
            list[index + 1] = list[index]
            list[index] = temp
         elif list[index] < list[index - 1]:
             temp = list[index - 1]
             list[index - 1] = list[index]
             list[index] = temp
         else:
             continue

   print(list)


solution([1,2,3,4,5,6,7])
