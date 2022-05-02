"""
You need to sort the integers in array with selection sort.
"""

def solution(numbers):

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[i]:
                temp = numbers[j]
                numbers[j] = numbers[i]
                numbers[i] = temp

    print(numbers)


numbers = [1, 4, 5, 7, 2, 9, 4]

solution(numbers)
