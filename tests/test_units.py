import unittest
from unittest.mock import Mock, patch
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from main import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.mock_master = Mock()
        with patch('tkinter.Entry'), patch('tkinter.Label'), patch('tkinter.Button'):
            self.calc = SimpleCalculator(self.mock_master)
            self.calc.entry1 = Mock()
            self.calc.entry2 = Mock()
            self.calc.result_label = Mock()

    def test_add(self):
        self.calc.entry1.get.return_value = "5"
        self.calc.entry2.get.return_value = "3"
        self.calc.add()
        self.calc.result_label.config.assert_called_with(text="Результат: 8.0")

    def test_subtract(self):
        self.calc.entry1.get.return_value = "5"
        self.calc.entry2.get.return_value = "2"
        self.calc.subtract()
        self.calc.result_label.config.assert_called_with(text="Результат: 3.0")

    def test_multiply(self):
        self.calc.entry1.get.return_value = "4"
        self.calc.entry2.get.return_value = "3"
        self.calc.multiply()
        self.calc.result_label.config.assert_called_with(text="Результат: 12.0")

    def test_divide(self):
        self.calc.entry1.get.return_value = "10"
        self.calc.entry2.get.return_value = "2"
        self.calc.divide()
        self.calc.result_label.config.assert_called_with(text="Результат: 5.0")

    def test_divide_by_zero(self):
        self.calc.entry1.get.return_value = "10"
        self.calc.entry2.get.return_value = "0"
        with patch('tkinter.messagebox.showerror') as mock_msg:
            self.calc.divide()
            mock_msg.assert_called_with("Помилка", "Ділення на нуль!")

    def test_invalid_input(self):
        self.calc.entry1.get.return_value = "abc"
        self.calc.entry2.get.return_value = "3"
        with patch('tkinter.messagebox.showerror') as mock_msg:
            num1, num2 = self.calc.get_inputs()
            self.assertIsNone(num1)
            mock_msg.assert_called_with("Помилка", "Введіть коректні числа")

if __name__ == '__main__':
    unittest.main()
