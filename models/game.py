"""Define the Game."""


class Game(tuple):
    """The Game object is just a tuple, with a few methods to print to json"""
    def __str__(self):
        if self[0][1] == self[0][0].POINTS_FOR_VICTORY:
            return f"Match entre {str(self[0][0])} (Vainqueur) et {str(self[1][0])}"
        elif self[0][1] == self[0][0].POINTS_FOR_DEFEAT:
            return f"Match entre {str(self[1][0])} (Vainqueur) et {str(self[0][0])}"
        elif self[0][1] == self[0][0].POINTS_FOR_TIE:
            return f"Match entre {str(self[0][0])} et {str(self[1][0])} (Match nul)"
        else:
            return f"Match entre {str(self[0][0])} et {str(self[1][0])} (Erreur : Issue du match inconnue)"

    def get_winner(self):
        if self[0][1] == self[0][0].POINTS_FOR_VICTORY:
            return self[0][0]
        elif self[0][1] == self[0][0].POINTS_FOR_DEFEAT:
            return self[1][0]
        elif self[0][1] == self[0][0].POINTS_FOR_TIE:
            return None
        else:
            return "Issue du match inconnue"

    def to_json(self):
        game = [[self[0][0].to_json(),self[0][1]],[self[1][0].to_json(),self[1][1]]]
        return game


if __name__ == '__main__':
    game = Game(([{'name': "John", 'age': 12}, 0], ["Gary", 1]))
    print(game)
    print(game[0])
    print(game[1])