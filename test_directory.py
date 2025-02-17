import unittest

# Предположим, у вас есть модуль `my_module.py`, где определена функция `add`.
from my_module import add


class TestMyModule(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)  # Проверка сложения
        self.assertEqual(add(-1, 1), 0)  # Проверка сложения с отрицательным числом
        self.assertEqual(add(0, 0), 0)  # Проверка сложения нуля

    def test_add_with_floats(self):
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)  # Проверка сложения с плавающими точками


if __name__ == '__main__':
    unittest.main()