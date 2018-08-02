import unittest


class PythonFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.int1 = 10
        cls.int2 = 2
        cls.flt1 = 10.1
        cls.flt2 = 2.00
        cls.boolT = True
        cls.boolF = False
        cls.none = None

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

    def test_instanceNone(self):
        #self.assertTrue(isinstance(self.none, None))
        self.assertFalse(isinstance(self.none, int))
        self.assertTrue(int, type(self.none))
        self.assertTrue(self.none is None)
        #self.assertTrue(self.none == None)


if __name__ == '__main__':
    unittest.main()
