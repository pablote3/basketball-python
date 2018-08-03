import unittest


class PythonStrings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.strMultLines = """
                              This is a longer string
                              that spans multiple lines
                           """
        cls.strDouble = "doubleQuote"
        cls.strInt = 5
        cls.strFloat = 2.5
        cls.strList = "blah"
        cls.list = list(cls.strList)

    def test_convert(self):
        self.assertEqual('5', (str(self.strInt)))
        self.assertEqual('2.5', (str(self.strFloat)))

    def test_comparison(self):
        self.assertEqual('doubleQuote', self.strDouble)
        self.assertEqual("doubleQuote", self.strDouble)

    def test_concatenate(self):
        self.assertEqual('doubleQuote blah', self.strDouble + ' ' + self.strList)

    def test_asList(self):
        self.assertEqual(['b', 'l', 'a'], self.list[:3])
        self.assertEqual('bla', self.strList[:3])

    def test_multipleLines(self):
        self.assertEqual(3, self.strMultLines.count('\n'))

    def test_error(self):
        self.assertRaises(IndexError, lambda: self.strDouble[25])


if __name__ == '__main__':
    unittest.main()
