"""Define the main controller."""

import json
from typing import List
from pprint import pprint

from models.player import Player
from models.tools.player_creator import create_player_from_dict


class PlayersController:
    """Main controller."""

    # def __init__(self, deck: Deck, view):
    def __init__(self, view):
        """Has a deck, a list of players and a view."""
        # models
        self.players: List[Player] = []
        # self.deck = deck

        # views
        self.view = view

    def get_players(self):
        """Retrieve the players stored in JSON and add them to the Controller"""
        with open('data/players/players.json', encoding='utf-8') as f:
            json_content = json.load(f)
            saved_players = json_content["players"]
            for saved_player in saved_players:
                player = create_player_from_dict(saved_player)
                self.players.append(player)
        # for player in self.players:
        #     print(player)

    def write_players_to_json(self):
        """Write the players to JSON"""
        to_write_players = {"players": []}
        for player in self.players:
            to_write_players["players"].append(player.to_json(include_score=False))
        # pprint(to_write_players)
        with open('data/players/players.json', 'w', encoding='utf-8') as f:
            json.dump(to_write_players, f, ensure_ascii=False, indent=2)

    def just_add_a_player(self, name, surname, chess_id, date_of_birth):
        player = create_player_from_dict({"name": name,
                                          "surname": surname,
                                          "chess_id": chess_id,
                                          "date_of_birth": date_of_birth})
        self.players.append(player)

    def create_new_player(self):

        must_prompt = True
        while must_prompt:
            already_exist = False
            chess_id = self.view.prompt_for_chess_id()
            for player in self.players:
                if chess_id == player.chess_id:
                    print("Cet identifiant existe déjà :")
                    print(player)
                    already_exist = True
            if already_exist:
                continue
            else:
                must_prompt = False

        player = self.view.prompt_for_player(chess_id)

        if player:
            self.players.append(create_player_from_dict(player))
            self.write_players_to_json()

    def run(self):
        """Run the game."""

        # print(len(self.tournaments))
        # for tournament in self.tournaments:
        #     print(tournament)
        #     pprint(tournament.to_json())



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
