from function_for_homework_12 import (sum_two_numbers,
                                      find_h_in_text,
                                      uniq_symbols_more_than_10,
                                      average,
                                      reverse_string)
from function_for_homework_12 import find_h_in_text
from unittest.mock import patch
from function_for_homework_12 import uniq_symbols_more_than_10
import unittest

#testing sum_two_numbers
#test01-02
class TestSumFunction(unittest.TestCase):
    def test_sum_two_numbers(self):
        self.assertEqual(sum_two_numbers(1, 2), 3)

    def test_sum_two_negative_numbers(self):
            self.assertEqual(sum_two_numbers(-1, -1), -2)

#testing average
#test03-04
class TestAverage(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([1, 2, 3, 4, 5]), 3)

    def test_incorrect_average(self):
        self.assertNotEquals(average([1, 2, 3, 4, 5]), 9)

#testing reverse_string
#test05-06
class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), 'olleh')

    def test_incorrect_reverse_string(self):
        self.assertNotEquals(reverse_string("hello"), 'hello')

#testing find_h_in_text function
#test07-08
class TestFindHInText(unittest.TestCase):

    @patch('builtins.input', return_value = 'hello')
    def test_find_h_in_text(self, mock_input):
        result = find_h_in_text()
        self.assertEqual(result, "Accepted!")

    @patch('builtins.input', side_effect=['test', 'nope', 'ahoy'])
    def test_no_h_in_text(self, mock_input):
        result = find_h_in_text()
        self.assertEqual(result, "Accepted!")

#testing uniq_symbols_more_than_10
#test09-11
class TestUniqSymbolsMoreThan10 (unittest.TestCase):
    @patch('builtins.input', return_value='qwertyuiopa')
    def test_uniq_symbols_more_than_10(self, mock_input):
        result = uniq_symbols_more_than_10()
        self.assertEqual(result, True)

    @patch('builtins.input', return_value='qwe')
    def test_uniq_symbols_less_than_10(self, mock_input):
        result = uniq_symbols_more_than_10()
        self.assertEqual(result, False)

    @patch('builtins.input', return_value=' ')
    def test_empty_input(self, mock_input):
        result = uniq_symbols_more_than_10()
        self.assertEqual(result, False)