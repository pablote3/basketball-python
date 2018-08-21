import unittest


class Functions(unittest.TestCase):

    def test_exception_handling(self):
        self.assertEqual(12.25, function_exception_handling(12.25))
        self.assertEqual('three', function_exception_handling('three'))


if __name__ == '__main__':
    unittest.main()


def function_exception_handling(n=10):
    try:
        return float(n)
    
    except:
        return n
