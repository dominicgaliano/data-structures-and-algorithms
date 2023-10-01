import unittest
from queue import Queue


class TestSinglyLinkedListMethods(unittest.TestCase):
    def test_enqueue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEquals(str(q), "1 2 3")

    def test_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        removedElement = q.dequeue()
        self.assertEquals(str(q), "2 3")
        self.assertEquals(removedElement, 1)

    def test_dequeue_empty(self):
        q = Queue()
        removedElement = q.dequeue()
        self.assertEquals(str(q), "")
        self.assertEquals(removedElement, None)


if __name__ == "__main__":
    unittest.main()
