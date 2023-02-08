"""Define the Tournaments Manager Subcontroller."""

from models.app_parameters import appParams
from datetime import datetime


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
            print("Ok, donc le dernier tour est fini. Il faut donc ajouter des tours."
                  "A moins que le tournoi ne soit fini.")
            if len(tournament.turns_list) == tournament.number_of_turns:
                print("Le tournoi est terminée. Todo : Faire afficher a la vue que le tournoi est terminé")
                now = datetime.now()
                tournament_end = f"{str(now.year)}/{str(now.month).rjust(2, '0')}/{str(now.day).rjust(2, '0')}"
                tournament.end_date = tournament_end
                tournament.in_progress = False
                self.tournamentsController.write_tournaments_to_json()
                print(repr(tournament))
                self.tournamentsController.run()
            else:
                print("TODO : Faire afficher un truc à la vue genre Oui blabla on crée un nouveau tour.")
                tournament.generate_new_turn()
                self.tournamentsController.write_tournaments_to_json()
                self.assess(tournament)
        else:
            self.prompt_for_turn_results(turn_in_progress, tournament)

    def prompt_for_turn_results(self, turn, tournament):
        """Allow the user to input the result of the matches of a turn"""
        print("TODO : Faire afficher un récap à la vue sur le tour")
        print(turn)
        for match in turn.matches:
            match_winner = self.view.prompt_for_match_winner(match)
            if match_winner == "1":
                match[0][0].win_a_game()
                match[0][1] = appParams["POINTS_FOR_VICTORY"]
                match[1][0].lose_a_game()
                match[1][1] = appParams["POINTS_FOR_DEFEAT"]
            elif match_winner == "2":
                match[1][0].win_a_game()
                match[1][1] = appParams["POINTS_FOR_VICTORY"]
                match[0][0].lose_a_game()
                match[0][1] = appParams["POINTS_FOR_DEFEAT"]
            elif match_winner == "3":
                match[0][0].tie_a_game()
                match[0][1] = appParams["POINTS_FOR_TIE"]
                match[1][0].tie_a_game()
                match[1][1] = appParams["POINTS_FOR_TIE"]
        now = datetime.now()
        turn_end = f"{str(now.hour).rjust(2, '0')}:{str(now.minute).rjust(2, '0')}"
        turn.end_time = turn_end
        self.tournamentsController.write_tournaments_to_json()
        self.assess(tournament)

    def run(self):
        """Function called by the AppController. Runs the Subcontroller."""
        self.show_main_menu()



