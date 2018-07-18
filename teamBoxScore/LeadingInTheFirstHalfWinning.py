import numpy as np
from numpy.polynomial.polynomial import polyfit
import pandas as pd
import matplotlib.pyplot as plt
import unittest

pd.options.mode.chained_assignment = None
DOWN_AT_HALF = -1
TIE_AT_HALF = 0
UP_AT_HALF = 1

df = pd.read_csv("../input/2017-18_teamBoxScore.csv")

df2 = df[["teamAbbr", "teamPTS", "teamPTS1", "teamPTS2", "opptPTS", "opptPTS1", "opptPTS2"]]

df2.loc[:, "teamPTSH1"] = df2["teamPTS1"] + df["teamPTS2"]
df2.loc[:, "opptPTSH1"] = df2["opptPTS1"] + df["opptPTS2"]

df2.loc[:, "ptdiffH1"] = df2["teamPTSH1"] - df2["opptPTSH1"]
df2.loc[:, "ptdiff"] = df2["teamPTS"] - df2["opptPTS"]
df = df[["teamAbbr", "teamLoc", "teamPTS", "teamPTS1", "teamPTS2", "teamPTS3", "teamPTS4", "teamPTS5",
         "opptAbbr", "opptLoc", "opptPTS", "opptPTS1", "opptPTS2", "opptPTS3", "opptPTS4", "opptPTS5"]]


def make_point_diff_mat(df):
    point_diff_df = df[["ptdiffH1", "ptdiff"]]
    point_diff = point_diff_df.as_matrix()
    return point_diff


def make_bool_point_diff_mat(df):
    point_diff = make_point_diff_mat(df)
    bool_point_diff = np.copy(point_diff)
    bool_point_diff[bool_point_diff > 0] = 1
    bool_point_diff[bool_point_diff < 0] = -1
    return bool_point_diff


def prob_of_winning_given(bool_point_diff, event):
    return np.mean((bool_point_diff[bool_point_diff[:, 0] == event][:, 1] + 1) / 2)

#point_diff = make_point_diff_mat(df2)
# np.corrcoef(point_diff.T)
# print(np)
