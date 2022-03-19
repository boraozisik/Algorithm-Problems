"""
An emirp (prime spelled backwards) is a prime number that results in a different prime when its decimal digits
are reversed.
This definition excludes the related palindromic primes.
The term reversible prime is used to mean the same as emirp, but may also, ambiguously, include the palindromic primes.

Check that if a number is emirp or not.

"""


def is_prime(number):

    answer = True
    for i in range(2, number):
        if number % i == 0:
            answer = False
            break

    return answer


def is_emirp(number):

    if is_prime(number):
        string_number = str(number)
        string_number_list = list(string_number)
        string_number_list.reverse()
        new_string = ""
        for i in string_number_list:
            new_string += i

        new_number = int(new_string)
        if is_prime(new_number):
            print("Your number is an emirp number")
        else:
            print("Your number is not an emirp number")

    else:
        print("Your number is not a prime number so it cannot be an emirp number")


is_emirp(13)