import unittest
import re


class Functions(unittest.TestCase):
    def test_parameters(self):
        self.assertEqual("Greater", function_parameters(34, 33))
        self.assertEqual("Greater", function_parameters(34))
        self.assertEqual(None, function_parameters(34, 34))
        self.assertEqual("Less", function_parameters(34, 35))

    def test_multiple_return_values(self):
        self.assertEqual((5, 6, 7), function_multiple_return_values_tuple())
        self.assertEqual({'a': 5, 'b': 6, 'c': 7}, function_multiple_return_values_dict())

    def test_regular_expressions(self):
        self.assertEqual('Alabama', function_str_string('  Alabama  '))
        self.assertEqual('Georgia', function_remove_punctuation('?Georgia!'))
        self.assertEqual('Georgia', function_str_title('georgia'))
        self.assertEqual('Florida', function_str_title('FlOrIda'))
        self.assertEqual('South  Carolina', function_clean_strings('!south  carolina###'))


if __name__ == '__main__':
    unittest.main()


def function_parameters(positional1, keyword2=1):
    if positional1 > keyword2:
        return "Greater"
    elif positional1 < keyword2:
        return "Less"


def function_multiple_return_values_tuple():
    a = 5
    b = 6
    c = 7
    return a, b, c


def function_multiple_return_values_dict():
    a = 5
    b = 6
    c = 7
    return {'a': a, 'b': b, 'c': c}


def function_remove_punctuation(value):
    return re.sub('[!#?]', '', value)   #remove special characters


def function_str_string(value):
    return str.strip(value)             #remove whitespace


def function_str_title(value):
    return str.title(value)             #camel case


def function_clean_strings(value):
    value = function_str_string(value)
    value = function_remove_punctuation(value)
    value = function_str_title(value)
    return value
