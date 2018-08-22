import unittest
import os
from FileHandling import FileHandling


class ErrorHandling(unittest.TestCase):
    def test_exception_handling(self):
        absolute_path = "/home/pablote/git/basketball-python/toolbox"
        relative_path = os.path.dirname(__file__)                        #absolute dir the script is in
        self.assertEqual(12.25, function_catch_except(12.25))
        self.assertEqual('exception', function_catch_except('three'))
        self.assertEqual('success', function_catch_value_error(12.25))
        self.assertEqual('valueError', function_catch_value_error('three'))
        self.assertEqual(2, FileHandling.function_read_line(absolute_path + '/paulRead.txt'))
        self.assertEqual('openFailed', FileHandling.function_read_line(absolute_path + '/paulo.txt'))
        self.assertEqual(2, FileHandling.function_read_line(relative_path + '/paulRead.txt'))
        self.assertEqual('openFailed', FileHandling.function_read_line(relative_path + '/paulo.txt'))
        self.assertEqual('line1\nline2', FileHandling.function_read_file(relative_path + '/paulRead.txt'))
        self.assertEqual('openFailed', FileHandling.function_read_file(relative_path + '/paulo.txt'))


if __name__ == '__main__':
    unittest.main()


def function_catch_except(n=10):
    try:
        return float(n)
    except:
        return 'exception'


def function_catch_value_error(n=10):
    try:
        float(n)
    except ValueError:
        return 'valueError'
    else:
        return 'success'
    finally:
        print()     #dummy event
