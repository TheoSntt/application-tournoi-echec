"""Define the main controller."""

import json
from typing import List
from pprint import pprint
from models.tournament import Tournament


class TournamentsController:
    """Main controller."""

    # def __init__(self, deck: Deck, view):
    def __init__(self, view, appController):
        """Has a deck, a list of players and a view."""
        self.tournaments: List[Tournament] = []
        self.view = view
        self.appController = appController

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

    def print_all_tournaments(self):
        """List all players saved in the app. With or without details (date of birth)"""
        self.view.print_all_tournaments(self.tournaments)
        self.show_tournament_selector_menu(len(self.tournaments))

    def create_new_tournament(self):
        """Handle the creation of a new tournament in the data"""
        print("Menu de création d'un tournoi à faire")

        self.run()

    def show_tournaments_in_progress(self):
        """Allow to continue a tournament in progress"""
        print("Menu de modification d'un tournoi à faire")

        self.run()

    def show_tournament_selector_menu(self, number_of_tournaments):
        """Show the tournament selector menu and handle the user choice"""
        selector_user_choice = self.view.prompt_selector_menu(number_of_tournaments)
        try:
            index = int(selector_user_choice)-1
            selected_tournament = self.tournaments[index]
            self.show_tournament_options(selected_tournament)
        except ValueError:
            if selector_user_choice.capitalize() == "R":
                self.show_main_menu()
            elif selector_user_choice.capitalize() == "A":
                self.appController.run()
            else:
                print(f"Erreur ! Choix utilisateur : {selector_user_choice}")

    def list_tournament_players(self, tournament):
        for player in tournament.players_list:
            self.view.basic_output(player)
        self.show_tournament_options(tournament)

    def show_tournament_details(self, tournament):
        self.view.print_tournament_details(tournament)
        self.show_tournament_options(tournament)

    def show_tournament_options(self, tournament):
        """Show the tournament options menu and handle the user choice"""
        options_user_choice = self.view.prompt_tournament_options()
        if options_user_choice == "1":
            self.list_tournament_players(tournament)
        elif options_user_choice == "2":
            self.show_tournament_details(tournament)
        elif options_user_choice == "3":
            print("Menu de modification d'un tournoi à faire")
        elif options_user_choice == "4":
            self.show_main_menu()

    def show_main_menu(self):
        """Show the Tournament Manager Main Menu and handle the user choice"""
        main_menu_user_choice = self.view.prompt_main_menu()
        if main_menu_user_choice == "1":
            # User choice : Print all tournaments
            self.print_all_tournaments()
        elif main_menu_user_choice == "2":
            # User choice : Create new tournaments
            self.create_new_tournament()
        elif main_menu_user_choice == "3":
            # User choice : Modify a tournament in progress
            self.show_tournaments_in_progress()
        elif main_menu_user_choice == "4":
            # User choice : Back to Main Menu
            self.appController.run()

    def run(self):
        """Function called by the AppController. Runs the Subcontroller"""
        self.show_main_menu()



