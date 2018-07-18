import unittest
import LeadingInTheFirstHalfWinning
import pandas as pd


class MyTest(unittest.TestCase):
    def setUp(self):
        self.data = [
                        {"ptdiffH1": 10, "ptdiff": 5},
                        {"ptdiffH1": 2, "ptdiff": -3}
                    ]
        self.df = pd.DataFrame(self.data)

    def testMake_point_diff_mat(self):
        x = LeadingInTheFirstHalfWinning.make_point_diff_mat(self.df)
        self.assertEqual(x.shape, (2, 2))
        self.assertEqual(x[0, 0], 10)
        self.assertEqual(x[0, 1], 5)
        self.assertEqual(x[1, 0], 2)
        self.assertEqual(x[1, 1], -3)

    def testMake_bool_point_diff_mat(self):
        x = LeadingInTheFirstHalfWinning.make_bool_point_diff_mat(self.df)
        self.assertEqual(x.shape, (2, 2))
        self.assertEqual(x[0, 0], 1)
        self.assertEqual(x[0, 1], 1)
        self.assertEqual(x[1, 0], 1)
        self.assertEqual(x[1, 1], -1)
