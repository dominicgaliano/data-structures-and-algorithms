import unittest
from linkedList import SinglyLinkedList


class TestSinglyLinkedListMethods(unittest.TestCase):
    def test_append(self):
        testList = SinglyLinkedList()
        testList.append(10)
        testList.append(10)
        testList.append(10)
        self.assertEqual(str(testList), "10 10 10")

    def test_append_change_head_tail(self):
        testList = SinglyLinkedList()
        insertedNode = testList.append(1)
        self.assertEqual(insertedNode, testList.head)
        self.assertEqual(insertedNode, testList.tail)

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

    def test_deleteAt(self):
        testList = SinglyLinkedList()
        testList.append(1)
        testList.append(2)
        testList.append(3)
        testList.deleteAt(2)
        self.assertEqual(str(testList), "1 3")

    def test_deleteAt_empty(self):
        testList = SinglyLinkedList()
        deletedNode = testList.deleteAt(2)
        self.assertEqual(deletedNode, None)
        self.assertEqual(str(testList), "")

    def test_deleteAt_notFound(self):
        testList = SinglyLinkedList()
        testList.append(1)
        testList.append(2)
        testList.append(3)
        deletedNode = testList.deleteAt(10)
        self.assertEqual(deletedNode, None)
        self.assertEqual(str(testList), "1 2 3")

    def test_prepend(self):
        testList = SinglyLinkedList()
        testList.prepend(1)
        testList.prepend(2)
        insertedNode = testList.prepend(3)
        self.assertEqual(insertedNode, testList.head)
        self.assertEqual(str(testList), "3 2 1")

    def test_prepend_change_head_tail(self):
        testList = SinglyLinkedList()
        insertedNode = testList.prepend(1)
        self.assertEqual(insertedNode, testList.head)
        self.assertEqual(insertedNode, testList.tail)


if __name__ == "__main__":
    unittest.main()
