#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    pass
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    first_index = 0
    last_index = len(array)-1


    while first_index <= last_index:
        middle_pointer_tracker = (last_index + first_index) // 2
        middle_pointer_value = array[middle_pointer_tracker]
        if middle_pointer_value == item:
            return middle_pointer_tracker
        elif middle_pointer_value < item:
            first_index = middle_pointer_tracker + 1
        else:
            last_index = middle_pointer_tracker - 1
    return None



def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
    if left is None:
        left = 0
        right = len(array) - 1

    if left > right:
        return None

    middle_index = (left + right) // 2
    middle_value = array[middle_index]

    if middle_value == item:
        return middle_index
    elif middle_value < item:
        left = middle_index + 1
        return binary_search_recursive(array, item, left, right)
    elif middle_value > item:
        right = middle_index - 1
        return binary_search_recursive(array, item, left, right)
