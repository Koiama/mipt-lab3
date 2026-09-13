"""Поведение счётчика, сформулированное до реализации."""

import unittest

from counter import Counter


class CounterTests(unittest.TestCase):
    def test_increase_and_decrease_return_new_value(self):
        counter = Counter(3)
        self.assertEqual(counter.increment(), 4)
        self.assertEqual(counter.increment(4), 8)
        self.assertEqual(counter.decrement(2), 6)
        self.assertEqual(counter.value, 6)

    def test_counter_can_go_below_zero(self):
        counter = Counter()
        self.assertEqual(counter.decrement(), -1)

    def test_invalid_start_is_rejected(self):
        for value in (True, 1.5, "1"):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    Counter(value)

    def test_non_positive_or_non_integer_step_is_rejected_without_mutation(self):
        counter = Counter(5)
        for step in (0, -1):
            with self.subTest(step=step):
                with self.assertRaises(ValueError):
                    counter.increment(step)
        with self.assertRaises(TypeError):
            counter.decrement(True)
        self.assertEqual(counter.value, 5)


if __name__ == "__main__":
    unittest.main()
