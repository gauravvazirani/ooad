import unittest
import outcome
import craps_onebetplayer
import table 
import nochange_betting

class TestNochangeBetting(unittest.TestCase):
    def setUp(self):
        self.outcome = outcome.Outcome('Pass Line', 1) 
        self.strategy = nochange_betting.NoChangeBetting(
            self.outcome
        )
        self.table = table.Table(5,1000) 
        self.player = craps_onebetplayer.OneBetPlayer(
          table = self.table,
          strategy = self.strategy  
        )

    def test_createBet(self):
        test_bet = self.strategy.createBet(self.player)
        self.assertEqual(test_bet.amount, 10)
        self.assertEqual(test_bet.outcome, self.outcome)

    def test_win(self):
        self.strategy.win()
        self.assertEqual(self.strategy.bet_amount, 10)

    def test_lose(self):
        self.strategy.lose()
        self.assertEqual(self.strategy.bet_amount, 10)

    def tearDown(self):
        self.outcome = None
        self.strategy = None
        self.table = None
        self.player = None

if __name__ == '__main__':
    unittest.main()
