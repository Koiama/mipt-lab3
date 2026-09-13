"""Средн.2: студент и вывод информации о нём."""


class Student:
    """Студент с именем и номером группы."""

    def __init__(self, name: str, group: str) -> None:
        for label, value in (("имя", name), ("группа", group)):
            if not isinstance(value, str):
                raise TypeError(f"{label} должно быть строкой")
            if not value.strip():
                raise ValueError(f"{label} не должно быть пустым")
        self.name = name.strip()
        self.group = group.strip()

    def info(self) -> str:
        return f"{self.name}, группа {self.group}"

    def show_info(self) -> None:
        print(self.info())


if __name__ == "__main__":
    Student("Ксения Грозная", "221141").show_info()
