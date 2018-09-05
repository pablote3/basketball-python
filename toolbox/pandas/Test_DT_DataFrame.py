import unittest
import pandas as pd


class TestPandasDataFrame(unittest.TestCase):
    def test_create_dataframe(self):
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


if __name__ == '__main__':
    unittest.main()
