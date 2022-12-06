from player import Player

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.player1.set_opponent(self.player2)
        self.player2.set_opponent(self.player1)

        self.game_over = False
        

    def won_point(self, player_name):
        if self.game_over:
            return
        if player_name == self.player1_name:
            self.game_over = self.player1.add_point_and_check_win()
        if player_name == self.player2_name:
            self.game_over = self.player2.add_point_and_check_win()
        

    def get_score(self):
        points1 = self.player1.points
        points2 = self.player2.points

        if self.game_over:
            return f"Win for {self._leader().name}"

        if self._check_deuce_or_more():
            if self.player1.points == self.player2.points:
                return "Deuce"
            return f"Advantage {self._leader().name}"
        
        score = f"{self.player1}-"
        
        if self._leader():
            return score + str(self.player2)

        return score + "All"
    
    def _leader(self):
        if self.player1.points > self.player2.points:
            return self.player1
        if self.player2.points > self.player1.points:
            return self.player2
        return None
    
    def _check_deuce_or_more(self):
        if self.player1.points >= 3 and self.player2.points >= 3:
            return True
        return False