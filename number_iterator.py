"""Средн.10: итератор по целым числам с заданным шагом."""


class NumberIterator:
    """Однопроходный итератор целых чисел до stop, не включая stop."""

    def __init__(self, start: int, stop: int, step: int = 1) -> None:
        for name, value in (("start", start), ("stop", stop), ("step", step)):
            if type(value) is not int:
                raise TypeError(f"{name} должен быть целым числом")
        if step == 0:
            raise ValueError("step не должен быть равен нулю")
        self._current = start
        self._stop = stop
        self._step = step

    def __iter__(self) -> "NumberIterator":
        return self

    def __next__(self) -> int:
        if self._step > 0 and self._current >= self._stop:
            raise StopIteration
        if self._step < 0 and self._current <= self._stop:
            raise StopIteration
        value = self._current
        self._current += self._step
        return value


if __name__ == "__main__":
    print("По возрастанию:", list(NumberIterator(1, 6)))
    print("По убыванию:", list(NumberIterator(5, -1, -2)))
