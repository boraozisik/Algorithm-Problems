"""
Any word that exactly reproduces the letters in another order is an anagram.

In other words, X and Y are anagrams if by rearranging the letters of X, we can get Y using all the original letters of
X exactly once.

Given two strings, determine if they are anagrams or not.If they are, return true else, return false.

Example:
    When the solution is called with the following input str1 = "the eyes" and str2 = "they see", since these strings
    are anagrams, the solution should print true.

"""


def solution(str1, str2):
    list_str1 = list(str1)
    list_str2 = list(str2)
    list_str1.sort()
    list_str2.sort()
    if " " in list_str1:
        list_str1.remove(" ")
    if " " in list_str2:
        list_str2.remove(" ")

    if list_str1 == list_str2:
        return True
    else:
        return False


print(solution("the eyes", "they see"))