class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nat):
        players = self.reader.get_players()
        players_nat = list(filter(lambda x: x.nationality == nat, players))
        players_nat.sort(key=lambda p: p.total, reverse=True)

        return players_nat