"""
Given 3 number that specifies the burned calories.
Target for burned calories is 500 calories, check that target is reached or not.
If not reached, print the total calories spend.
"""



def solution(inputs):
    total = 0

    for i in inputs:
        total += i

    if total >= 500:
        print("Target is reached")
    else:
        print("Total {}".format(total))


inputs = {20, 100, 300}

solution(inputs)
