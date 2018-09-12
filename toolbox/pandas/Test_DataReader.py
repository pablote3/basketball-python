import unittest
import pandas as pd
import numpy as np


class TestPandasDataReader(unittest.TestCase):
    def test_read_web(self):
        import pandas_datareader.data as web
        all_data = {ticker: web.get_data_yahoo(ticker)
                    for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']
                 }
        price = pd.DataFrame({ticker: data['Adj Close']
                              for ticker, data in all_data.items()})
        volume = pd.DataFrame({ticker: data['Volume']
                               for ticker, data in all_data.items()})

        series = pd.Series([0.001729, -0.004404, -0.012080, 0.000323], index=['AAPL', 'GOOG', 'IBM', 'MSFT'])
        self.assertFalse(((series == price.pct_change().iloc[1]).all()).all())


if __name__ == '__main__':
    unittest.main()
