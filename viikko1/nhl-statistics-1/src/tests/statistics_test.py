import unittest
from statistics import Statistics
from player import Player
from sort_by import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_valid_search_works(self):
        player = self.statistics.search("Semenko")
        self.assertEqual(player, self.statistics._players[0])
        player = self.statistics.search("Kurri")
        self.assertEqual(player, self.statistics._players[2])

    def test_invalid_search_works(self):
        player = self.statistics.search("Matti")
        self.assertEqual(player, None)

    def test_team_works(self):
        team = self.statistics.team("EDM")
        self.assertEqual(team[0], self.statistics._players[0])
        self.assertEqual(team[1], self.statistics._players[2])
        self.assertEqual(team[2], self.statistics._players[4])
    
    def test_top_correct_amount(self):
        # top(n) funktio näyttää palauttavan n+1 pelaajaa.
        # en tiedä onko tarkoituksellista, mutta en lähtenyt koodia muokkaamaan joten testit sen mukaan.
        top = self.statistics.top(2)
        self.assertEqual(len(top), 3)
    
    def test_top_correct_sorting_no_argument(self):
        top = self.statistics.top(2)
        self.assertEqual(top[0], self.statistics._players[4])
        self.assertEqual(top[1], self.statistics._players[1])
        self.assertEqual(top[2], self.statistics._players[3])
    
    def test_top_correct_sorting_points(self):
        top = self.statistics.top(2, SortBy.POINTS)
        self.assertEqual(top[0], self.statistics._players[4])
        self.assertEqual(top[1], self.statistics._players[1])
        self.assertEqual(top[2], self.statistics._players[3])

    def test_top_correct_sorting_goals(self):
        top = self.statistics.top(2, SortBy.GOALS)
        self.assertEqual(top[0], self.statistics._players[1])
        self.assertEqual(top[1], self.statistics._players[3])
        self.assertEqual(top[2], self.statistics._players[2])

    def test_top_correct_sorting_assists(self):
        top = self.statistics.top(2, SortBy.ASSISTS)
        self.assertEqual(top[0], self.statistics._players[4])
        self.assertEqual(top[1], self.statistics._players[3])
        self.assertEqual(top[2], self.statistics._players[1])

    def test_top_correct_sorting_invalid_argument(self):
        top = self.statistics.top(2, 42)
        self.assertEqual(top, None)
