import unittest
from nba_py import player
from nba_py.player import get_player


class TestPlayer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.playerId = get_player('Tim', 'Duncan')
        cls.vs_playerId = get_player('Stephen', 'Curry')
        cls.teamId = ''
        cls.measureType = 'Base'
        cls.perMode = 'PerGame'
        cls.plusMinus = 'N'
        cls.paceAdjust = 'N'
        cls.rank = 'Y'
        cls.leagueId = '00'
        cls.season = '2015-16'
        cls.seasonType = 'Regular Season'
        cls.poRound = ''
        cls.outcome = ''
        cls.location = 'Home'
        cls.month = 0
        cls.sessionSegment = ''
        cls.dateFrom = ''
        cls.dateTo = ''
        cls.opponentTeamId = 0
        cls.vsConference = ''
        cls.vsDivision = ''
        cls.gameSegment = ''
        cls.period = 1
        cls.shotClockRange = ''
        cls.lastNGames = 0

    def testAll(self):
        assert player.PlayerList()
        assert player.PlayerSummary(self.playerId)
        # assert player.PlayerGeneralSplits(self.playerId)
        # assert player.PlayerOpponentSplits(self.playerId)
        assert player.PlayerLastNGamesSplits(self.playerId)
        assert player.PlayerInGameSplits(self.playerId)
        assert player.PlayerClutchSplits(self.playerId)
        # assert player.PlayerShootingSplits(self.playerId)
        assert player.PlayerPerformanceSplits(self.playerId)
        assert player.PlayerYearOverYearSplits(self.playerId)

        assert player.PlayerCareer(self.playerId)

        assert player.PlayerProfile(self.playerId)
        assert player.PlayerGameLogs(self.playerId)
        assert player.PlayerShotTracking(self.playerId)
        assert player.PlayerReboundTracking(self.playerId)
        assert player.PlayerPassTracking(self.playerId)
        assert player.PlayerDefenseTracking(self.playerId)
        # assert player.PlayerShotLogTracking(self.playerId)
        # assert player.PlayerReboundLogTracking(self.playerId)
        assert player.PlayerVsPlayer(self.playerId, self.vs_playerId)

    def testPlayerCareer(self):
        playercareer = player.PlayerCareer(self.playerId)

        self.assertTrue((15, 27), playercareer.all_star_season_totals().shape)
        self.assertTrue((1 == playercareer.all_star_season_totals()[1:2].GP).all())
        self.assertTrue((15 == playercareer.career_all_star_season_totals()[0:1].GP).all())
        self.assertTrue((128 == playercareer.college_season_career_totals()[0:1].GP).all())
        self.assertTrue((31 == playercareer.college_season_totals()[0:1].GP).all())
        self.assertTrue((251 == playercareer.post_season_career_totals()[0:1].GP).all())
        self.assertTrue((9 == playercareer.post_season_totals()[0:1].GP).all())
        #postseasonrankings = playercareer.post_season_rankings()
        self.assertTrue(('NR' == playercareer.preseason_career_totals()[0:1].GP).all())
        self.assertTrue(('NR' == playercareer.preseason_season_totals()[0:1].GP).all())
        self.assertTrue((1392 == playercareer.regular_season_career_totals()[0:1].GP).all())
        self.assertTrue((82 == playercareer.regular_season_totals()[0:1].GP).all())
        #regularseasonrankings = playercareer.regular_season_rankings()

    def testPlayerClutchSplits(self):
        playercluchsplits = player.PlayerClutchSplits(self.playerId,
                                                      self.teamId,
                                                      self.measureType,
                                                      self.perMode,
                                                      self.plusMinus,
                                                      self.paceAdjust,
                                                      self.rank,
                                                      self.leagueId,
                                                      self.season,
                                                      self.seasonType,
                                                      self.poRound,
                                                      self.outcome,
                                                      self.location,
                                                      self.month,
                                                      self.sessionSegment,
                                                      self.dateFrom,
                                                      self.dateTo,
                                                      self.opponentTeamId,
                                                      self.vsConference,
                                                      self.vsDivision,
                                                      self.gameSegment,
                                                      self.lastNGames)

        self.assertTrue((1, 62) == playercluchsplits.overall().shape)
        self.assertTrue((31 == playercluchsplits.overall()[0:1].GP).all())
        self.assertTrue((1 == playercluchsplits.last5min_deficit_5point()[0:1].GP).all())
        self.assertTrue((8 == playercluchsplits.last5min_plusminus_5point()[0:1].GP).all())
        self.assertTrue((1 == playercluchsplits.last3min_deficit_5point()[0:1].GP).all())
        self.assertTrue((8 == playercluchsplits.last3min_plusminus_5point()[0:1].GP).all())
        self.assertTrue((1 == playercluchsplits.last1min_deficit_5point()[0:1].GP).all())
        self.assertTrue((6 == playercluchsplits.last1min_plusminus_5point()[0:1].GP).all())
        self.assertTrue((1 == playercluchsplits.last30sec_deficit_3point()[0:1].GP).all())
        self.assertTrue((1 == playercluchsplits.last10sec_deficit_3point()[0:1].GP).all())

    def testPlayerGameLogs(self):
        playergamelogs = player.PlayerGameLogs(self.playerId,
                                               self.leagueId,
                                               self.season,
                                               self.seasonType)

        info = playergamelogs.info()
        self.assertTrue((61, 27) == info.shape)
        self.assertTrue((12 == info[0:1].PTS).all())

    def testPlayerGeneralSplits(self):
        playergeneralsplits = player.PlayerGeneralSplits(self.playerId,
                                                         self.teamId,
                                                         self.measureType,
                                                         self.perMode,
                                                         self.plusMinus,
                                                         self.paceAdjust,
                                                         self.rank,
                                                         self.leagueId,
                                                         self.season,
                                                         self.seasonType,
                                                         self.poRound,
                                                         self.outcome,
                                                         self.location,
                                                         self.month,
                                                         self.sessionSegment,
                                                         self.dateFrom,
                                                         self.dateTo,
                                                         self.opponentTeamId,
                                                         self.vsConference,
                                                         self.vsDivision,
                                                         self.gameSegment,
                                                         self.lastNGames)

        self.assertTrue((1, 62) == playergeneralsplits.overall().shape)
        self.assertTrue((31 == playergeneralsplits.overall()[0:1].GP).all())
        self.assertTrue((1 == playergeneralsplits.days_rest()[0:1].GP).all())
        self.assertTrue((31 == playergeneralsplits.location()[0:1].GP).all())
        self.assertTrue((1 == playergeneralsplits.month()[0:1].GP).all())
        self.assertTrue((20 == playergeneralsplits.pre_post_all_star()[0:1].GP).all())
        self.assertTrue((30 == playergeneralsplits.starting_position()[0:1].GP).all())
        self.assertTrue((31 == playergeneralsplits.win_losses()[0:1].GP).all())

    def testPlayerInGameSplits(self):
        playeringamesplits = player.PlayerInGameSplits(self.playerId,
                                                       self.teamId,
                                                       self.measureType,
                                                       self.perMode,
                                                       self.plusMinus,
                                                       self.paceAdjust,
                                                       self.rank,
                                                       self.leagueId,
                                                       self.season,
                                                       self.seasonType,
                                                       self.poRound,
                                                       self.outcome,
                                                       self.location,
                                                       self.month,
                                                       self.sessionSegment,
                                                       self.dateFrom,
                                                       self.dateTo,
                                                       self.opponentTeamId,
                                                       self.vsConference,
                                                       self.vsDivision,
                                                       self.gameSegment,
                                                       self.lastNGames)

        self.assertTrue((1, 62) == playeringamesplits.overall().shape)
        self.assertTrue((31 == playeringamesplits.overall()[0:1].GP).all())
        self.assertTrue((1 == playeringamesplits.by_actual_margin()[0:1].GP).all())
        self.assertTrue((31 == playeringamesplits.by_half()[0:1].GP).all())
        self.assertTrue((31 == playeringamesplits.by_period()[0:1].GP).all())
        self.assertTrue((31 == playeringamesplits.by_score_margin()[0:1].GP).all())

    def testPlayerLastNGameSplits(self):
        playerlastngamesplits = player.PlayerLastNGamesSplits(self.playerId,
                                                              self.teamId,
                                                              self.measureType,
                                                              self.perMode,
                                                              self.plusMinus,
                                                              self.paceAdjust,
                                                              self.rank,
                                                              self.leagueId,
                                                              self.season,
                                                              self.seasonType,
                                                              self.poRound,
                                                              self.outcome,
                                                              self.location,
                                                              self.month,
                                                              self.sessionSegment,
                                                              self.dateFrom,
                                                              self.dateTo,
                                                              self.opponentTeamId,
                                                              self.vsConference,
                                                              self.vsDivision,
                                                              self.gameSegment,
                                                              self.lastNGames)

        self.assertTrue((1, 62) == playerlastngamesplits.overall().shape)
        self.assertTrue((31 == playerlastngamesplits.overall()[0:1].GP).all())
        self.assertTrue((4 == playerlastngamesplits.gamenumber()[0:1].GP).all())
        self.assertTrue((2 == playerlastngamesplits.last5()[0:1].GP).all())
        self.assertTrue((6 == playerlastngamesplits.last10()[0:1].GP).all())
        self.assertTrue((10 == playerlastngamesplits.last15()[0:1].GP).all())
        self.assertTrue((11 == playerlastngamesplits.last20()[0:1].GP).all())

    def testPlayerList(self):
        playerlist = player.PlayerList(self.leagueId,
                                       self.season,
                                       1)

        self.assertTrue((101, 13) == playerlist.info().shape)
        self.assertTrue(('Memphis' == playerlist.info()[0:1].TEAM_CITY).all())

    def testPlayerOpponentSplits(self):
        playeropponentsplits = player.PlayerOpponentSplits(self.playerId,
                                                           self.teamId,
                                                           self.measureType,
                                                           self.perMode,
                                                           self.plusMinus,
                                                           self.paceAdjust,
                                                           self.rank,
                                                           self.leagueId,
                                                           self.season,
                                                           self.seasonType,
                                                           self.poRound,
                                                           self.outcome,
                                                           self.location,
                                                           self.month,
                                                           self.sessionSegment,
                                                           self.dateFrom,
                                                           self.dateTo,
                                                           self.opponentTeamId,
                                                           self.vsConference,
                                                           self.vsDivision,
                                                           self.gameSegment,
                                                           self.lastNGames)

        self.assertTrue((1, 62) == playeropponentsplits.overall().shape)
        self.assertTrue((31 == playeropponentsplits.overall()[0:1].GP).all())
        self.assertTrue((13 == playeropponentsplits.by_conference()[0:1].GP).all())
        self.assertTrue((5 == playeropponentsplits.by_division()[0:1].GP).all())
        self.assertTrue((1 == playeropponentsplits.by_opponent()[0:1].GP).all())
