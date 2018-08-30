import unittest
import numpy as np


class TestNumpyArray(unittest.TestCase):
    def test_create_float_array(self):
        arr1 = np.array([6, 7.5, 8, 0, 1])
        self.assertEqual("<class 'numpy.ndarray'>", str(type(arr1)))
        self.assertEqual("float64", arr1.dtype)                     #data type of array
        self.assertEqual(1, arr1.ndim)                              #number of dimensions
        self.assertEqual((5,), arr1.shape)
        self.assertEqual(6., arr1[0])

    def test_create_two_dimension_array(self):
        arr1 = np.array([[1, 2, 3], [4, 5, 6]])
        self.assertEqual("<class 'numpy.ndarray'>", str(type(arr1)))
        self.assertEqual("int64", arr1.dtype)                       #data type of array
        self.assertEqual(2, arr1.ndim)                              #number of dimensions
        self.assertEqual((2, 3), arr1.shape)
        self.assertEqual(1, arr1[0, 0])
        self.assertEqual(4, arr1[1, 0])

    def test_create_zeros_array(self):
        arr1 = np.zeros(10)
        self.assertEqual(1, arr1.ndim)
        self.assertEqual((10, ), arr1.shape)
        self.assertEqual(0, arr1[0])

    def test_create_ones_array(self):
        arr1 = np.ones((3, 6))
        self.assertEqual(2, arr1.ndim)
        self.assertEqual((3, 6), arr1.shape)
        self.assertEqual(1, arr1[0, 1])

    def test_create_empty_array(self):
        arr1 = np.empty((2, 3, 2))                                  #not initialized
        self.assertEqual(3, arr1.ndim)
        self.assertEqual((2, 3, 2), arr1.shape)
        self.assertIsNotNone(arr1[0, 1, 0])

    def test_create_arrange_array(self):
        arr1 = np.arange(15)                                        #built in range function
        self.assertEqual(1, arr1.ndim)
        self.assertEqual((15, ), arr1.shape)
        self.assertEqual(0, arr1[0])

    def test_convert_dtype_array(self):
        arr1 = np.array([1, 2, 3, 4, 5])                            #int64 to float64
        self.assertEqual('int64', arr1.dtype)
        arr2 = arr1.astype(np.float64)
        self.assertEqual('float64', arr2.dtype)
        self.assertEqual(1.0, arr2[0, ])

        arr1 = np.array([1.0, 2.0, 3.0, 4.0, 5.0])                  #float64 to int32
        self.assertEqual('float64', arr1.dtype)
        arr2 = arr1.astype(np.int32)
        self.assertEqual('int32', arr2.dtype)
        self.assertEqual(1, arr2[0, ])

        arr1 = np.array(['1.25', '-9.6', '42'], dtype=np.string_)   #string to float64
        self.assertEqual('|S4', arr1.dtype)
        arr2 = arr1.astype(np.float)
        self.assertEqual('float', arr2.dtype)
        self.assertEqual(1.25, arr2[0, ])

        arr1 = np.array(['Baa', 'Raa', 'Waa'], dtype=np.string_)   #cast error, string to float64
        self.assertRaises(ValueError, lambda: arr1.astype(np.float64))

    def test_vectorization(self):
        arr1 = np.array([[1., 2., 3.], [4., 5., 6.]])
        self.assertTrue((np.array([[1., 4., 9.], [16., 25., 36.]]) == (arr1 * arr1)).all())
        self.assertTrue((np.array([[0., 0., 0.], [0., 0., 0.]]) == (arr1 - arr1)).all())
        self.assertTrue((np.array([[0., 0., 0.], [0., 0., 0.]]) == (arr1 - arr1)).all())
        self.assertTrue((np.array([[1., 1.4142, 1.7321], [2., 2.2361, 2.4495]]) == (1 / arr1)).any())
        self.assertTrue((np.array([[1., 0., 0.], [2., 0., 0.]]) == (arr1 ** 0.5)).any())


if __name__ == '__main__':
    unittest.main()
