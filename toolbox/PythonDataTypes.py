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
        cls.dt = datetime(2011, 10, 29, 20, 30, 21)
        cls.strMultLines = """
                              This is a longer string
                              that spans multiple lines
                           """
        cls.strDouble = "doubleQuote"
        cls.strInt = 5
        cls.strFloat = 2.5
        cls.strList = "blah"
        cls.list = list(cls.strList)

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
        self.assertEqual(29, self.dt.day)
        self.assertEqual(30, self.dt.minute)
        self.assertEqual(date(2011, 10, 29), self.dt.date())
        self.assertEqual(time(20, 30, 21), self.dt.time())

    def test_dateFormat(self):
        self.assertEqual('10/29/2011 20:30', self.dt.strftime('%m/%d/%Y %H:%M'))
        self.assertEqual(datetime(2009, 10, 31, 0, 0), datetime.strptime('20091031', '%Y%m%d'))

    def test_stringConvert(self):
        self.assertEqual('5', (str(self.strInt)))
        self.assertEqual('2.5', (str(self.strFloat)))

    def test_stringComparison(self):
        self.assertEqual('doubleQuote', self.strDouble)
        self.assertEqual("doubleQuote", self.strDouble)

    def test_stringConcatenate(self):
        self.assertEqual('doubleQuote blah', self.strDouble + ' ' + self.strList)

    def test_stringAsList(self):
        self.assertEqual(['b', 'l', 'a'], self.list[:3])
        self.assertEqual('bla', self.strList[:3])

    def test_stringMultipleLines(self):
        self.assertEqual(3, self.strMultLines.count('\n'))

    def test_stringError(self):
        self.assertRaises(IndexError, lambda: self.strDouble[25])


if __name__ == '__main__':
    unittest.main()
