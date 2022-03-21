"""
Given a String, remove all vowels.

Example:
    Given: "Hello, I love Python!"
    Result: Hll, I lv Pythn!
"""


def remove_vowels(string):
    vowels = ('a', 'e', 'i', 'o', 'u');

    for i in string.lower():
        if i in vowels:
            string = string.replace(i, "");

    print(string);


remove_vowels("Hello, I love Python!")