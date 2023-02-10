"""Define the main controller : the one that runs the app."""

from controllers.players_controller import PlayersController
from controllers.tournaments_controller import TournamentsController
from views.players_view import PlayersView
from views.tournaments_view import TournamentsView


class AppController:
    """Main controller."""
    def __init__(self, view):
        """Has 2 subcontrollers and a view."""
        # subcontrollers
        self.playersController = PlayersController(PlayersView(), self)
        self.tournamentsController = TournamentsController(TournamentsView(), self)
        # view
        self.view = view

    def write_data_to_json(self):
        """Write the tournaments and player to JSON"""
        # Creating a to_write_tournaments object and writing it to the json file
        self.tournamentsController.write_tournaments_to_json()
        # Creating a to_write_players object and writing it to the json file
        self.playersController.write_players_to_json()

    def show_main_menu(self):
        """Show the App Main Menu and handle the user choice."""
        main_menu_user_choice = self.view.prompt_main_menu()
        if main_menu_user_choice == "1":
            self.playersController.run()
        elif main_menu_user_choice == "2":
            self.tournamentsController.run()
        else:
            return

    def run(self):
        """Run the App."""
        self.playersController.get_players()
        self.tournamentsController.get_tournaments()
        self.show_main_menu()

