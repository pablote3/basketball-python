import unittest
from datetime import datetime, date, time


class PythonDataTypes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.int1 = 10
        cls.int2 = 2
        cls.flt1 = 10.1
        cls.flt2 = 2.00
        cls.boolT = True
        cls.boolF = False
        cls.none = None
        cls.dtTm = datetime(2011, 10, 29, 20, 30, 21)
        cls.strMultiLine = """
                              This is a longer string
                              that spans multiple lines
                           """
        cls.str1 = "doubleQuote"
        cls.str2 = "blah"
        cls.list = list(cls.str2)

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

    def test_dateType(self):
        self.assertEqual(29, self.dtTm.day)
        self.assertEqual(30, self.dtTm.minute)
        self.assertEqual(date(2011, 10, 29), self.dtTm.date())
        self.assertEqual(time(20, 30, 21), self.dtTm.time())

    def test_dateFormat(self):
        self.assertEqual('10/29/2011 20:30', self.dtTm.strftime('%m/%d/%Y %H:%M'))
        self.assertEqual(datetime(2009, 10, 31, 0, 0), datetime.strptime('20091031', '%Y%m%d'))

    def test_stringConvert(self):
        self.assertEqual('10', (str(self.int1)))
        self.assertEqual('10.1', (str(self.flt1)))
        self.assertRaises(IndexError, lambda: self.str1[25])

    def test_stringComparison(self):
        self.assertEqual('doubleQuote', self.str1)
        self.assertEqual("doubleQuote", self.str1)

    # noinspection PyTypeChecker
    def test_stringConcatenate(self):
        self.assertEqual('doubleQuote blah', self.str1 + ' ' + self.str2)
        self.assertRaises(TypeError, lambda: self.str1 + self.int1)

    def test_stringAsList(self):
        self.assertEqual(['b', 'l', 'a'], self.list[:3])
        self.assertEqual('bla', self.str2[:3])
        self.assertTrue("Q" in self.str1)
        self.assertFalse("m" in self.str1)
        self.assertTrue("m" not in self.str1)

    def test_stringMultipleLines(self):
        self.assertEqual(3, self.strMultiLine.count('\n'))


if __name__ == '__main__':
    unittest.main()
