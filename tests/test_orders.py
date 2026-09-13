"""Контракт товара и корзины, сформулированный до реализации."""

import unittest
from dataclasses import FrozenInstanceError
from decimal import Decimal

from orders import Basket, Product


class ProductTests(unittest.TestCase):
    def test_price_is_exact_and_product_cannot_change(self):
        tea = Product("Чай", "119.90")
        self.assertEqual(tea.price, Decimal("119.90"))
        with self.assertRaises(FrozenInstanceError):
            tea.price = Decimal("1.00")

    def test_invalid_name_is_rejected(self):
        with self.assertRaises(ValueError):
            Product("  ", "10.00")
        with self.assertRaises(TypeError):
            Product(25, "10.00")

    def test_invalid_price_is_rejected(self):
        for price in ("-1", "1.001", "NaN", "Infinity", "abc"):
            with self.subTest(price=price):
                with self.assertRaises(ValueError):
                    Product("Товар", price)
        for price in (True, 0.1):
            with self.subTest(price=price):
                with self.assertRaises(TypeError):
                    Product("Товар", price)


class BasketTests(unittest.TestCase):
    def setUp(self):
        self.tea = Product("Чай", "119.90")
        self.bread = Product("Хлеб", "80.20")
        self.basket = Basket()

    def test_empty_basket_has_zero_total(self):
        self.assertEqual(self.basket.total, Decimal("0.00"))
        self.assertEqual(self.basket.quantity, 0)
        self.assertEqual(self.basket.lines, ())

    def test_add_merges_same_product_and_total_is_exact(self):
        self.basket.add(self.tea, 2)
        self.basket.add(self.tea)
        self.basket.add(self.bread)
        self.assertEqual(self.basket.quantity, 4)
        self.assertEqual(self.basket.lines, ((self.tea, 3), (self.bread, 1)))
        self.assertEqual(self.basket.total, Decimal("439.90"))

    def test_remove_some_then_all_updates_total(self):
        self.basket.add(self.tea, 3)
        self.basket.remove(self.tea)
        self.assertEqual(self.basket.total, Decimal("239.80"))
        self.basket.remove(self.tea, 2)
        self.assertEqual(self.basket.lines, ())
        self.assertEqual(self.basket.total, Decimal("0.00"))

    def test_remove_missing_or_too_many_preserves_state(self):
        with self.assertRaises(ValueError):
            self.basket.remove(self.tea)
        self.basket.add(self.tea, 2)
        with self.assertRaises(ValueError):
            self.basket.remove(self.tea, 3)
        self.assertEqual(self.basket.lines, ((self.tea, 2),))

    def test_invalid_quantity_or_product_preserves_state(self):
        for count in (0, -1):
            with self.subTest(count=count):
                with self.assertRaises(ValueError):
                    self.basket.add(self.tea, count)
        for count in (True, 1.5):
            with self.subTest(count=count):
                with self.assertRaises(TypeError):
                    self.basket.add(self.tea, count)
        with self.assertRaises(TypeError):
            self.basket.add("чай")
        self.assertEqual(self.basket.lines, ())

    def test_lines_are_a_snapshot(self):
        self.basket.add(self.tea)
        old_lines = self.basket.lines
        self.basket.add(self.bread)
        self.assertEqual(old_lines, ((self.tea, 1),))
        self.assertEqual(len(self.basket.lines), 2)


if __name__ == "__main__":
    unittest.main()
