from pycrackwatch import api
from datetime import datetime
import unittest

class TestCrackwatch(unittest.TestCase):

    def setUp(self):

        self.cracks = api.getCracks()
        self.games = api.getGames()
        self.test_game = self.games[0]
        self.test_crack = self.cracks[0]

    def test_cracks(self):

        assert isinstance(self.cracks, (list,))
        assert len(self.cracks) == 30

        assert self.test_crack.__repr__().startswith("<Crack -")

        assert isinstance(self.test_crack.title, str)
        assert isinstance(self.test_crack.scene_group, str)
        assert isinstance(self.test_crack.image, str)
        assert isinstance(self.test_crack.date, datetime)
        self.assertRaises(Exception, self.test_crack.get, 'test')

    def test_games(self):
        assert isinstance(self.games, (list,))
        assert len(self.games) == 30

        assert self.test_game.__repr__().startswith("<Game -")

        assert isinstance(self.test_game.title, str)
        assert isinstance(self.test_game.link, str)
        assert isinstance(self.test_game.pub_date, datetime)
        assert isinstance(self.test_game.images, tuple)
        assert isinstance(self.test_game.crack_date, datetime)
        assert isinstance(self.test_game.is_AAA, bool)
        assert isinstance(self.test_game.is_hot, bool)
        assert isinstance(self.test_game.NFOs_count, int)
        assert isinstance(self.test_game.comments_count, int)
        assert isinstance(self.test_game.ratings, int)
        assert isinstance(self.test_game.followers_count, int)
        assert isinstance(self.test_game.original_price, float)
        assert isinstance(self.test_game.best_prices, tuple)
        assert isinstance(self.test_game.original_platform, str)
        assert isinstance(self.test_game.best_platforms, tuple)
        assert isinstance(self.test_game.DRMs, tuple)
        assert isinstance(self.test_game.scene_groups, tuple)
        assert isinstance(self.test_game.steam, str)
        assert isinstance(self.test_game.origin, str)
        assert isinstance(self.test_game.IMDB, str)
        assert isinstance(self.test_game.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
