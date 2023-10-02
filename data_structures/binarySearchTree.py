from nodes import BinaryTreeNode


class BST:
    def __init__(self):
        self.root = None
        self.nodeCount = 0

    def isEmpty(self):
        return self.root is None

    def size(self):
        return self.nodeCount

    def add(self, elem):
        # if contains already, do not add
        if self.contains(elem):
            return False

        # recurse
        self.root = self.addRecursively(self.root, elem)
        self.nodeCount += 1

    # private function to recursively add element
    def addRecursively(self, node, elem):
        # Null node found, place child
        if node is None:
            return BinaryTreeNode(elem)

        if elem < node.value:
            node.left = self.addRecursively(node.left, elem)
            return node

        node.right = self.addRecursively(node.right, elem)
        return node

    def remove(self, elem):
        pass

    # private function to recursively remove element
    def removeRecursively(self, node, elem):
        pass

    def findMin(self):
        if self.root is None:
            return None

        # keep going left
        node = self.root
        while node.left:
            node = node.left

        return node.value

    def findMax(self):
        if self.root is None:
            return None

        # keep going right
        node = self.root
        while node.right:
            node = node.right

        return node.value

    def contains(self, elem):
        return self.containsRecursively(self.root, elem)

    # private function to recursively search for element
    def containsRecursively(self, node, elem):
        # null node reached
        if node is None:
            return False

        # comparisons
        # equal
        if node.value == elem:
            return True
        # node less than elem, recurse right
        elif node.value < elem:
            return self.containsRecursively(node.right, elem)
        # node greater than elem, recurse left
        return self.containsRecursively(node.left, elem)

    def height(self):
        return self.heightRecursively(self.root)

    def heightRecursively(self, node):
        if node is None:
            return 0
        return (
            max(
                self.heightRecursively(node.left),
                self.heightRecursively(node.right),
            )
            + 1
        )

    def traverse(self, order):
        pass
