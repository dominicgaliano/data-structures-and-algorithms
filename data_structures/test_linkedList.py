import unittest
from linkedList import SinglyLinkedList


class TestSinglyLinkedListMethods(unittest.TestCase):
    def test_append(self):
        testList = SinglyLinkedList()
        testList.append(10)
        testList.append(10)
        testList.append(10)
        self.assertEqual(str(testList), "10 10 10")

    def test_insertAt(self):
        testList = SinglyLinkedList()
        testList.append(1)
        testList.append(2)
        testList.append(3)
        testList.insertAt(3, 4)
        self.assertEqual(str(testList), "1 2 4 3")

    def test_insertAt_empty(self):
        testList = SinglyLinkedList()
        testList.insertAt(1, 2)
        self.assertEqual(str(testList), "")

    def test_insertAt_notFound(self):
        testList = SinglyLinkedList()
        testList.append(1)
        testList.append(1)
        testList.append(1)
        testList.insertAt(2, 3)
        self.assertEqual(str(testList), "1 1 1")


if __name__ == "__main__":
    unittest.main()