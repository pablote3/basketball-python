import unittest
import numpy as np


class TestNumpyArray(unittest.TestCase):
    def test_array_create(self):
        list1 = [6, 7.5, 8, 0, 1]
        arr1 = np.array(list1)
        self.assertEqual("<class 'numpy.ndarray'>", str(type(arr1)))


if __name__ == '__main__':
    unittest.main()
