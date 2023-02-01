"""Player and Hand."""


from models.player import Player


def create_player_from_dict(player_dict):
    """Create a Player object from a dict, imported from JSON"""
    if "score" in player_dict:
        player = Player(name=player_dict["name"],
                        surname=player_dict["surname"],
                        chess_id=player_dict["chess_id"],
                        date_of_birth=player_dict["date_of_birth"],
                        score=player_dict["score"])
    else:
        player = Player(name=player_dict["name"],
                        surname=player_dict["surname"],
                        chess_id=player_dict["chess_id"],
                        date_of_birth=player_dict["date_of_birth"])
    return player

