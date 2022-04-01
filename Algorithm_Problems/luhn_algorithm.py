"""
The Luhn algorithm, also known as the modulus 10 or mod 10 algorithm, is a simple checksum formula used to validate a variety of identification numbers, such as credit card numbers, IMEI numbers, Canadian Social Insurance Numbers. The LUHN formula was created in the late 1960s by a group of mathematicians. Shortly thereafter, credit card companies adopted it. Because the algorithm is in the public domain, it can be used by anyone. Most credit cards and many government identification numbers use the algorithm as a simple method of distinguishing valid numbers from mistyped or otherwise incorrect numbers. It was designed to protect against accidental errors, not malicious attacks.

Steps involved in the Luhn algorithm
Let’s understand the algorithm with an example:
Consider the example of an account number “79927398713“.
Step 1 – Starting from the rightmost digit, double the value of every second digit,
Step 2 – If doubling of a number results in a two digit number i.e greater than 9(e.g., 6 × 2 = 12), then add the digits of the product (e.g., 12: 1 + 2 = 3, 15: 1 + 5 = 6), to get a single digit number.
Step 3 – Now take the sum of all the digits.
Step 4 – If the total modulo 10 is equal to 0 (if the total ends in zero) then the number is valid according to the Luhn formula; else it is not valid.

"""




credit_card_number = list(input("Enter your credit card number: ").strip())

if len(credit_card_number) == 16:
    check_digit = credit_card_number.pop()

    credit_card_number.reverse()

    digits = []

    for index, digit in enumerate(credit_card_number):
        if index % 2 == 0:
            doubled_digit = int(digit) * 2
            if doubled_digit > 9:
                doubled_digit -= 9
                digits.append(doubled_digit)
            else:
                digits.append(doubled_digit)
        else:
            digits.append(int(digit))

    total = int(check_digit) + sum(digits)

    if total % 10 == 0:
        print("Valid credit card number")
    else:
        print("Invalid credit card number")

else:
    print("Invalid digit number for credit card!!")
