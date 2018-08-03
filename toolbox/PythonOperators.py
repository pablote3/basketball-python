import unittest


class PythonOperators(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.int1 = 10
        cls.int2 = 2
        cls.flt1 = 10.1
        cls.flt2 = 2.00
        cls.str1 = "10.0"
        cls.boolT = True
        cls.boolF = False
        cls.none = None

    def test_typecast(self):
        self.assertEqual(10, int(self.flt1))
        self.assertEqual(10.0, float(self.str1))
        self.assertEqual(True, bool(self.str1))

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
