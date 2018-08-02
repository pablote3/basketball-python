import unittest


class DataTypesNumeric(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.int1 = 10
        cls.int2 = 2
        cls.flt1 = 10.1
        cls.flt2 = 2.00
        cls.boolT = True
        cls.boolF = False

    def test_instanceInt(self):
        self.assertTrue(isinstance(self.int1, int))
        self.assertTrue(int, type(self.int1))
        self.assertTrue(int, isinstance(self.int1, float))
        self.assertTrue(float, type(self.int1))
        self.assertTrue(str, type(self.int1))
        self.assertTrue(bool, type(self.int1))

    def test_instanceFloat(self):
        self.assertFalse(isinstance(self.flt1, int))
        self.assertTrue(int, type(self.flt1))
        self.assertTrue(isinstance(self.flt1, float))
        self.assertTrue(float, type(self.flt1))
        self.assertTrue(str, type(self.flt1))
        self.assertTrue(bool, type(self.flt1))

    def test_instanceBool(self):
        self.assertTrue(isinstance(self.boolT, int))
        self.assertTrue(int, type(self.boolT))
        self.assertFalse(isinstance(self.boolT, float))
        self.assertTrue(float, type(self.boolT))
        self.assertTrue(str, type(self.boolT))
        self.assertTrue(bool, type(self.boolT))

    def test_add(self):
        self.assertEqual(12, self.int1 + self.int2)
        self.assertEqual(12.1, self.flt1 + self.flt2)
        self.assertEqual(20.1, self.int1 + self.flt1)

    def test_subtract(self):
        self.assertEqual(8, self.int1 - self.int2)
        self.assertEqual(8.1, self.flt1 - self.flt2)
        self.assertEqual(-0.09999999999999964, self.int1 - self.flt1)

    def test_multiply(self):
        self.assertEqual(20, self.int1 * self.int2)
        self.assertEqual(20.2, self.flt1 * self.flt2)
        self.assertEqual(101.0, self.int1 * self.flt1)

    def test_divide(self):
        self.assertEqual(5, self.int1 / self.int2)
        self.assertEqual(5.05, self.flt1 / self.flt2)
        self.assertEqual(0.9900990099009901, self.int1 / self.flt1)

    def test_floorDivide(self):
        self.assertEqual(5, self.int1 // self.int2)
        self.assertEqual(5, self.flt1 // self.flt2)
        self.assertEqual(0, self.int1 // self.flt1)

    def test_exponent(self):
        self.assertEqual(100, self.int1 ** self.int2)
        self.assertEqual(102.00999999999999, self.flt1 ** self.flt2)
        self.assertEqual(100.0, self.int1 ** self.flt2)

    def test_comparison(self):
        self.assertTrue(self.int1 != self.int2)
        self.assertTrue(self.int1 == self.int1)
        self.assertTrue(self.int2 == self.flt2)
        self.assertTrue(self.int1 >= self.int2)
        self.assertTrue(self.int1 >= self.int1)
        self.assertTrue(self.int2 >= self.flt2)

    def test_identity(self):
        self.assertFalse(self.int1 is self.int2)
        self.assertTrue(self.int1 is self.int1)
        self.assertTrue(self.int2 is not self.flt2)

    def test_logical(self):
        self.assertTrue(self.boolT and self.boolT)
        self.assertFalse(self.boolT and self.boolF)
        self.assertTrue(self.boolT or self.boolF)
        self.assertFalse(self.boolF or self.boolF)
        self.assertFalse(not(self.boolT and self.boolT))
        self.assertTrue(self.boolT & self.boolT)
        self.assertFalse(self.boolT & self.boolF)
        self.assertTrue(self.boolT | self.boolF)
        self.assertFalse(self.boolF | self.boolF)


if __name__ == '__main__':
    unittest.main()
