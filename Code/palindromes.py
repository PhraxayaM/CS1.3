#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests

    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    #return is_palindrome_recursive(text)

def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests
    left_index = 0
    right_index = len(text)-1
    # While our left index is less than our right index. It moves the pointers until they meet in the middle
    while left_index < right_index:
        # We check to see if our first and last index values are the same.
        if text[left_index].lower() == text[right_index].lower():
            #If it is, then we have a possible palindrome. We move each index to the next adjecent index.
            #Our left index will increase by 1 in order to move to the index to the right
            #Our right index will decrease by 1 in order to move to the index to the left
            right_index -= 1
            left_index += 1
        else:
            return False

    return True


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    pass
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests

    if left is None and right is None:
        left = 0
        right = len(text)-1

    if left < right:
        if text[left] == text[right]:
            return is_palindrome_recursive(text, left+1, right-1)
        else:
            return False
    else:
        return True


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
    text = 'racecar'
    is_palindrome(text)
