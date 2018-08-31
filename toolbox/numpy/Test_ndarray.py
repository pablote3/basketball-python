import unittest
import numpy as np


class TestNumpyArray(unittest.TestCase):
    def test_create_array(self):
        arr1 = np.array([6, 7.5, 8, 0, 1])                          #1d 1x5 float array
        self.assertEqual("<class 'numpy.ndarray'>", str(type(arr1)))
        self.assertEqual("float64", arr1.dtype)                     #array data type
        self.assertEqual(1, arr1.ndim)                              #array dimensions
        self.assertEqual((5,), arr1.shape)
        self.assertEqual(6., arr1[0])

        arr1 = np.array([[1, 2, 3], [4, 5, 6]])                     #2d 2x3 integer array
        self.assertEqual("<class 'numpy.ndarray'>", str(type(arr1)))
        self.assertEqual("int64", arr1.dtype)
        self.assertEqual(2, arr1.ndim)
        self.assertEqual((2, 3), arr1.shape)
        self.assertEqual(1, arr1[0, 0])
        self.assertEqual(4, arr1[1, 0])

        arr1 = np.empty(5)                                          #1d 1x5 uninitialized array
        self.assertEqual(1, arr1.ndim)
        self.assertEqual((5, ), arr1.shape)
        self.assertIsNotNone(arr1)

        arr1 = np.zeros((2, 5))                                     #2d 2x5 zeros array
        self.assertEqual(2, arr1.ndim)
        self.assertEqual((2, 5), arr1.shape)
        self.assertEqual(0, arr1[0, 0])
        self.assertTrue((np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == arr1).all())

        arr1 = np.ones((3, 6))                                      #2d 3x6 ones array
        self.assertEqual(2, arr1.ndim)
        self.assertEqual((3, 6), arr1.shape)
        self.assertEqual(1, arr1[0, 1])
        self.assertTrue((np.array([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == arr1).all())

        arr1 = np.arange(15)                                        #1d 1x15 array using range function
        self.assertEqual(1, arr1.ndim)
        self.assertEqual((15, ), arr1.shape)
        self.assertEqual(0, arr1[0])
        self.assertTrue((np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == arr1).all())

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

        arr1 = np.array(['Baa', 'Raa', 'Waa'], dtype=np.string_)    #cast error, string to float64
        self.assertRaises(ValueError, lambda: arr1.astype(np.float64))

    def test_vectorization(self):
        arr1 = np.array([[1., 2., 3.], [4., 5., 6.]])
        self.assertTrue((np.array([[1., 4., 9.], [16., 25., 36.]]) == (arr1 * arr1)).all())
        self.assertTrue((np.array([[0., 0., 0.], [0., 0., 0.]]) == (arr1 - arr1)).all())
        self.assertTrue((np.array([[0., 0., 0.], [0., 0., 0.]]) == (arr1 - arr1)).all())
        self.assertTrue((np.array([[1., 1.4142, 1.7321], [2., 2.2361, 2.4495]]) == (1 / arr1)).any())
        self.assertTrue((np.array([[1., 0., 0.], [2., 0., 0.]]) == (arr1 ** 0.5)).any())
        arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
        self.assertTrue((np.array([[False, True, False], [True, False, True]], dtype=bool) == (arr2 > arr1)).all())

    def test_indexing(self):
        arr1 = np.arange(10)                                        #1d 1x10 array
        self.assertTrue(np.array(([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == arr1).all())
        self.assertEqual(5, arr1[5])
        self.assertTrue(np.array(([5, 6, 7]) == arr1[5:8]).all())

        arr_slice = arr1[5:8]
        self.assertTrue(np.array(([5, 6, 7]) == arr_slice).all())
        arr_slice[:] = 12                                           #broadcast value 12 to all array values
        self.assertTrue(np.array(([12, 12, 12]) == arr_slice).all())
        self.assertTrue(np.array(([0, 1, 2, 3, 4, 12, 12, 12, 8, 9]) == arr1).all())    #original array is impacted

        arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])          #2d 2x3 array
        self.assertTrue(np.array(([4, 5, 6]) == arr1[1]).all())
        self.assertTrue(3 == arr1[0][2])                            #axis 0 = rows; axis 1 = columns
        self.assertTrue(3 == arr1[0, 2])

        arr1 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])            #3d 2x2x3 array
        self.assertTrue(np.array(([[1, 2, 3], [4, 5, 6]]) == arr1[0]).all())
        arr1_copy = arr1[0].copy()                                  #create copy of array[0]
        arr1[0] = 42
        self.assertTrue(np.array(([[42, 42, 42], [42, 42, 42]]) == arr1[0]).all())
        arr1[0] = arr1_copy
        self.assertTrue(np.array(([[1, 2, 3], [4, 5, 6]]) == arr1[0]).all())
        self.assertTrue(np.array(([7, 8, 9]) == arr1[1, 0]).all())

    def test_slicing(self):
        arr1 = np.array([0, 1, 2, 3, 4, 64, 64, 64, 8, 9])          #1d 1x10 array
        self.assertTrue(np.array(([1, 2, 3, 4, 64]) == arr1[1:6]).all())

        arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])          #2d 2x3 array
        self.assertTrue(np.array(([1, 2, 3]) == arr1[:1]).all())    #first row
        self.assertTrue(np.array(([1, 2, 3], [4, 5, 6]) == arr1[:2]).all())   #first 2 rows
        self.assertTrue(np.array(([2, 3], [5, 6]) == arr1[:2, 1:]).all())     #first 2 rows, after first column
        self.assertTrue(np.array(([4, 5]) == arr1[1, :2]).all())    #second row, first 2 columns
        self.assertTrue(np.array(([3, 6]) == arr1[:2, 2]).all())    #third column, first 2 rows
        self.assertTrue(np.array(([1], [4], [7]) == arr1[:, :1]).all())       #entire axis, first column

        arr1[:2, 1:] = 0                                            #assign to slice
        self.assertTrue(np.array(([1, 0, 0], [4, 0, 0], [7, 8, 9]) == arr1).all())

    def test_boolean_indexing(self):
        names1 = np.array(['Bob', 'Joe', 'Bob', 'Marty', 'Paul'])   #1d 1x5 array
        data1 = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])  #2d 2x5 array
        self.assertTrue(np.array(([True, False, True, False, False]) == (names1 == 'Bob')).all())
        self.assertTrue(np.array(([[1, 2], [3, 4]]) == data1[names1 == 'Bob']).all())
        self.assertTrue(np.array(([[1], [3]]) == (data1[names1 == 'Bob', :1])).all())
        self.assertTrue(np.array(([[2], [4]]) == (data1[names1 == 'Bob', 1:])).all())
        self.assertTrue(np.array(([2, 4]) == (data1[names1 == 'Bob', 1])).all())

        self.assertTrue(np.array(([False, True, False, True, True]) == (names1 != 'Bob')).all())    #negate with !=
        self.assertTrue(np.array(([False, True, False, True, True]) == ~(names1 == 'Bob')).all())   #netate with ~

        cond = (names1 == 'Bob') | (names1 == 'Marty')              #combine boolean conditions
        self.assertTrue(np.array(([True, False, True, True, False]) == cond).all())

        data1 = np.array([[1.1, -2.5], [-2, 3], [.3, -.4], [4.1, -5.2], [-5, -6]])
        data1[data1 < 0] = 0                                        #setting values with boolean array
        self.assertTrue(np.array(([[1.1, 0.], [0., 3], [.3, 0.], [4.1, 0.], [0., 0.]]) == data1).all())


if __name__ == '__main__':
    unittest.main()
