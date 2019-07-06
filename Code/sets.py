from hashtable import HashTable
from linkedlist import LinkedList, Node

class Set(HashTable):

    def __init__(self, init_size=8, elements=None):
        super(Set, self).__init__(init_size)
        if elements is not None:
            for element in elements:
                self.add(element)

    def contains(self, element):
        """return true or false if the element is found. O(1)"""
        return super(Set, self).contains(element)


    def add(self, element):
        """if the element exists, delete it and add it in. If it doesn't exist, add it O(n)"""
        if self.contains(element) == False:
            self.set(element, None)


    def remove(self, element):
        """Remove element from the set O(1)"""
        self.delete(element)

    def union(self, other_set):
        """Returns a new set that is made from combing the first and second set O(n*m)"""
        new_set = Set()

        for item in self.keys():
            new_set.add(item)

        for item in other_set.keys():
            new_set.add(item)

        return new_set

    def difference(self, other_set):
        """Returns a new set that only contains unique values from both sets O(n)"""
        new_set = Set()

        for item in self.keys():
            if not other_set.contains(item):
                new_set.add(item)

        return new_set

    def intersection(self, other_set):
        """Take the elements that are shared by both sets and return them in a new set O(n)"""
        new_set = Set()

        for item in self.keys():
            if other_set.contains(item):
                new_set.add(item)

        return new_set

    def is_subset(self, other_set):
        """Checks to see if every element in this set is also into the other set
        Time Complexity: O(n)"""

        for item in self.keys():
            if not other_set.contains(item):
                return False

        return True


set = Set()
set.add('A')
set.add('B')
set.add('C')
set.add('F')

set2 = Set()
set2.add('B')
set2.add('E')
set2.add('F')
set2.add('G')

set3 = Set()
set3.add('B')
set3.add('Z')

print(set)
print(set2)

union_test = set.union(set2)
difference_test = set.difference(set2)
intersection_test = set.intersection(set2)

print(union_test)
print(difference_test)
print(intersection_test)
print(set3.is_subset(set))
