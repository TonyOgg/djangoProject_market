import unittest

def alls(a, b):
    c = []
    for i in a:
        if i in b:
            c.append(i)
    return c

class Tests(unittest.TestCase):
    def test_alls(self):
        res = alls([1, 3, 5], [2, 4, 5])
        self.assertTrue(res == [5])

def dubles(a):
    no_dubles = list(set(a))
    return no_dubles

class Test(unittest.TestCase):
    def test_dubles(self):
        res = dubles([1, 3, 5, 5, 7, 8, 8])
        self.assertTrue(res == [1, 3, 5, 7, 8])


if __name__ == '__main__':
    unittest.main()
