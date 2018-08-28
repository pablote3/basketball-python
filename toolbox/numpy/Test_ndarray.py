import unittest
import numpy as np


class TestNumpyArray(unittest.TestCase):
    def test_array_create_float(self):
        list1 = [6, 7.5, 8, 0, 1]
        arr1 = np.array(list1)
        self.assertEqual("<class 'numpy.ndarray'>", str(type(arr1)))
        self.assertEqual((5,), arr1.shape)
        self.assertEqual(6., arr1[0])


if __name__ == '__main__':
    unittest.main()
