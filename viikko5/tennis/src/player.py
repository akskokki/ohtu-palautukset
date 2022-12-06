class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.opponent = None
    
    def set_opponent(self, opponent):
        self.opponent = opponent
    
    def add_point(self):
        if self.points == 3:
            if self.opponent.points == 4:
                self.opponent.deuce()
                return
            if self.opponent.points < 3:
                self.points = 5
                return
        
        self.points += 1
    
    def deuce(self):
        self.points = 3
    
    def __repr__(self):
        if self.points == 0:
            return "Love"
        if self.points == 1:
            return "Fifteen"
        if self.points == 2:
            return "Thirty"
        if self.points == 3:
            return "Forty"
        return ""