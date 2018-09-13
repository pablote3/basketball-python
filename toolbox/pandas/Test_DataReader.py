import unittest
import pandas as pd
import numpy as np
import os


class TestPandasDataReader(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = os.path.dirname(__file__) + "/files"

    def test_read_csv(self):
        result = pd.DataFrame([[1, 2, 3, 4, 'hello'], [5, 6, 7, 8, 'world'], [9, 10, 11, 12, 'foo']],
                              index=[0, 1, 2],
                              columns=['a', 'b', 'c', 'd', 'message'])
        df = pd.read_csv(self.path + '/paulHeader.csv')
        self.assertTrue(((result == df).all()).all())

    # def test_read_web(self):
        # import pandas_datareader.data as web
        # all_data = {ticker: web.get_data_yahoo(ticker)
        #             for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']
        #          }
        # price = pd.DataFrame({ticker: data['Adj Close']
        #                       for ticker, data in all_data.items()})
        # volume = pd.DataFrame({ticker: data['Volume']
        #                        for ticker, data in all_data.items()})
        #
        # returns = price.pct_change()
        # series = pd.Series([0.001729, -0.004404, -0.012080, 0.000323], index=['AAPL', 'GOOG', 'IBM', 'MSFT'])
        # self.assertFalse(((series == returns.iloc[1]).all()).all())
        #
        # self.assertEqual(0.4727037674161532, returns['MSFT'].corr(returns['IBM']))    #correlation between non-na values
        # self.assertEqual(7.975231793694253e-05, returns['MSFT'].cov(returns['IBM']))  #covariance between non-na values
        #
        # series = pd.Series([0.429221, 1.000000, 0.394260, 0.508301], index=['AAPL', 'GOOG', 'IBM', 'MSFT'])
        # self.assertFalse(((series == returns.corr().iloc[1]).all()).all())            #full correlation
        # series = pd.Series([0.000103, 0.000230, 0.000071, 0.000109], index=['AAPL', 'GOOG', 'IBM', 'MSFT'])
        # self.assertFalse(((series == returns.cov().iloc[1]).all()).all())             #full covariance
        #
        # series = pd.Series([0.361089, 0.394260, 1.000000, 0.472704], index=['AAPL', 'GOOG', 'IBM', 'MSFT'])
        # self.assertFalse(((series == returns.corrwith(returns.IBM)).all()).all())     #correlation with column
        # series = pd.Series([-0.066761, -0.017556, -0.162330, -0.087171], index=['AAPL', 'GOOG', 'IBM', 'MSFT'])
        # self.assertFalse(((series == returns.corrwith(volume)).all()).all())          #correlation with value


if __name__ == '__main__':
    unittest.main()
