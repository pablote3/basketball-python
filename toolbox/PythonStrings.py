import unittest


class PythonStrings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.strMultLines = """
                              This is a longer string
                              that spans multiple lines
                              """
        cls.strDouble = "doubleQuote"

    def test_multipleLines(self):
        self.assertEqual(3, self.strMultLines.count('\n'))

    def test_comparison(self):
        self.assertEqual(self.strDouble, 'doubleQuote')
        self.assertEqual(self.strDouble, "doubleQuote")

    def test_error(self):
        self.assertRaises(IndexError, lambda: self.strDouble[25])


if __name__ == '__main__':
    unittest.main()
