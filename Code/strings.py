#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    """O(n) because find all indexes is O(N)"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    """ old code
    # if pattern in text:
    #     return True
    # else:
    #     return False
    """
    found_index = find_all_indexes(text, pattern)

    if found_index == []:
        return False

    return True



def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""

    """O(n) because find all indexes is O(N)"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    found_index = find_all_indexes(text, pattern)

    if found_index == []:
        return None

    return found_index[0]



    """Old code
    # create a variable to keep track of our index
    text_index = 0
    # if our pattern is empty, we will return our text_index, which is defaulted to be set at 0
    if pattern == '':
        return text_index

    # while our text_index, which starts at 0, is not equal to the length of our text, the code will run until our
    # text_index and the length of the text we are passing in are the same.
    while text_index != len(text):
        We are iterating through our pattern. For example, if the pattern is 'abc', 'i' will become 'a' and then loop through
            the whole if statements below it. Once the if statements have been completed, 'i' then becomes 'b' and it loops again
            through the whole if statements.

        for i in range(len(pattern)):
            #if our text_index, which is currently at [0] plus our 'i', which starts at [0] is less than the length of our text
            #For example, it will be 0 + 0, followed by 0 + 1, then 0 + 2, until it is no longer less than the length of our text
            if text_index + i < len(text):
                # The first character(index 0) of both the text and the pattern need to match
                # For example, text is = 'abc' and pattern is = 'ab'
                # First iteration will be value at index 0, this is because text[0 + 0] will give you text[0] and unwraps the value
                # so it is if 'a' is not equal to 'a' break the loop
                if text[text_index + i] != pattern[i]:
                    break
                if i == len(pattern) - 1:
                    return text_index
        text_index += 1
"""


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""

    """O(n) because we are enumerating through each index"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    indices = []
    #enumerate over the text we are passing. enumerating the text gives each text a value starting at 0, just like indexes
    #
    for index, _ in enumerate(text):
        if pattern == text[index: (index + len(pattern))]:
            print('find_all_index is:' + text[index: (index + len(pattern))])
            indices.append(index)

    return indices



def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
