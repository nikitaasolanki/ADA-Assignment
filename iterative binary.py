import unittest
from binary_search import iterative_binary_search

class TestBinarySearch(unittest.TestCase):

    numbers = [2, 3, 6, 12, 31, 34, 75]

    def test_iterative_binary_search_with_numeric_list(self):
        self.assertEqual(iterative_binary_search(0, len(self.numbers) - 1, self.numbers, 2), 0)
        self.assertEqual(iterative_binary_search(0, len(self.numbers) - 1, self.numbers, 3), 1)
        self.assertEqual(iterative_binary_search(0, len(self.numbers) - 1, self.numbers, 6), 2)
        self.assertEqual(iterative_binary_search(0, len(self.numbers) - 1, self.numbers, 12), 3)
        self.assertEqual(iterative_binary_search(0, len(self.numbers) - 1, self.numbers, 31), 4)
        self.assertEqual(iterative_binary_search(0, len(self.numbers) - 1, self.numbers, 34), 5)
        self.assertEqual(iterative_binary_search(0, len(self.numbers) - 1, self.numbers, 75), 6)
        self.assertEqual(iterative_binary_search(0, len(self.numbers) - 1, self.numbers, 76), -1)

if __name__ == '__main__':
    unittest.main()
