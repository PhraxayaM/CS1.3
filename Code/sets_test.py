from sets import Set
import unittest

class TestSetOperations(unittest.TestCase):

    def test_init(self):
        set = Set(6)
        assert len(set.buckets) == 6
        assert set.size == 0

    def test_size(self):
        set = Set()
        set.add('A')
        assert set.size == 1
        set.add('B')
        assert set.size == 2
        set.add('C')
        set.add('D')
        set.add('E')
        assert set.size == 4

    def test_contains(self):
        set = Set()
        set.add('A')
        assert set.contains('A') == True
        set.add('B')
        assert set.contains('B') == True
        set.add('C')
        assert set.contains('D') == False

    def test_delete(self):
        set = Set()
        set.add('A')
        set.add('B')
        set.add('C')
        assert set.size == 3
        set.delete('B')
        assert set.contains('B') == False
        set.delete('A')
        assert set.contains('A') == False
        assert set.contains('C') == True
        assert set.size == 1

    def test_is_subset(self):
        set1 = Set(8, ['A', 'B', 'C', 'D'])
        set2 = Set(8, ['C', 'D'])
        assert set2.is_subset(set1)

        set3 = Set(8, ['A', 'B', 'C', 'D'])
        set4 = Set(8, ['E', 'F'])
        assert set4.is_subset(set3) == False

        set5 = Set(8, ['R', 'A', 'C', 'E'])
        set6 = Set(8, ['R', 'A', 'C', 'K'])
        assert set6.is_subset(set5) == False


    def test_union(self):
        set1 = Set(8, ['A', 'B', 'C'])
        set2 = Set(8, ['D', 'E', 'F', 'A'])
        new_set = set1.union(set2)

        assert set1.is_subset(new_set)
        assert set2.is_subset(new_set)
        assert new_set.size == 6

        set3 = Set(8, ['Z', 'T', 'R'])
        set4 = Set(8, ['V', 'E', 'G', 'A'])
        new_set2 = set3.union(set4)

        assert set3.is_subset(new_set2)
        assert set4.is_subset(new_set2)
        assert new_set2.size == 7

        set5 = Set(8, ['R', 'A', 'C', 'E'])
        set6 = Set(8, ['B', 'A', 'S', 'E'])
        new_set3 = set5.union(set6)

        assert set5.is_subset(new_set3)
        assert set6.is_subset(new_set3)
        assert new_set3.size == 6

    def test_intersection(self):
        set1 = Set(8, ['A', 'B', 'C', 'D'])
        set2 = Set(8, ['C', 'D', 'E'])
        new_set = set1.intersection(set2)

        self.assertCountEqual(new_set.keys(), ['C', 'D'])
        assert new_set.size == 2

        set3 = Set(8, ['R', 'A', 'C', 'E'])
        set4 = Set(8, ['A', 'C', 'E', 'D'])
        new_set2 = set3.intersection(set4)

        self.assertCountEqual(new_set2.keys(), ['A', 'C', 'E'])
        assert new_set2.size == 3

        set5 = Set(8, ['W', 'A', 'T', 'E', 'R'])
        set6 = Set(8, ['M', 'A', 'T', 'E'])
        new_set3 = set5.intersection(set6)

        self.assertCountEqual(new_set3.keys(), ['A', 'T', 'E'])
        assert new_set3.size == 3

    def test_difference(self):
        set1 = Set(8, ['A', 'B', 'C', 'D'])
        set2 = Set(8, ['C', 'D', 'E'])
        new_set = set1.difference(set2)

        self.assertCountEqual(new_set.keys(), ['A', 'B'])
        assert new_set.size == 2

        set3 = Set(8, ['S', 'P', 'E', 'E'])
        set4 = Set(8, ['C', 'A', 'S', 'E'])
        new_set2 = set3.difference(set4)

        self.assertCountEqual(new_set2.keys(), ['R', 'C'])
        assert new_set2.size == 2

        set5 = Set(8, ['W', 'A', 'T', 'E', 'R'])
        set6 = Set(8, ['M', 'A', 'T', 'E'])
        new_set3 = set5.difference(set6)

        self.assertCountEqual(new_set3.keys(), ['W', 'R'])
        assert new_set3.size == 2
