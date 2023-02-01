"""Player and Hand."""


from models.game import Game
from models.tools.player_creator import create_player_from_dict


def create_game_from_list(game_list):
    """Create a Player object from a dict, imported from JSON"""
    first_list = game_list[0]
    second_list = game_list[1]
    player1 = create_player_from_dict(first_list[0])
    score1 = first_list[1]
    player2 = create_player_from_dict(second_list[0])
    score2 = second_list[1]
    game = Game(([player1, score1], [player2, score2]))
    return game


# class Tools:
#     """Player."""
#
#     def __init__(self):
#         """Has no attribute. Is a helper class"""
#
#     def create_player_from_dict(player_dict):
#         """Create a Player object from a dict, imported from JSON"""
#         player = Player(player_dict["name"],
#                         player_dict["surname"],
#                         player_dict["chess_ID"],
#                         player_dict["date_of_birth"])
#         return player
#
#     def create_tournament_from_dict(tournament_dict):
#         """Create a Tournament object from a dict, imported from JSON"""
#         tournament = Tournament(
#             tournament_dict["name"],
#             tournament_dict["place"],
#             tournament_dict["start_date"],
#             tournament_dict["end_date"],
#             tournament_dict["description"],
#             tournament_dict["number_of_turns"],
#             tournament_dict["current_turn"],
#             tournament_dict["in_progress"],
#             tournament_dict["turns_list"],
#             tournament_dict["players_list"])
#         return tournament
