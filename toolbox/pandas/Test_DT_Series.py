import unittest
import pandas as pd


class TestPandasSeries(unittest.TestCase):
    def test_create_series(self):
        arr1 = pd.Series([4, 7, -5, 3])                                 #default index
        self.assertTrue(([4, 7, -5, 3] == arr1.values).all())
        self.assertTrue((pd.Index([0, 1, 2, 3] == arr1.index)).all())
        self.assertTrue((pd.RangeIndex(start=0, stop=4, step=1) == arr1.index).all())

        arr1 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])     #index with label
        self.assertTrue((pd.Index(['d', 'b', 'a', 'c'] == arr1.index)).all())
        self.assertEqual(7, arr1['b'])
        self.assertTrue(([3, -5, 4] == arr1[['c', 'a', 'd']]).all())

    def test_series_functions(self):
        arr1 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
        self.assertTrue(([4, 7, 3] == arr1[arr1 > 0]).all())            #values greater than 0
        self.assertTrue(([8, 14, -10, 6] == arr1 * 2).all())            #values multiplied by 2
        self.assertEqual(True, 'b' in arr1)                             #'b' in series

        dict1 = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
        arr1 = pd.Series(dict1)                                         #create from dict
        self.assertEqual(4, arr1.size)
        self.assertTrue((pd.Index(['Ohio', 'Oregon', 'Texas', 'Utah']) == arr1.index).all())
        self.assertEqual(71000, arr1['Texas'])
        match = pd.Series(arr1, index=['California', 'Ohio', 'Oregon', 'Texas'])
        match.name = 'population'
        match.index.name = 'state'
        self.assertTrue((pd.Index(['California', 'Ohio', 'Oregon', 'Texas']) == match.index).all())
        self.assertTrue(pd.isnull(match['California']))                 #is null check


if __name__ == '__main__':
    unittest.main()
