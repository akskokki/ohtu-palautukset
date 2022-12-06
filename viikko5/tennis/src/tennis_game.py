from player import Player

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.player1.set_opponent(self.player2)
        self.player2.set_opponent(self.player1)
        

    def won_point(self, player_name):
        if self._check_game_over():
            return
        if player_name == self.player1.name:
            self.game_over = self.player1.add_point()
        if player_name == self.player2.name:
            self.game_over = self.player2.add_point()
        

    def get_score(self):
        if self._check_game_over():
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
    
    def _check_game_over(self):
        if self.player1.points >= 5  or self.player2.points >= 5:
            return True
        return False
    
    def _check_deuce_or_more(self):
        if self.player1.points >= 3 and self.player2.points >= 3:
            return True
        return False