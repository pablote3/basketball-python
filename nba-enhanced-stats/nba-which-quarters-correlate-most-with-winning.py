from numpy.polynomial.polynomial import polyfit
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../input/2017-18_teamBoxScore.csv")
df = df[["teamAbbr", "teamLoc", "teamPTS", "teamPTS1", "teamPTS2", "teamPTS3", "teamPTS4", "teamPTS5",
         "opptAbbr", "opptLoc", "opptPTS", "opptPTS1", "opptPTS2", "opptPTS3", "opptPTS4", "opptPTS5"]]

for i in range(1, 6):
    df["ptsDiff%s" % i] = df["teamPTS%s" % i] - df["opptPTS%s" % i]
df["teamWin"] = (df["teamPTS"] > df["opptPTS"]).apply(lambda x: x and 1.0 or -1.0)
df["wentToOT"] = (df["teamPTS5"] + df["opptPTS5"]) > 0
print(df.shape)
print(df.loc[0, :])

# Eliminate overtime games
dfReg = df[["teamAbbr", "teamLoc", "ptsDiff1", "ptsDiff2", "ptsDiff3", "ptsDiff4", "teamWin", "wentToOT"]]
dfReg = dfReg.drop(dfReg[(dfReg.wentToOT == True)].index)
dfReg.drop("wentToOT", axis=1, inplace=True)
print(dfReg.shape)
print(dfReg.corr())
print("")

# Sum team points per quarter and team win​
sumsReg = dfReg.select_dtypes(pd.np.number).sum().rename('total')
sumsReg = sumsReg[["ptsDiff1", "ptsDiff2", "ptsDiff3", "ptsDiff4", "teamWin"]]
print(sumsReg)

# Utah Jazz games ending during regulation
dfJazz = dfReg[["teamAbbr", "ptsDiff1", "ptsDiff2", "ptsDiff3", "ptsDiff4", "teamWin"]]
dfJazz.drop(dfJazz[(dfJazz.teamAbbr != "UTA")].index, inplace=True)
dfJazz.drop(["teamAbbr"], axis=1, inplace=True)
print(dfJazz.shape)
print(dfJazz.corr())
print("")

# Utah Jazz home games ending during regulation
dfJazzHome = dfReg[["teamAbbr", "teamLoc", "ptsDiff1", "ptsDiff2", "ptsDiff3", "ptsDiff4", "teamWin"]]
dfJazzHome.drop(dfJazzHome[(dfJazzHome.teamLoc == "Away")].index, inplace=True)
dfJazzHome.drop(dfJazzHome[(dfJazzHome.teamAbbr != "UTA")].index, inplace=True)
dfJazzHome.drop(["teamAbbr", "teamLoc"], axis=1, inplace=True)
print(dfJazzHome.shape)
print(dfJazzHome.corr())
print("")

sumsJazzHome = dfJazzHome.select_dtypes(pd.np.number).sum().rename('total')
sumsJazzHome = sumsJazzHome[["ptsDiff1", "ptsDiff2", "ptsDiff3", "ptsDiff4", "teamWin"]]
print(sumsJazzHome)

# best fit lines
# slightly negative correlation between periods 1 and 2
x = dfJazzHome['ptsDiff1']
y = dfJazzHome['ptsDiff2']
b, m = polyfit(x, y, 1)
plt.plot(x, y, '.')
plt.plot(x, b + m * x, '-')
plt.scatter(x, y, color='cyan')
plt.show()

# slightly positive correlation between periods 3 and 4
x = dfJazzHome['ptsDiff3']
y = dfJazzHome['ptsDiff4']
b, m = polyfit(x, y, 1)
plt.plot(x, y, '.')
plt.plot(x, b + m * x, '-')
plt.scatter(x, y, color='cyan')
plt.show()

# significant correlation between period 4 and game outcome
x = dfJazzHome['ptsDiff4']
y = dfJazzHome['teamWin']
b, m = polyfit(x, y, 1)
plt.plot(x, y, '.')
plt.plot(x, b + m * x, '-')
plt.scatter(x, y, color='cyan')
plt.show()
