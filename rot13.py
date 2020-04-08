"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered with Rot13.
If there are numbers or special characters included in the string, they should be returned as they are.
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation"

"""

import string

def encoded_char(step,char, string):
    for i in range(len(string)):
        if string[i] == char:
            char_num = i
            counter = 0
            new_char_num = i
            while counter != step:
                if new_char_num < (len(string) - 1):
                    new_char_num += 1
                else:
                    new_char_num = 0
                counter += 1
    new_char = string[new_char_num]

    return new_char

def rot13(message):
    new_message = ''
    letter_number = 0
    for letter in message:
        if letter in string.ascii_lowercase:
            new_message += encoded_char(13, letter, string.ascii_lowercase)
        elif letter == ' ':
            new_message += ' '
        elif letter in string.digits:
            new_message += letter
        elif letter in string.punctuation:
            new_message += letter
        else:
            new_message += encoded_char(13, letter, string.ascii_uppercase)
    return new_message

print(rot13('Test 1234 test person_1!@>@$?'))
print(rot13('10+2 equals twelve'))
