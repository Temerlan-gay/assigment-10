import unittest
import hw_bonus


class TestFunctions(unittest.TestCase):

    def test_memoized_fibonacci(self):
        self.assertEqual(hw_bonus.memoized_fibonacci(10), 55)
        self.assertEqual(hw_bonus.memoized_fibonacci(20), 6765)
        self.assertEqual(hw_bonus.memoized_fibonacci(0), 0)
        self.assertEqual(hw_bonus.memoized_fibonacci(1), 1)

    def test_curry(self):
        def add(a, b, c):
            return a + b + c

        f = hw_bonus.curry(add, 5, 6)
        self.assertEqual(f(7), 18)

    def test_my_zip(self):
        self.assertEqual(
            list(hw_bonus.my_zip([1, 2, 3], [4, 5, 6])),
            [(1, 4), (2, 5), (3, 6)]
        )

    def test_recursive_flatten(self):
        self.assertEqual(
            hw_bonus.recursive_flatten([1, [2, [3, 4], 5]]),
            [1, 2, 3, 4, 5]
        )


if __name__ == "__main__":
    unittest.main()