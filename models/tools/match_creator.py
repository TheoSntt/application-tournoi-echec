"""Create a Match Object from a list object."""


from models.match import Match
from models.tools.player_creator import create_player_from_dict


def create_match_from_list(match_list):
    """Create a Match Object from a list object, imported from JSON"""
    first_list = match_list[0]
    second_list = match_list[1]
    player1 = create_player_from_dict(first_list[0])
    score1 = first_list[1]
    player2 = create_player_from_dict(second_list[0])
    score2 = second_list[1]
    match = Match(([player1, score1], [player2, score2]))
    return match
