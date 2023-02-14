"""Define the Players Manager Subcontroller."""

import json
from typing import List
from models.player import Player


class PlayersController:
    """Players Manager Subcontroller."""
    def __init__(self, view, appcontroller):
        """Has a list of players, a view, and a reference to the App Controller."""
        self.players: List[Player] = []
        self.view = view
        self.appController = appcontroller

    def create_player_from_dict(self, player_dict):
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

    def get_players(self):
        """Retrieve the players stored in JSON and add them to the Controller"""
        with open('data/players/players.json', encoding='utf-8') as f:
            json_content = json.load(f)
            saved_players = json_content["players"]
            for saved_player in saved_players:
                player = self.create_player_from_dict(saved_player)
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
            new_player = self.create_player_from_dict(player)
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

    def show_main_menu(self):
        """Show the Tournament Manager Main Menu and handle the user choice."""
        main_menu_user_choice = self.view.prompt_main_menu()
        if main_menu_user_choice == "1":
            self.print_all_players()
        elif main_menu_user_choice == "2":
            self.print_all_players(show_detail=True)
        elif main_menu_user_choice == "3":
            self.create_new_player()
        elif main_menu_user_choice == "4":
            self.appController.show_main_menu()

    def run(self):
        """Function called by the AppController. Runs the Subcontroller."""
        self.show_main_menu()
