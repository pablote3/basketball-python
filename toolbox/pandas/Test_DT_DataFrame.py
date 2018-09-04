import unittest
import pandas as pd


class TestPandasDataFrame(unittest.TestCase):
    def test_create_dataframe(self):
        dict1 = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
                 'year': [2000, 2001, 2002, 2001, 2002, 2003],
                 'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
                 }
        frame = pd.DataFrame(dict1)

        frame.head()                                            #select first 5 rows
        frame.tail()                                            #select last 5 rows
        pd.DataFrame(frame, columns=['year', 'state', 'pop'])    #change order of columns


if __name__ == '__main__':
    unittest.main()
