import unittest
import pandas as pd
import numpy as np


class TestPandasSeries(unittest.TestCase):
    def test_create(self):
        arr1 = pd.Series([4, 7, -5, 3])                                 #default index
        self.assertTrue(([4, 7, -5, 3] == arr1.values).all())
        self.assertTrue((pd.Index([0, 1, 2, 3] == arr1.index)).all())
        self.assertTrue((pd.RangeIndex(start=0, stop=4, step=1) == arr1.index).all())

        arr1 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])     #index with label
        self.assertTrue((pd.Index(['d', 'b', 'a', 'c'] == arr1.index)).all())
        self.assertEqual(7, arr1['b'])
        self.assertTrue(([3, -5, 4] == arr1[['c', 'a', 'd']]).all())

    def test_functions(self):
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

    def test_reindex(self):
        frame = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
        self.assertEqual(4, frame.index.size)
        frame = frame.reindex(['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(5, frame.index.size)                                   #rearrange new index, add missing values

        frame = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
        frame = frame.reindex(range(6), method='ffill')                         #reindex with forward-fill values
        arr1 = np.array(['blue', 'blue', 'purple', 'purple', 'yellow', 'yellow'])
        self.assertTrue((arr1 == frame.values).all())


if __name__ == '__main__':
    unittest.main()
