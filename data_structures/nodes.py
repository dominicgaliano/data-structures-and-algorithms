class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class BidirectionalNode(Node):
    def __init__(self, value, prev=None, next=None):
        super().__init__(value, next)
        self.prev = prev
