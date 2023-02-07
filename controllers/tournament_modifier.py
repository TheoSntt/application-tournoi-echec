"""Define the Tournaments Manager Subcontroller."""


class TournamentModifier:
    """Tournaments Manager Subcontroller."""
    def __init__(self, view, tournamentscontroller):
        """Has a deck, a list of players and a view."""
        self.view = view
        self.tournamentsController = tournamentscontroller

    def show_main_menu(self, tournament):
        """Show the Tournament Modifier Main Menu and handle the user choice."""
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

    def assess(self, tournament):
        """Assess the situation of the tournament to modify : Is the last Turn finished or still in progress ?"""
        turn_in_progress = None
        for turn in tournament.turns_list:
            if turn.end_time is None:
                turn_in_progress = turn
        if turn_in_progress is None:
            print("Ok, donc le dernier tour est fini. Il faut donc ajouter des tours")
        else:
            print("OK, donc on a quitté l'application au milieu d'un tour. On reprend le tour en cours.")


    def run(self):
        """Function called by the AppController. Runs the Subcontroller."""
        self.show_main_menu()



