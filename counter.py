"""Средн.8: счётчик с увеличением и уменьшением."""


class Counter:
    """Целочисленный счётчик с доступным для чтения значением."""

    def __init__(self, start: int = 0) -> None:
        if type(start) is not int:
            raise TypeError("начальное значение должно быть целым числом")
        self._value = start

    @property
    def value(self) -> int:
        """Текущее значение счётчика."""
        return self._value

    def increment(self, amount: int = 1) -> int:
        self._check_amount(amount)
        self._value += amount
        return self._value

    def decrement(self, amount: int = 1) -> int:
        self._check_amount(amount)
        self._value -= amount
        return self._value

    @staticmethod
    def _check_amount(amount: int) -> None:
        if type(amount) is not int:
            raise TypeError("шаг должен быть целым числом")
        if amount <= 0:
            raise ValueError("шаг должен быть положительным")


if __name__ == "__main__":
    counter = Counter(3)
    print("Начало:", counter.value)
    print("После увеличения на 4:", counter.increment(4))
    print("После уменьшения на 2:", counter.decrement(2))
