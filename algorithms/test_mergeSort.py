import unittest
from mergeSort import mergeSort


class TestMergeSortMethods(unittest.TestCase):
    def test_sortList(self):
        lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        sortedList = mergeSort(lst)
        lst = lst.copy()
        lst.sort()
        self.assertEqual(lst, sortedList)

    def test_emptyList(self):
        lst = []
        sortedList = mergeSort(lst)
        self.assertEqual(sortedList, [])

    def test_sort_oddIndexList(self):
        lst = [2, 3, 1]
        sortedList = mergeSort(lst)
        lst = lst.copy()
        lst.sort()
        self.assertEqual(lst, sortedList)


if __name__ == "__main__":
    unittest.main()
