import unittest
import pandas as pd


class TestNumpyArray(unittest.TestCase):
    def test_create_array(self):
        arr1 = pd.Series([4, 7, -5, 3])
        self.assertTrue(([4, 7, -5, 3] == arr1.values).all())           #array representation
        self.assertTrue(([0, 1, 2, 3] == arr1.index.values).all())      #index


if __name__ == '__main__':
    unittest.main()
