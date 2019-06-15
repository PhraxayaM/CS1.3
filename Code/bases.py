#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace
# COMPARE_INVERTED = {
#     0 : '0',
#     1 : '1',
#     2 : '2',
#     3 : '3',
#     4 : '4',
#     5 : '5',
#     6 : '6',
#     7 : '7',
#     8 : '8',
#     9 : '9',
#     10 : 'A',
#     11 : 'B',
#     12 : 'C',
#     13 : 'D',
#     14 : 'E',
#     15 : 'F',
#     16 : 'G',
#     17 : 'H',
#     18 : 'I',
#     19 : 'J',
#     20 : 'K',
#     21 : 'L',
#     22 : 'M',
#     23 : 'N',
#     24 : 'O',
#     25 : 'P',
#     26 : 'Q',
#     27 : 'R',
#     28 : 'S',
#     29 : 'T',
#     30 : 'U',
#     31 : 'V',
#     32 : 'W',
#     33 : 'X',
#     34 : 'Y',
#     35 : 'Z'
#
#
# }
COMPARE = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15,
    'g': 16,
    'h': 17,
    'i': 18,
    'j': 19,
    'k': 20,
    'l': 21,
    'm': 22,
    'n': 23,
    'o': 24,
    'p': 25,
    'q': 26,
    'r': 27,
    's': 28,
    't': 29,
    'u': 30,
    'v': 31,
    'w': 32,
    'x': 33,
    'y': 34,
    'z': 35
}


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]

    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)

    # We get the power by taking the length of the array and starting at the highest possible value
    # When we create our loop, as we iterate through our array, our indexes will increment by 1 while
    # our power will decrease by 1

    power = len(digits) - 1
    counter = 0

    # iterate through digits
    for digit in digits:
        value_of_digit = COMPARE[digit]
        counter += value_of_digit * (base ** power)
        power -= 1
    return counter


    # ...
    # TODO: Decode digits from hexadecimal (base 16)
    # ...
    # TODO: Decode digits from any base (2 up to 36)
    # ...


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    # Create an empty string to keep track of each character in the conversion
    conversion = ''
    # Concatinate digit and string. The output will be '0123456789abcdefghijklmnopqrstuvwxyz'
    compare = string.digits + string.ascii_lowercase

    # while the number we are passing through is greater than 0
    while number > 0:
        remainder = number % base
        number = number // base
        # divmod returns (number, remainder)
        conversion = compare[remainder] + conversion

    return conversion



    # ...
    # TODO: Encode number in hexadecimal (base 16)
    # ...
    # TODO: Encode number in any base (2 up to 36)
    # ...


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...

    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    # main()
    # print(decode('10', 2))
    print(encode(10,2))
