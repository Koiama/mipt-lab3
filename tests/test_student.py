"""Поведение класса студента, сформулированное до реализации."""

import io
import unittest
from contextlib import redirect_stdout

from student import Student


class StudentTests(unittest.TestCase):
    def test_information_contains_name_and_group(self):
        student = Student("Ксения Грозная", "221141")
        self.assertEqual(student.info(), "Ксения Грозная, группа 221141")

    def test_show_info_writes_readable_line(self):
        output = io.StringIO()
        with redirect_stdout(output):
            Student("Анна", "221141").show_info()
        self.assertEqual(output.getvalue(), "Анна, группа 221141\n")

    def test_blank_name_or_group_is_rejected(self):
        for name, group in ((" ", "221141"), ("Анна", "")):
            with self.subTest(name=name, group=group):
                with self.assertRaises(ValueError):
                    Student(name, group)

    def test_non_string_name_is_rejected(self):
        with self.assertRaises(TypeError):
            Student(42, "221141")


if __name__ == "__main__":
    unittest.main()
