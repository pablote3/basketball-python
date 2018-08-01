import unittest


class DataTypesNumeric(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.int1 = 10
        cls.int2 = 2
        cls.flt1 = 10.1
        cls.flt2 = 2.00

        cls.listNumber = [1, 2, 3, 4, 5]
        cls.tuple = ('Geeks', 'for', 'geeks')

    def test_instanceInt(self):
        self.assertTrue(type(self.int1), int)
        self.assertTrue(type(self.int1), float)
        self.assertTrue(type(self.int1), str)
        self.assertTrue(type(self.int1), bool)

    def test_instanceFloat(self):
        self.assertTrue(type(self.flt1), int)
        self.assertTrue(type(self.flt1), float)
        self.assertTrue(type(self.flt1), str)
        self.assertTrue(type(self.flt1), bool)

    def test_add(self):
        self.assertEqual(self.int1 + self.int2, 12)
        self.assertEqual(self.flt1 + self.flt2, 12.1)
        self.assertEqual(self.int1 + self.flt1, 20.1)


if __name__ == '__main__':
    unittest.main()
