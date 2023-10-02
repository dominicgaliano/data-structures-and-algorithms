class UnionFind:
    def __init__(self, elements):
        try:
            iter(elements)
        except TypeError as te:
            print(elements, "is not iterable")

        self.map = dict()
        self.arr = [i for i in range(len(elements))]
        i = 0
        for element in elements:
            self.map["element"] = i
            i += 1
        self.numComponents = i - 1

    def __str__(self):
        return str(self.arr)

    def unify(self, A, B):
        rootA = self.find(A)
        rootB = self.find(B)

        if rootA != rootB:
            self.arr[rootA] = self.arr[rootB]
            self.numComponents -= 1

    def find(self, A):
        i = self.map(A)
        parent = self.arr[i]

        while i != parent:
            i = parent
            parent = self.arr[i]

        return i

    def connected(self, A, B):
        if A not in self.map or B not in self.map:
            raise KeyError()

        return self.find(A) == self.find(B)

    def componentSize(self, A):
        if A not in self.map:
            raise KeyError()

        n = 0
        i = self.map[A]
        parent = self.arr[i]

        while i != parent:
            n += 1
            i = parent
            parent = self.arr[i]

        return n

    def components(self):
        return self.numComponents
