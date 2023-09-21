import unittest
from lab1 import find_unsorted_subarray


class TestFindUnsortedSubarray(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(find_unsorted_subarray([-3, -1, 3, 4, 7]), (-1, -1))

    def test_sort_whole_array(self):
        self.assertEqual(find_unsorted_subarray([5, 1, 8, 2, 3]), (0, 4))

    def test_single_element_array(self):
        self.assertEqual(find_unsorted_subarray([7]), (-1, -1))

    def test_unsorted_array(self):
        self.assertEqual(find_unsorted_subarray([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), (3, 9))


if __name__ == '__main__':
    unittest.main()
