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

        series1 = pd.Series(['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
                            index=['one', 'two', 'three', 'four', 'five', 'six'])
        self.assertTrue((series1 == frame['state']).all())                      #retrieve column as a series
        self.assertEqual(6, frame['state'].size)

        result = pd.Index(['year', 'state', 'pop', 'debt'])
        self.assertTrue((result == frame.loc['three'].index).all())             #retrieve by position
        result = list([2002, 'Ohio', 3.6, float('nan')])
        self.assertTrue((result == frame.loc['three'].values).any())            #some casting needed

        debt = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
        frame['debt'] = debt                                                    #assign list to debt column
        result = list([2001, 'Ohio', 1.7, -1.2])
        self.assertTrue((result == frame.loc['two'].values).any())              #some casting needed

        frame['eastern'] = frame.state == 'Ohio'                                #create column of booleans
        self.assertEqual(5, frame.columns.size)
        arr1 = np.array(['year', 'state', 'pop', 'debt', 'eastern'])
        self.assertTrue((arr1 == frame.columns.values).any())

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

        series1 = {'Ohio': frame['Ohio'][:-1],                                  #series
                   'Nevada': frame['Nevada'][:2]
                   }
        frame = pd.DataFrame(series1)                                           #outer key = columns, inner keys = rows
        self.assertEqual(2, frame.columns.size)
        self.assertEqual(2, frame.index.size)


if __name__ == '__main__':
    unittest.main()
