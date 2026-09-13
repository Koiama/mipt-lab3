"""Повыш.3: товары и корзина с точным расчётом стоимости."""

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation


_CENT = Decimal("0.01")


@dataclass(frozen=True, slots=True, init=False)
class Product:
    """Неизменяемый товар с ценой в рублях и копейках."""

    name: str
    price: Decimal

    def __init__(self, name: str, price: Decimal | int | str) -> None:
        if not isinstance(name, str):
            raise TypeError("название должно быть строкой")
        if not name.strip():
            raise ValueError("название не должно быть пустым")
        if type(price) not in (Decimal, int, str):
            raise TypeError("цену передавайте целым числом, строкой или Decimal")
        try:
            amount = Decimal(price)
            if not amount.is_finite() or amount < 0 or amount != amount.quantize(_CENT):
                raise ValueError("цена должна быть неотрицательной, с точностью до копейки")
            amount = amount.quantize(_CENT)
        except InvalidOperation as error:
            raise ValueError("цена должна быть числом с точностью до копейки") from error
        object.__setattr__(self, "name", name.strip())
        object.__setattr__(self, "price", amount)


class Basket:
    """Корзина: складывает одинаковые товары и пересчитывает итог."""

    def __init__(self) -> None:
        self._lines: dict[Product, int] = {}

    @property
    def lines(self) -> tuple[tuple[Product, int], ...]:
        """Снимок позиций в порядке их добавления."""
        return tuple(self._lines.items())

    @property
    def quantity(self) -> int:
        """Общее количество единиц товара."""
        return sum(self._lines.values())

    @property
    def total(self) -> Decimal:
        """Стоимость всех позиций в рублях."""
        return sum((item.price * count for item, count in self._lines.items()), Decimal("0.00"))

    def add(self, product: Product, count: int = 1) -> None:
        self._check_product(product)
        self._check_count(count)
        self._lines[product] = self._lines.get(product, 0) + count

    def remove(self, product: Product, count: int = 1) -> None:
        self._check_product(product)
        self._check_count(count)
        available = self._lines.get(product, 0)
        if available < count:
            raise ValueError("в корзине недостаточно выбранного товара")
        if available == count:
            del self._lines[product]
        else:
            self._lines[product] = available - count

    @staticmethod
    def _check_product(product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("ожидается объект Product")

    @staticmethod
    def _check_count(count: int) -> None:
        if type(count) is not int:
            raise TypeError("количество должно быть целым числом")
        if count <= 0:
            raise ValueError("количество должно быть положительным")


if __name__ == "__main__":
    basket = Basket()
    basket.add(Product("Чай", "119.90"), 2)
    basket.add(Product("Хлеб", "80.20"))
    for item, count in basket.lines:
        print(f"{item.name}: {count} × {item.price:.2f} ₽")
    print(f"Итого: {basket.total:.2f} ₽")
