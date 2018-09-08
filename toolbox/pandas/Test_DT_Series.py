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
        self.assertTrue(([3, -5, 4] == arr1[['c', 'a', 'd']]).all())

        dict1 = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
        arr1 = pd.Series(dict1)                                         #create from dict
        self.assertEqual(4, arr1.size)
        self.assertTrue((pd.Index(['Ohio', 'Oregon', 'Texas', 'Utah']) == arr1.index).all())
        self.assertEqual(71000, arr1['Texas'])

        arr1 = pd.Series(dict1, index=['California', 'Ohio', 'Oregon', 'Texas'])   #remove Utah, add California to index
        arr1.name = 'population'                                        #assign name to value
        arr1.index.name = 'state'                                       #assign name to index
        self.assertTrue((pd.Index(['California', 'Ohio', 'Oregon', 'Texas']) == arr1.index).all())
        self.assertTrue(pd.isnull(arr1['California']))                  #is null check

    def test_selection(self):
        arr1 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
        self.assertEqual(7, arr1['b'])                                  #select by index
        self.assertEqual(7, arr1[1])                                    #select by i
        self.assertTrue(([7, -5, 4] == arr1[['b', 'a', 'd']]).all())    #slice by indexes
        self.assertTrue(([7, -5] == arr1[1:3]).all())                   #slice by i
        self.assertTrue(([7, 3] == arr1[[1, 3]]).all())                 #slice by i
        self.assertTrue(([4, 7, 3] == arr1[arr1 > 0]).all())            #values greater than 0

    def test_functions(self):
        arr1 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
        self.assertTrue(([8, 14, -10, 6] == arr1 * 2).all())            #values multiplied by 2
        self.assertEqual(True, 'b' in arr1)                             #is 'b' in series

        arr1 = pd.Series({'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000})
        arr1 = arr1.drop('Oregon')                                      #drop row
        self.assertTrue((pd.Index(['Ohio', 'Texas', 'Utah']) == arr1.index).all())
        arr1 = arr1.drop(['Ohio', 'Utah'])                              #drop rows
        self.assertTrue((pd.Index(['Texas']) == arr1.index).all())

    def test_reindex(self):
        arr1 = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
        self.assertEqual(4, arr1.index.size)
        arr1 = arr1.reindex(['a', 'b', 'c', 'd', 'e'])                  #rearrange index, add column with null values
        self.assertEqual(5, arr1.index.size)
        self.assertTrue(pd.isnull(arr1['e']))

        ser1 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
        ser1 = ser1.reindex(range(6), method='ffill')                   #reindex with forward-fill missing values
        arr1 = np.array(['blue', 'blue', 'purple', 'purple', 'yellow', 'yellow'])
        self.assertTrue((arr1 == ser1.values).all())


if __name__ == '__main__':
    unittest.main()
