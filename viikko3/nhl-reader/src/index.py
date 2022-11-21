import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        if player_dict['nationality'] == 'FIN':
            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists']
            )
            players.append(player)

    players.sort(key=lambda p: p.total, reverse=True)    

    for player in players:
        print(player)

if __name__ == "__main__":
    main()