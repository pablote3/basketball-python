import numpy as np
from numpy.polynomial.polynomial import polyfit
import pandas as pd
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None
DOWN = -1
TIE = 0
UP = 1

df = pd.read_csv("../input/2017-18_teamBoxScore.csv")

df2 = df[["teamAbbr", "teamPTS", "teamPTS1", "teamPTS2", "opptPTS", "opptPTS1", "opptPTS2"]]

df2.loc[:, "teamPTSHalf"] = df2["teamPTS1"] + df2["teamPTS2"]
df2.loc[:, "opptPTSHalf"] = df2["opptPTS1"] + df2["opptPTS2"]
df2.loc[:, "ptDiffHalf"] = df2["teamPTSHalf"] - df2["opptPTSHalf"]

df2.loc[:, "ptDiffFull"] = df2["teamPTS"] - df2["opptPTS"]


def make_point_diff_mat(df):
    point_diff_df = df[["ptDiffHalf", "ptDiffFull"]]
    point_diff = point_diff_df.values
    return point_diff


def make_bool_point_diff_mat(df):
    point_diff = make_point_diff_mat(df)
    bool_point_diff = np.copy(point_diff)
    bool_point_diff[bool_point_diff > 0] = UP
    bool_point_diff[bool_point_diff == 0] = TIE
    bool_point_diff[bool_point_diff < 0] = DOWN
    return bool_point_diff


def prob_of_winning_given(bool_point_diff, event):
    return np.mean((bool_point_diff[bool_point_diff[:, 0] == event][:, 1] + 1) / 2)


point_diff = make_point_diff_mat(df2)
print(np.corrcoef(point_diff.T))

x = point_diff[:, 0]
y = point_diff[:, 1]
b, m = polyfit(x, y, 1)
plt.plot(x, y, '.')
plt.plot(x, b + m * x, '-')

plt.scatter(x, y)
plt.ylabel("point differential: end of game")
plt.xlabel("point differential: end of first half")
plt.show()

bool_point_diff = make_bool_point_diff_mat(df2)
print(np.corrcoef(bool_point_diff.T))
prob_of_winning_given(bool_point_diff, DOWN)
