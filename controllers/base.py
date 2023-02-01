"""Define the main controller."""

import json
from typing import List
from pprint import pprint

from models.player import Player
from models.tournament import Tournament
from models.tools.player_creator import create_player_from_dict
from controllers.players_controller import PlayersController
from controllers.tournaments_controller import TournamentsController
from views.players_view import PlayersView
from views.tournaments_view import TournamentsView
from models.turn import Turn


class Controller:
    """Main controller."""

    # def __init__(self, deck: Deck, view):
    def __init__(self, view):
        """Has a deck, a list of players and a view."""
        # models
        self.playersController = PlayersController(PlayersView())
        self.tournamentsController = TournamentsController(TournamentsView())
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

    # def get_tournaments(self):
    #     """Retrieve the tournaments stored in JSON and add them to the Controller"""
    #     with open('data/tournaments/tournaments.json', encoding='utf-8') as f:
    #         json_content = json.load(f)
    #         saved_tournaments = json_content["tournaments"]
    #         for saved_tournament in saved_tournaments:
    #             tournament = Tournament(
    #                 name=saved_tournament["name"],
    #                 place=saved_tournament["place"],
    #                 start_date=saved_tournament["start_date"],
    #                 end_date=saved_tournament["end_date"],
    #                 description=saved_tournament["description"],
    #                 number_of_turns=saved_tournament["number_of_turns"],
    #                 current_turn=saved_tournament["current_turn"],
    #                 in_progress=saved_tournament["in_progress"],
    #                 turns_list=saved_tournament["turns_list"],
    #                 players_list=saved_tournament["players_list"])
    #             self.tournaments.append(tournament)

    def write_data_to_json(self):
        """Write the tournaments and player to JSON"""
        # Creating a to_write_tournaments object and writing it to the json file
        self.tournamentsController.write_tournaments_to_json()
        # Creating a to_write_players object and writing it to the json file
        self.playersController.write_players_to_json()

    # def evaluate_game(self):
    #     """Evaluate the best player."""
    #     last_player = self.players[0]
    #     best_candidate = self.players[0]
    #
    #     for player in self.players[1:]:
    #         player_card = player.hand[0]
    #         last_player_card = last_player.hand[0]
    #
    #         if player_card > last_player_card:
    #             best_candidate = player
    #
    #         last_player = player
    #
    #     return best_candidate.name

    # def rebuild_deck(self):
    #     """Rebuild the deck."""
    #     for player in self.players:
    #         while player.hand:
    #             card = player.hand.pop()
    #             card.is_face_up = False
    #             self.deck.append(card)
    #     self.deck.shuffle()

    # def start_game(self):
    #     """Shuffle the deck and makes the players draw a card."""
    #     self.deck.shuffle()
    #     for player in self.players:
    #         card = self.deck.draw_card()
    #         if card:
    #             player.hand.append(card)

    def run(self):
        """Run the game."""
        # self.get_players()
        # self.get_tournaments()
        # print(len(self.tournaments))
        # for tournament in self.tournaments:
        #     print(tournament)
        #     pprint(tournament.to_json())

        self.write_data_to_json()
        print(self.view.get_correct_input(self.view.MAIN_MENU_PROMPT, self.view.MAIN_MENU_VALUES))


        # running = True
        # while running:
        #
        #     self.start_game()
        #     for player in self.players:
        #         self.view.show_player_hand(player.name, player.hand)
        #
        #     self.view.prompt_for_flip_cards()
        #     for player in self.players:
        #         for card in player.hand:
        #             card.is_face_up = True
        #
        #         self.view.show_player_hand(player.name, player.hand)
        #
        #     self.view.show_winner(self.evaluate_game())
        #     running = self.view.prompt_for_new_game()
        #
        #     self.rebuild_deck()
