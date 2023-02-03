"""Define the Player Object."""


class Player:
    """Players are stored independently in JSON. Tournaments include Players in their players_list variable."""
    def __init__(self, name, surname, chess_id, date_of_birth, score=0):
        """Has a name, surname, chess_id, date_of_birth, and score."""
        self.name = name
        self.surname = surname
        self.chess_id = chess_id
        self.date_of_birth = date_of_birth
        self.score = score
        # Application variables
        self.POINTS_FOR_VICTORY = 1
        self.POINTS_FOR_TIE = 0.5
        self.POINTS_FOR_DEFEAT = 0

    def __str__(self):
        """Used in print."""
        return f"{self.name} {self.surname} ({self.chess_id})"

    def __repr__(self):
        """Used in print."""
        return f"{self.name} {self.surname}\n{self.chess_id}\n{self.date_of_birth}"

    def to_json(self, include_score=False):
        """Used to write player to JSON."""
        if include_score:
            player = {
                'name': self.name,
                'surname': self.surname,
                'chess_id': self.chess_id,
                'date_of_birth': self.date_of_birth,
                'score': self.score
            }
        else:
            player = {
                'name': self.name,
                'surname': self.surname,
                'chess_id': self.chess_id,
                'date_of_birth': self.date_of_birth
            }
        return player

    def win_a_game(self):
        self.score += self.POINTS_FOR_VICTORY
        print(f"Yay, {self} won a game !")

    def tie_a_game(self):
        self.score += self.POINTS_FOR_TIE
        print(f"Hum, {self} tied !")
