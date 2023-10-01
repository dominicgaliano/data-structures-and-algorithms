import unittest
from linkedList import SinglyLinkedList


class TestSinglyLinkedListMethods(unittest.TestCase):
    def test_append(self):
        testList = SinglyLinkedList()
        testList.append(10)
        testList.append(10)
        testList.append(10)
        self.assertEqual(str(testList), "10 10 10")


if __name__ == "__main__":
    unittest.main()
