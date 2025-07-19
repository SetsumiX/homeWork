import unittest

class AnyFunc:
    @staticmethod
    def _add(a, b):
        return a + b

    @staticmethod
    def _sum(*args):
        lst = []
        cnt = 0
        for k, v in enumerate(args):
            cnt += 1
            lst.append(v)
        return sum(lst)/cnt

    @staticmethod
    def _max(*args):
        lst = []
        for v in args:
            lst.append(v)
        return max(lst)

    @staticmethod
    def _min(*args):
        lst = []
        for v in args:
            lst.append(v)
        return min(lst)

class TestAnyFunc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(AnyFunc._add(2, 3), 5)
        self.assertEqual(AnyFunc._add(-1, 1), 0)
        self.assertEqual(AnyFunc._add(0, 0), 0)

    def test_sum(self):
        self.assertEqual(AnyFunc._sum(2, 2), 2)
        self.assertAlmostEqual(AnyFunc._sum(2, 3, 4, 5), 3.5, places=6)
        self.assertAlmostEqual(AnyFunc._sum(-2, -3, -4, -5), -3.5, places=6)

    def test_max(self):
        self.assertEqual(AnyFunc._max(2, 4, 1, 7), 7)
        self.assertEqual(AnyFunc._max(-6, -3, -1), -1)

    def test_min(self):
        self.assertEqual(AnyFunc._min(2, 4, 1, 7), 1)
        self.assertEqual(AnyFunc._min(-6, -3, -1), -6)

if __name__ == "__main__":
    unittest.main()