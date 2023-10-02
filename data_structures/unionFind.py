class UnionFind:
    def __init__(self, elements):
        try:
            iter(elements)
        except TypeError as te:
            raise TypeError

        if len(elements) <= 0:
            raise IndexError

        self.map = dict()
        self.arr = [i for i in range(len(elements))]
        i = 0
        for element in elements:
            self.map[element] = i
            i += 1
        self.numComponents = i

    def __str__(self):
        return str(self.arr)

    def unify(self, A, B):
        """Combines components containing A and B"""
        rootA = self.find(A)
        rootB = self.find(B)

        if rootA != rootB:
            self.arr[rootA] = self.arr[rootB]
            self.numComponents -= 1

    def find(self, A):
        """Returns index of parent of element 'A'"""
        root = self.map[A]

        while root != self.arr[root]:
            root = self.arr[root]

        # path compression
        # root is now found, now travel from A to root again
        # pointing the nodes reached to the root
        i = self.map[A]
        while i != root:
            nextElement = self.arr[i]
            self.arr[i] = root
            i = nextElement

        return root

    def connected(self, A, B):
        """Returns true if A and B are in the same component"""
        if A not in self.map or B not in self.map:
            raise KeyError

        return self.find(A) == self.find(B)

    def componentSize(self, A):
        """Returns size of component containing element 'A'"""
        if A not in self.map:
            raise KeyError

        A_parent = self.find(A)
        count = 0
        for element in self.map.keys():
            parent = self.find(element)
            if parent == A_parent:
                count += 1

        return count

    def components(self):
        """Returns total number of components"""
        return self.numComponents
