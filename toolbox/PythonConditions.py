import unittest


class PythonConditions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.int1 = 33
        cls.int2 = 200

    def test_if(self):
        self.assertTrue(condition(self.int1, self.int2))


if __name__ == '__main__':
    unittest.main()


def condition(int1, int2):
    return int2 > int1
