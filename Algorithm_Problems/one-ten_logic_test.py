"""
A logic test that checks if the number is between 1 and 10.

Example:
    Given: (14,True) and (8,True)
    Result: False and True
"""



def solution(number, statement):
    is_range = False
    final_statement = False

    if 0 <= number <= 10:
        is_range = False
    else:
        is_range = True

    if statement != is_range:
        final_statement = True

    print(final_statement)


solution(14,True)
solution(8,True)