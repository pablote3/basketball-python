import unittest


class Functions(unittest.TestCase):
    def test_if(self):
        self.assertEqual("Greater", function_if(34, 33))
        self.assertEqual("Greater", function_if(34))
        self.assertEqual("Equal", function_if(34, 34))
        self.assertEqual("Less", function_if(34, 35))


if __name__ == '__main__':
    unittest.main()


def function_if(int1, int2=1):
    if int1 > int2:
        return "Greater"
    elif int1 < int2:
        return "Less"
    else:
        return "Equal"
