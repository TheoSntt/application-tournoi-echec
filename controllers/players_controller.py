"""Define the main controller."""

import json
from typing import List
from pprint import pprint

from models.player import Player
from models.tools.player_creator import create_player_from_dict
from controllers.ABC_controller import SubController


class PlayersController:
    """Main controller."""

    # def __init__(self, deck: Deck, view):
    def __init__(self, view, appController):
        """Has a deck, a list of players and a view."""
        self.players: List[Player] = []
        self.view = view
        self.appController = appController

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
        """Was a test function : TO REMOVE"""
        player = create_player_from_dict({"name": name,
                                          "surname": surname,
                                          "chess_id": chess_id,
                                          "date_of_birth": date_of_birth})
        self.players.append(player)

    def create_new_player(self):
        """Handle the creation of a new player in the data"""
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
            new_player = create_player_from_dict(player)
            self.players.append(new_player)
            self.write_players_to_json()
            # print("Nouveau joueur ajouté :")
            # print(repr(new_player))
            # print("_________________________")
            # print()
            self.view.basic_output("Nouveau joueur ajouté :", repr(new_player))

        self.run()

    def print_all_players(self, show_detail=False):
        """List all players saved in the app. With or without details (date of birth)"""
        if show_detail:
            self.view.print_all_players(self.players, show_detail=True)
        else:
            self.view.print_all_players(self.players)

        self.run()


    def run(self):
        """Main function of the subcontroller : runs itself."""
        main_menu_user_choice = self.view.prompt_main_menu()
        if main_menu_user_choice ==1:
            self.print_all_players()
        elif main_menu_user_choice ==2:
            self.print_all_players(show_detail=True)
        elif main_menu_user_choice ==3:
            self.create_new_player()
        elif main_menu_user_choice ==4:
            self.appController.run()
