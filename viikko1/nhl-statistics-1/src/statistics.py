from sort_by import SortBy

def sort_by_points(player):
    return player.points

def sort_by_goals(player):
    return player.goals

def sort_by_assists(player):
    return player.assists


class Statistics:
    def __init__(self, reader):
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sorting=SortBy.POINTS):
        if sorting == SortBy.POINTS:
            sort_key = sort_by_points
        elif sorting == SortBy.GOALS:
            sort_key = sort_by_goals
        elif sorting == SortBy.ASSISTS:
            sort_key = sort_by_assists
        else:
            return None

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_key
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
