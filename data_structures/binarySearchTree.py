from nodes import BinaryTreeNode


class BST:
    def __init__(self):
        root = None

    def isEmpty(self):
        return self.root is None

    def size(self):
        pass

    def add(self, elem):
        self.addRecursively(self.root, elem)

    # private function to recursively add element
    def addRecursively(self, node, elem):
        pass

    def remove(self, elem):
        pass

    # private function to recursively remove element
    def removeRecursively(self, node, elem):
        pass

    def findMin(self):
        pass

    def findMax(self):
        pass

    def contains(self, elem):
        pass

    # private function to recursively search for element
    def containsRecursively(self, node, elem):
        pass

    def height(self):
        pass

    def traverse(self, order):
        pass
