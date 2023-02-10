"""Define the Tournaments Manager Subcontroller."""

import json
from typing import List
from pprint import pprint
from models.tournament import Tournament
from controllers.tournament_modifier import TournamentModifier
from controllers.tournament_creator import TournamentCreator
from views.tournament_modifier_view import TournamentModifierView
from views.tournament_creator_view import TournamentCreatorView


class TournamentsController:
    """Tournaments Manager Subcontroller."""
    def __init__(self, view, appcontroller):
        """Has a list of tournaments, a view, a reference to the App Controller, and 2 submodules."""
        self.tournaments: List[Tournament] = []
        self.view = view
        self.appController = appcontroller
        self.tournamentModifier = TournamentModifier(TournamentModifierView(), self)
        self.tournamentCreator = TournamentCreator(TournamentCreatorView(), self)

    def get_tournaments(self):
        """Retrieve the tournaments stored in JSON and add them to the Controller."""
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
        """Write the tournaments to JSON."""
        to_write_tournaments = {"tournaments": []}
        for tournament in self.tournaments:
            to_write_tournaments["tournaments"].append(tournament.to_json())
        with open('data/tournaments/tournaments.json', 'w', encoding='utf-8') as f:
            json.dump(to_write_tournaments, f, ensure_ascii=False, indent=2)

    def print_tournaments_for_selection(self, in_progress=False):
        """List all tournaments saved in the app."""
        if in_progress:
            in_progress_list = []
            for tournament in self.tournaments:
                if tournament.in_progress:
                    in_progress_list.append(tournament)
            self.view.print_tournaments_for_selection(in_progress_list)
            self.show_tournament_selector_menu(in_progress_list, modify=True)
        else:
            self.view.print_tournaments_for_selection(self.tournaments)
            self.show_tournament_selector_menu(self.tournaments)

    def create_new_tournament(self):
        """Handle the creation of a new tournament in the data."""
        self.tournamentCreator.create_tournament()

    def show_tournament_selector_menu(self, tournaments, modify=False):
        """After a list of tournaments is displayed, show the tournament selector menu and handle the user choice."""
        selector_user_choice = self.view.prompt_selector_menu(len(tournaments))
        try:
            index = int(selector_user_choice)-1
            selected_tournament = tournaments[index]
            if modify:
                self.show_tournament_modifying_options(selected_tournament)
            else:
                self.show_tournament_options(selected_tournament)
        except ValueError:
            if selector_user_choice.capitalize() == "R":
                self.show_main_menu()
            elif selector_user_choice.capitalize() == "A":
                self.appController.run()
            else:
                print(f"Erreur ! Choix utilisateur : {selector_user_choice}")

    def list_tournament_players(self, tournament):
        """List all the player in a tournament and has the view display them."""
        self.view.print_all_players(tournament.players_list)
        self.show_tournament_options(tournament)

    def show_tournament_details(self, tournament):
        """Send the selected tournament to the view for it to display all information about the tournament."""
        self.view.print_tournament_details(tournament)
        self.show_tournament_options(tournament)

    def show_tournament_modifying_options(self, tournament):
        """Show the tournament options menu for tournament modification and handle the user choice."""
        options_user_choice = self.view.prompt_tournament_modifying_options(str(tournament))
        if options_user_choice == "1":
            self.tournamentModifier.assess(tournament)
        elif options_user_choice == "2":
            self.show_main_menu()

    def show_tournament_options(self, tournament):
        """Show the tournament options menu and handle the user choice."""
        options_user_choice = self.view.prompt_tournament_options(str(tournament))
        if options_user_choice == "1":
            self.list_tournament_players(tournament)
        elif options_user_choice == "2":
            self.show_tournament_details(tournament)
        elif options_user_choice == "3":
            self.show_main_menu()

    def show_main_menu(self):
        """Show the Tournament Manager Main Menu and handle the user choice."""
        main_menu_user_choice = self.view.prompt_main_menu()
        if main_menu_user_choice == "1":
            # User choice : Print all tournaments
            self.print_tournaments_for_selection()
        elif main_menu_user_choice == "2":
            # User choice : Create new tournaments
            self.create_new_tournament()
        elif main_menu_user_choice == "3":
            # User choice : Modify a tournament in progress
            self.print_tournaments_for_selection(in_progress=True)
        elif main_menu_user_choice == "4":
            # User choice : Back to Main Menu
            self.appController.show_main_menu()

    def run(self):
        """Function called by the AppController. Runs the Subcontroller."""
        self.show_main_menu()



