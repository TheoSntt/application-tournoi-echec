"""Define the main controller."""

import json
from typing import List
from pprint import pprint
from models.tournament import Tournament


class TournamentsController:
    """Main controller."""

    # def __init__(self, deck: Deck, view):
    def __init__(self, view):
        """Has a deck, a list of players and a view."""
        # models
        self.tournaments: List[Tournament] = []
        self.get_tournaments()
        # self.deck = deck

        # views
        self.view = view

    # def get_players(self):
    #     """Retrieve the players stored in JSON and add them to the Controller"""
    #     with open('data/players/players.json', encoding='utf-8') as f:
    #         json_content = json.load(f)
    #         saved_players = json_content["players"]
    #         for saved_player in saved_players:
    #             player = create_player_from_dict(saved_player)
    #             self.players.append(player)
    #     # for player in self.players:
    #     #     print(player)

    def get_tournaments(self):
        """Retrieve the tournaments stored in JSON and add them to the Controller"""
        with open('data/tournaments/tournaments.json', encoding='utf-8') as f:
            json_content = json.load(f)
            saved_tournaments = json_content["tournaments"]
            for saved_tournament in saved_tournaments:
                tournament = Tournament(
                    name=saved_tournament["name"],
                    place=saved_tournament["place"],
                    start_date=saved_tournament["start_date"],
                    end_date=saved_tournament["end_date"],
                    description=saved_tournament["description"],
                    number_of_turns=saved_tournament["number_of_turns"],
                    current_turn=saved_tournament["current_turn"],
                    in_progress=saved_tournament["in_progress"],
                    turns_list=saved_tournament["turns_list"],
                    players_list=saved_tournament["players_list"])
                self.tournaments.append(tournament)

    def write_tournaments_to_json(self):
        """Write the tournaments to JSON"""
        to_write_tournaments = {"tournaments": []}
        for tournament in self.tournaments:
            to_write_tournaments["tournaments"].append(tournament.to_json())
        pprint(to_write_tournaments)
        with open('data/tournaments/tournaments.json', 'w', encoding='utf-8') as f:
            json.dump(to_write_tournaments, f, ensure_ascii=False, indent=2)

    def run(self):
        """Run the game."""


