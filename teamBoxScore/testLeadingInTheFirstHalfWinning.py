import unittest
import LeadingInTheFirstHalfWinning
import pandas as pd


class MyTest(unittest.TestCase):
    def setUp(self):
        self.data = [
                        {"ptDiffHalf": -4, "ptDiffFull": 5},
                        {"ptDiffHalf": 0, "ptDiffFull": 2},
                        {"ptDiffHalf": 2, "ptDiffFull": -3}
                    ]
        self.df = pd.DataFrame(self.data)

    def testMake_point_diff_mat(self):
        x = LeadingInTheFirstHalfWinning.make_point_diff_mat(self.df)
        self.assertEqual(x.shape, (3, 2))
        self.assertEqual(x[0, 0], -4)
        self.assertEqual(x[0, 1], 5)
        self.assertEqual(x[1, 0], 0)
        self.assertEqual(x[1, 1], 2)
        self.assertEqual(x[2, 0], 2)
        self.assertEqual(x[2, 1], -3)

    def testMake_bool_point_diff_mat(self):
        x = LeadingInTheFirstHalfWinning.make_bool_point_diff_mat(self.df)
        self.assertEqual(x.shape, (3, 2))
        self.assertEqual(x[0, 0], -1)
        self.assertEqual(x[0, 1], 1)
        self.assertEqual(x[1, 0], 0)
        self.assertEqual(x[1, 1], 1)
        self.assertEqual(x[2, 0], 1)
        self.assertEqual(x[2, 1], -1)
