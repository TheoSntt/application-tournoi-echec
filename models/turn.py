"""Define the Deck."""


import time
from models.tools.game_creator import create_game_from_list


class Turn:
    """Deck of cards."""

    def __init__(self, name, games, start_time=time.time(), end_time=0):
        """Has a name, start_time, end_time, and includes matches."""
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.games = []
        for game in games:
            game_object = create_game_from_list(game)
            self.games.append(game_object)

    def to_json(self):
        """Used to write turn to JSON."""
        turn = {
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "games": []
        }
        for game in self.games:
            turn['games'].append(game.to_json())

        return turn


if __name__ == '__main__':
    games = [
            [
              [{"name": "Jean", "surname": "Bon", "date_of_birth": "1994/11/03", "chess_ID": "AA12345"}, 0],
              [{"name": "Sylvie", "surname": "Culture", "date_of_birth": "1996/03/21", "chess_ID": "AA12346"}, 1]
            ],
            [
              [{"name": "Paul", "surname": "Pogba", "date_of_birth": "1988/01/31", "chess_ID": "AA12347"}, 0],
              [{"name": "Sylvie", "surname": "Vartan", "date_of_birth": "1993/02/16", "chess_ID": "AB12345"}, 1]
            ]
          ]
    test = Turn("Tour test", games)
    print(test.name)
    print(test.start_time)
    print(test.to_json())
    for game in test.games:
        print(game)
        print(game.to_json())
        # print(game[0][1])
        # print(game[1][0])
        # print(game[1][1])
