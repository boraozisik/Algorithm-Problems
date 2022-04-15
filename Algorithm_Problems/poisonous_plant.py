"""
There are a number of plants in a garden.
Each of the plants has been treated with some amount of pesticide.
After each day, if any plant has more pesticide than the plant on its left, being weaker than the left one, it dies.
You are given the initial values of the pesticide in each of the plants.
Determine the number of days after which no plant dies,
 i.e. the time after which there is no plant with more pesticide content than the plant to its left.

Sample Input
6 5 8 4 7 10 9

Sample Output
2
"""


def solution(arr):
    stack = []
    max_day = 0

    for i in arr:
        day = 0
        while stack and stack[-1][0] >= i:
            day = max(day, stack.pop()[1])

        if stack:
            day += 1

        else:
            day = 0

        max_day = max(max_day, day)
        stack.append([i, day])

    print(max_day)


plants = [6, 5, 8, 4, 7, 10, 9]

solution(plants)