import unittest


class Functions(unittest.TestCase):
    def test_parameters(self):
        self.assertEqual("Greater", function_parameters(34, 33))
        self.assertEqual("Greater", function_parameters(34))
        self.assertEqual(None, function_parameters(34, 34))
        self.assertEqual("Less", function_parameters(34, 35))

    def test_multiple_return_values(self):
        self.assertEqual((5, 6, 7), function_multiple_return_values_tuple())
        self.assertEqual({'a': 5, 'b': 6, 'c': 7}, function_multiple_return_values_dict())


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
