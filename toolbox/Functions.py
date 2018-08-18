import unittest


class Functions(unittest.TestCase):
    def test_if(self):
        self.assertEqual("Greater", function_if(34, 33))
        self.assertEqual("Greater", function_if(34))
        self.assertEqual(None, function_if(34, 34))
        self.assertEqual("Less", function_if(34, 35))


if __name__ == '__main__':
    unittest.main()


def function_if(positional1, keyword2=1):
    if positional1 > keyword2:
        return "Greater"
    elif positional1 < keyword2:
        return "Less"
