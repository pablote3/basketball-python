import unittest
import nba_py


class TestNbaPy(unittest.TestCase):

    def testAll(self):
        assert nba_py.Scoreboard(month=2, day=21, year=2015)

    def testScoreboard(self):
        scoreboard = nba_py.Scoreboard(month=2, day=21, year=2015)

        available = scoreboard.available()
        self.assertTrue((5, 2), available.shape)
        self.assertTrue(('0021400817' == available[1:2].GAME_ID).all())

        eastconfstandingsbyday = scoreboard.east_conf_standings_by_day()
        self.assertTrue((15, 12), eastconfstandingsbyday.shape)
        self.assertTrue(('Toronto' == eastconfstandingsbyday[1:2].TEAM).all())

        westconfstandingsbyday = scoreboard.west_conf_standings_by_day()
        self.assertTrue((15, 12), westconfstandingsbyday.shape)
        self.assertTrue(('Memphis' == westconfstandingsbyday[1:2].TEAM).all())

        gameheader = scoreboard.game_header()
        self.assertTrue((5, 14), gameheader.shape)
        self.assertTrue(('20150221/NOPMIA' == gameheader[1:2].GAMECODE).all())

        lastmeeting = scoreboard.last_meeting()
        self.assertTrue((5, 13), lastmeeting.shape)
        self.assertTrue(('Heat' == lastmeeting[1:2].LAST_GAME_HOME_TEAM_NAME).all())

        linescore = scoreboard.line_score()
        self.assertTrue((10, 28), linescore.shape)
        self.assertTrue(('Charlotte' == linescore[1:2].TEAM_CITY_NAME).all())

        seriesstandings = scoreboard.series_standings()
        self.assertTrue((5, 7), seriesstandings.shape)
        self.assertTrue(('Tied' == seriesstandings[1:2].SERIES_LEADER).all())
