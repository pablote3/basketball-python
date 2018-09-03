import unittest
import pandas as pd


class TestNumpyArray(unittest.TestCase):
    def test_create_array(self):
        arr1 = pd.Series([4, 7, -5, 3])                                 #default index
        self.assertTrue(([4, 7, -5, 3] == arr1.values).all())
        self.assertTrue((pd.Index([0, 1, 2, 3] == arr1.index)).all())
        self.assertTrue((pd.RangeIndex(start=0, stop=4, step=1) == arr1.index).all())

        arr1 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])     #index with label
        self.assertTrue((pd.Index(['d', 'b', 'a', 'c'] == arr1.index)).all())
        self.assertEqual(7, arr1['b'])
        self.assertTrue(([3, -5, 4] == arr1[['c', 'a', 'd']]).all())


if __name__ == '__main__':
    unittest.main()
