import unittest
from auto_test_1_1 import full_name


class NameTestCase(unittest.TestCase):
    """Автоматическое тестирование для функции full_name(auto_test_1_1.py)."""

    def test_name_last(self):
        """Проверка ФИО по формату: 'Петров Василий'"""
        format_name = full_name("Петров", "Василий")
        self.assertEqual(format_name, "Петров Василий")

    def test_last_name_patronymic(self):
        """Проверка ФИО по формату: 'Петров Василий Васильевич'"""
        format_name = full_name("Петров", "Василий", "Васильевич", )
        self.assertEqual(format_name, "Петров Василий Васильевич")


if __name__ == "__name__":
    unittest.main()
