import unittest
from nba_py import team
from nba_py.player import get_player
from nba_py.constants import TEAMS


class TestTeam(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.teamId = TEAMS['ATL']['id']
        cls.playerId = get_player('Lebron', 'James')

    def testAll(self):
        assert team.TeamList()
        assert team.TeamSummary(self.teamId)
        team_details = team.TeamDetails(self.teamId)
        assert team_details
        # assert team_details.background()
        # assert team_details.history()
        assert team.TeamCommonRoster(self.teamId)
        assert team.TeamGeneralSplits(self.teamId)
        assert team.TeamOpponentSplits(self.teamId)
        assert team.TeamLastNGamesSplits(self.teamId)
        assert team.TeamInGameSplits(self.teamId)
        assert team.TeamClutchSplits(self.teamId)
        assert team.TeamShootingSplits(self.teamId)
        assert team.TeamPerformanceSplits(self.teamId)
        assert team.TeamLineups(self.teamId)
        assert team.TeamPlayers(self.teamId)
        assert team.TeamPlayerOnOffDetail(self.teamId)
        assert team.TeamPlayerOnOffSummary(self.teamId)
        assert team.TeamGameLogs(self.teamId)
        assert team.TeamShotTracking(self.teamId)
        assert team.TeamReboundTracking(self.teamId)
        assert team.TeamPassTracking(self.teamId)
        assert team.TeamVsPlayer(self.teamId, self.playerId)

    def test_TeamSeasons(self):
        teamstats = team.TeamSeasons(self.teamId)
        info = teamstats.info()
        self.assertTrue((70, 34), info.shape)
