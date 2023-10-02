class PQueue:
    def __init__(self):
        self.heap = []
        self.heapSize = 0

    def __str__(self):
        return str(self.heap)

    def isEmpty(self):
        return self.heapSize == 0

    def clear(self):
        self.heap = []

    def heapify(self):
        """O(n) efficient heap formation"""
        raise NotImplementedError("Not implemented for time sake")

    def size(self):
        return self.heapSize

    def peek(self):
        if self.isEmpty():
            return None
        return self.heap[0]

    def poll(self):
        return self.removeAt(0)

    def contains(self, element):
        for heapElement in self.heap:
            if element == heapElement:
                return True
        return False

    def removeAt(self, index):
        pass

    def add(self, element):
        if element is None:
            raise TypeError("Element cannot be None")

        self.heap.append(element)
        self.swim(self.heapSize)
        self.heapSize += 1

    def swim(self, k):
        # bottom up node swim, O(log(n))
        parent = (k - 1) // 2
        while k > 0 and self.less(k, parent):
            # bubble up
            self.heap[k], self.heap[parent] = self.heap[parent], self.heap[k]
            k = parent

            # recalculate parent
            parent = (k - 1) // 2

    def less(self, i, j):
        return self.heap[i] <= self.heap[j]
