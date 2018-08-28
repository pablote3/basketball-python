import unittest
import numpy as np


class TestNumpyArray(unittest.TestCase):
    def test_create_float_array(self):
        arr1 = np.array([6, 7.5, 8, 0, 1])
        self.assertEqual("<class 'numpy.ndarray'>", str(type(arr1)))
        self.assertEqual("float64", arr1.dtype)             #data type of array
        self.assertEqual(1, arr1.ndim)                      #number of dimensions
        self.assertEqual((5,), arr1.shape)
        self.assertEqual(6., arr1[0])

    def test_create_two_dimension_array(self):
        arr1 = np.array([[1, 2, 3], [4, 5, 6]])
        self.assertEqual("<class 'numpy.ndarray'>", str(type(arr1)))
        self.assertEqual("int64", arr1.dtype)             #data type of array
        self.assertEqual(2, arr1.ndim)                      #number of dimensions
        self.assertEqual((2, 3), arr1.shape)
        self.assertEqual(1, arr1[0, 0])
        self.assertEqual(4, arr1[1, 0])


if __name__ == '__main__':
    unittest.main()
