import unittest
from unionFind import UnionFind


class TestUnionFindMethods(unittest.TestCase):
    def test_unionFind_init(self):
        elements = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        uf = UnionFind(elements)
        self.assertEqual(str(uf), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_unionFind_init_set(self):
        elements = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
        uf = UnionFind(elements)
        self.assertTrue(set(uf.arr) == set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_unionFind_union(self):
        elements = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        uf = UnionFind(elements)
        uf.unify("A", "B")
        pass


if __name__ == "__main__":
    unittest.main()
