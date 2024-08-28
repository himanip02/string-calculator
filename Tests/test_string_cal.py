import unittest
from src.str_cal import add

class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(""), 0)
    def test_single_number(self):
        self.assertEqual(add("1"), 1)
    def test_two_numbers(self):
        self.assertEqual(add("1,2"), 3)
    def test_newline_separator(self):
        self.assertEqual(add("1\n2,3"), 6)
    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)
    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as error:
            add("1,-2,3,-4")
        self.assertEqual(str(error.exception), "Negative numbers are not allowed: -2, -4")
    def test_custom_del(self):
        self.assertEqual(add("//|\n1|2"),3)
