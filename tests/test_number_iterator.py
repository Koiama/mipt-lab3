"""Контракт класса-итератора, сформулированный до реализации."""

import unittest

from number_iterator import NumberIterator


class NumberIteratorTests(unittest.TestCase):
    def test_ascending_sequence_excludes_stop(self):
        self.assertEqual(list(NumberIterator(1, 6)), [1, 2, 3, 4, 5])
        self.assertEqual(list(NumberIterator(1, 8, 3)), [1, 4, 7])

    def test_descending_sequence(self):
        self.assertEqual(list(NumberIterator(5, -1, -2)), [5, 3, 1])

    def test_empty_range(self):
        self.assertEqual(list(NumberIterator(4, 4)), [])
        self.assertEqual(list(NumberIterator(4, 0)), [])

    def test_iterator_is_its_own_cursor_and_stays_exhausted(self):
        numbers = NumberIterator(2, 4)
        self.assertIs(iter(numbers), numbers)
        self.assertEqual(next(numbers), 2)
        self.assertEqual(list(numbers), [3])
        for _ in range(2):
            with self.assertRaises(StopIteration):
                next(numbers)

    def test_zero_step_is_rejected(self):
        with self.assertRaises(ValueError):
            NumberIterator(0, 3, 0)

    def test_non_integer_argument_is_rejected(self):
        with self.assertRaises(TypeError):
            NumberIterator(0, 3, True)
        with self.assertRaises(TypeError):
            NumberIterator("0", 3)


if __name__ == "__main__":
    unittest.main()
