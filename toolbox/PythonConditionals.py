import unittest


class PythonConditions(unittest.TestCase):
    def test_if(self):
        self.assertEqual("Greater", conditionIf(34, 33))
        self.assertEqual("Equal", conditionIf(34, 34))
        self.assertEqual("Less", conditionIf(34, 35))


if __name__ == '__main__':
    unittest.main()


def conditionIf(int1, int2):
    if int1 > int2:
        return "Greater"
    elif int1 < int2:
        return "Less"
    else:
        return "Equal"
