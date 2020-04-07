"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered with Rot13.
If there are numbers or special characters included in the string, they should be returned as they are.
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation"

"""

def rot13(message):
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    capital_letters = lower_letters.upper()
    numbers = '0123456789'
    symbols = "!@#$%^&*()[]{}'/.><?,'=-+"
    new_message = ''
    letter_number = 0
    for char in message:
        if char in lower_letters:
            for i in range(len(lower_letters)):
                if lower_letters[i] == char:
                    letter_number = i
                    counter = 0
                    new_letter_num = i
                    while counter != 13:
                        if new_letter_num < 25:
                            new_letter_num += 1
                        else:
                            new_letter_num = 0
                        counter += 1
                    new_message += lower_letters[new_letter_num]
        elif char == ' ':
            new_message += ' '
        elif char in numbers:
            new_message += char
        elif char in symbols:
            new_message += char
        else:
            for i in range(len(capital_letters)):
                if capital_letters[i] == char:
                    letter_number = i
                    counter = 0
                    new_letter_num = i
                    while counter != 13:
                        if new_letter_num < 25:
                            new_letter_num += 1
                        else:
                            new_letter_num = 0
                        counter += 1
                    new_message += capital_letters[new_letter_num]

    return new_message


print(rot13('Test 1234 test motherfucker!@>@$?'))
print(rot13('10+2 equals twelve'))
