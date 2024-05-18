import unittest
import binarySearchHelper from 003.py

class TestBinarySearch(unittest.TestCase):

    def test_empty_list(self):
        lst = []
        elt = 10
        index = binarySearchHelper(lst, elt, 0, len(lst) - 1)
        self.assertIsNone(index)

    def test_element_not_found(self):
        lst = [1, 3, 5, 7, 9]
        elt = 8
        index = binarySearchHelper(lst, elt, 0, len(lst) - 1)
        self.assertIsNone(index)

    def test_element_found_at_beginning(self):
        lst = [1, 3, 5, 7, 9]
        elt = 1
        index = binarySearchHelper(lst, elt, 0, len(lst) - 1)
        self.assertEqual(index, 0)

    def test_element_found_at_end(self):
        lst = [1, 3, 5, 7, 9]
        elt = 9
        index = binarySearchHelper(lst, elt, 0, len(lst) - 1)
        self.assertEqual(index, 4)

    def test_element_found_in_middle(self):
        lst = [1, 3, 5, 7, 9]
        elt = 5
        index = binarySearchHelper(lst, elt, 0, len(lst) - 1)
        self.assertEqual(index, 2)

    def test_duplicate_elements(self):
        lst = [1, 3, 5, 5, 7, 9]
        elt = 5
        index = binarySearchHelper(lst, elt, 0, len(lst) - 1)
        self.assertEqual(index, 2)  # Returns the first occurrence

if __name__ == "__main__":
    unittest.main()
