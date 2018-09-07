import unittest
import pandas as pd
import numpy as np


class TestPandasDataFrame(unittest.TestCase):
    def test_create_using_dict(self):
        dict1 = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
                 'year': [2000, 2001, 2002, 2001, 2002, 2003],
                 'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
                 }
        frame = pd.DataFrame(dict1)

        frame.head()                                                            #select first 5 rows
        frame.tail()                                                            #select last 5 rows

        pd.DataFrame(dict1, columns=['year', 'state', 'pop'])                   #change order of columns

        frame = pd.DataFrame(dict1, columns=['year', 'state', 'pop', 'debt'],   #adding column with missing values
                             index=['one', 'two', 'three', 'four', 'five', 'six'])
        self.assertTrue((pd.isnull(frame['debt'])).all())                       #retrieve column as series as dict
        self.assertTrue((pd.notnull(frame.year)).all())                         #retrieve column as series by attribute

        result = pd.Series(['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
                           index=['one', 'two', 'three', 'four', 'five', 'six'])
        self.assertTrue((result == frame['state']).all())                       #retrieve column as indexed series

        result = pd.Index(['year', 'state', 'pop', 'debt'])
        self.assertTrue((result == frame.loc['three'].index).all())             #retrieve row by position
        result = list([2002, 'Ohio', 3.6, float('nan')])
        self.assertTrue((result == frame.loc['three'].values).any())            #TODO: for all(), casting needed

        debt = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
        frame['debt'] = debt                                                    #assign list to debt column
        result = list([2001, 'Ohio', 1.7, -1.2])
        self.assertTrue((result == frame.loc['two'].values).any())              #TODO: for all(), casting needed

        frame['eastern'] = frame.state == 'Ohio'                                #create column of booleans
        self.assertEqual(5, frame.columns.size)
        arr1 = np.array(['year', 'state', 'pop', 'debt', 'eastern'])
        self.assertTrue((arr1 == frame.columns.values).any())                   #TODO: for all(), casting needed

        del frame['eastern']                                                    #delete column
        self.assertEqual(4, frame.columns.size)

    def test_create_using_dict_nested(self):
        dict1 = {'Nevada': {2001: 2.4, 2002: 2.9},                              #nested dict
                 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}
                 }
        frame = pd.DataFrame(dict1)                                             #outer key = columns, inner keys = rows
        self.assertEqual(2, frame.columns.size)
        self.assertEqual(3, frame.index.size)

        self.assertEqual(3, frame.T.columns.size)                               #transpose columns and rows
        self.assertEqual(2, frame.T.index.size)

    def test_reindex(self):
        frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
                             index=['a', 'c', 'd'],
                             columns=['Ohio', 'Texas', 'California'])
        self.assertTrue((pd.Index(['a', 'c', 'd']) == frame.index).all())
        self.assertTrue((pd.Index(['Ohio', 'Texas', 'California']) == frame.columns).all())
        result = pd.Series([0., 3., 6.], index=['a', 'c', 'd'])
        self.assertTrue((result == frame['Ohio']).all())
        result = pd.Series([1., 4., 7.], index=['a', 'c', 'd'])
        self.assertTrue((result == frame['Texas']).all())
        result = pd.Series([2., 5., 8.], index=['a', 'c', 'd'])
        self.assertTrue((result == frame['California']).all())

        frame = frame.reindex(['a', 'b', 'c', 'd'])                             #rearrange new index and add new row
        self.assertTrue((pd.Index(['a', 'b', 'c', 'd']) == frame.index).all())
        self.assertTrue((pd.Index(['Ohio', 'Texas', 'California']) == frame.columns).all())
        result = pd.Series([0., float('nan'), 3., 6.], index=['a', 'b', 'c', 'd'])
        self.assertTrue((result == frame['Ohio']).any())                        #TODO: for all(), casting needed
        result = pd.Series([1., float('nan'), 4., 7.], index=['a', 'b', 'c', 'd'])
        self.assertTrue((result == frame['Texas']).any())                       #TODO: for all(), casting needed
        result = pd.Series([2., float('nan'), 5., 8.], index=['a', 'b', 'c', 'd'])
        self.assertTrue((result == frame['California']).any())                  #TODO: for all(), casting needed


if __name__ == '__main__':
    unittest.main()
