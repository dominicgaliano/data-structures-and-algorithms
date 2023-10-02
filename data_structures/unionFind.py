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

    def __str__(self):
        return str(self.arr)

    def unify(self, A, B):
        pass

    def find(self, A):
        pass

    def connected(self, A, B):
        pass

    def componentSize(self, A):
        pass

    def size(self):
        pass

    def components(self):
        pass
