import unittest
import hw


class TestExercise(unittest.TestCase):

    def test_operation(self):
        def add(a, b):
            return a + b
        self.assertEqual(hw.operation(add, 2, 3), 5)
        self.assertEqual(hw.operation(add, -1, 1), 0)
        self.assertEqual(hw.operation(add, 0, 0), 0)

    def test_my_map(self):
        self.assertEqual(hw.my_map(lambda x: x**3, [1, 2, 3, 4]), [1, 8, 27, 64])
        self.assertEqual(hw.my_map(lambda x: x+2, [1, 2, 3, 4]), [3, 4, 5, 6])

    def test_filter_even_numbers(self):
        self.assertEqual(hw.filter_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 3, 5, 7, 9])
        self.assertEqual(hw.filter_even_numbers([11, 12, 13, 14, 15]), [11, 13, 15])

    def test_recursive_factorial(self):
        self.assertEqual(hw.recursive_factorial(3), 6)
        self.assertEqual(hw.recursive_factorial(4), 24)
        self.assertEqual(hw.recursive_factorial(1), 1)

    def test_compose(self):
        def plus_one(x):
            return x + 1

        def double(x):
            return x * 2

        new_func = hw.compose(plus_one, double)
        self.assertEqual(new_func(3), 8)
        self.assertEqual(new_func(0), 2)

    def test_partial(self):
        def multiply_three_numbers(a, b, c):
            return a * b * c

        multiply_by_two_and_three = hw.partial(multiply_three_numbers, 2, 3)
        self.assertEqual(multiply_by_two_and_three(4), 24)

    def test_factorial_reduce(self):
        self.assertEqual(hw.factorial_reduce(3), 6)
        self.assertEqual(hw.factorial_reduce(4), 24)

    def test_my_reduce(self):
        self.assertEqual(hw.my_reduce(lambda x, y: x+y, [1, 2, 3, 4]), 10)
        self.assertEqual(hw.my_reduce(lambda x, y: x*y, [1, 2, 3, 4]), 24)

    def test_sort_by_last_letter(self):
        self.assertEqual(
            hw.sort_by_last_letter(['apple', 'banana', 'cherry', 'date', 'grape']),
            ['banana', 'apple', 'date', 'grape', 'cherry']
        )

    def test_recursive_reverse(self):
        self.assertEqual(hw.recursive_reverse([1, 2, 3, 4, 5, 6]), [6, 5, 4, 3, 2, 1])
        self.assertEqual(hw.recursive_reverse(['a', 'b', 'c']), ['c', 'b', 'a'])

    def test_find_max(self):
        self.assertEqual(hw.find_max([1, 2, 3, 4, 5]), 5)
        self.assertEqual(hw.find_max([-1, -2, -3, -4, -5]), -1)

    def test_remove_elements(self):
        self.assertEqual(hw.remove_elements([1, 2, 3, 2, 4, 2, 5], 2), [1, 3, 4, 5])
        self.assertEqual(hw.remove_elements([1, 1, 1], 1), [])

    def test_repeat(self):
        repeat_three = hw.repeat(3)
        self.assertEqual(repeat_three("hi"), "hihihi")

    def test_recursive_sum(self):
        self.assertEqual(hw.recursive_sum([1, 2, 3, 4, 5]), 15)

    def test_add_two_lists(self):
        self.assertEqual(hw.add_two_lists([1, 2, 3], [4, 5, 6]), [5, 7, 9])


if __name__ == "__main__":
    unittest.main()