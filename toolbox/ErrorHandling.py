import unittest


class Functions(unittest.TestCase):

    def test_exception_handling(self):
        self.assertEqual(12.25, function_catch_except(12.25))
        self.assertEqual('exception', function_catch_except('three'))
        self.assertEqual('success', function_catch_value_error(12.25))
        self.assertEqual('valueError', function_catch_value_error('three'))
        self.assertEqual('openSuccess', function_open_file('/home/pablote/Documents/python/notes/paul.txt'))
        self.assertEqual('openFailed', function_open_file('/home/pablote/Documents/python/notes/paul.bat'))


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


def function_open_file(path):
    try:
        f = open(path, 'r')
    except:
        return 'openFailed'
    else:
        f.close()
        return 'openSuccess'
    # finally:
    #     f.close()                 #UnboundLocalError if f not loaded
