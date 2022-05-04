"""
The function receives 2 integer parameters ; first grade and then attendance percentage.
If the attendance is below 80, the student fails.
If grade is below 40 student also fails.
If garde is greater than 40 but less than 50 student soft passes.
If grade is greater than 50 student passes.
Print that student fails or passes.
"""


def solution(grade, attendance):
    answer = ""
    if attendance < 80:
        answer = "FAİL"

    else:
        if grade < 40:
            answer = "FAİL"
        elif 40 <= grade <=49:
            answer = "SOFT PASS"
        else:
            answer = "PASS"

    return answer


print(solution(58,80))
