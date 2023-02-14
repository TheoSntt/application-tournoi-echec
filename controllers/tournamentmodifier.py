"""Define the Tournament modification Module of the Tournaments Controller."""

from models.appparameters import appParams
from datetime import datetime


class TournamentModifier:
    """Tournaments Modification module. Allow turn generation, and the input of match results"""
    def __init__(self, view, tournamentscontroller):
        """Has a view, and a reference to the Tournaments Controller."""
        self.view = view
        self.tournamentsController = tournamentscontroller

    def assess(self, tournament):
        """Assess the situation of the tournament to modify : Is the last Turn finished or still in progress ?"""
        if not tournament.turns_list:
            # Tournament is newly created. Prompt for turn creation.
            create_turn = self.view.prompt_for_turn_creation(new=True)
            if create_turn:
                tournament.generate_new_turn()
                self.tournamentsController.write_tournaments_to_json()
                self.assess(tournament)
            else:
                self.tournamentsController.run()
        else:
            # Tournament is not new. Assess if the last turn is still in progress
            turn_in_progress = None
            for turn in tournament.turns_list:
                if turn.end_time is None:
                    turn_in_progress = turn
            if turn_in_progress is None:
                # Last turn is over. Must create a new turn. Except if tournament has reach its max turn number
                if len(tournament.turns_list) == tournament.number_of_turns:
                    # Tournament is over
                    now = datetime.now()
                    tournament_end = f"{str(now.year)}/{str(now.month).rjust(2, '0')}/{str(now.day).rjust(2, '0')}"
                    tournament.end_date = tournament_end
                    tournament.in_progress = False
                    self.tournamentsController.write_tournaments_to_json()
                    self.view.basic_output("TOURNOI TERMINE")
                    self.view.print_tournament_details(tournament)
                    self.tournamentsController.run()
                else:
                    # Last turn is over and tournament is not finished. Prompt for new turn creation
                    create_turn = self.view.prompt_for_turn_creation()
                    if create_turn:
                        tournament.generate_new_turn()
                        self.tournamentsController.write_tournaments_to_json()
                        self.assess(tournament)
                    else:
                        self.tournamentsController.run()
            else:
                # Last turn still in progress. Prompt for the matches results.
                self.prompt_for_turn_results(turn_in_progress, tournament)

    def prompt_for_turn_results(self, turn, tournament):
        """Allow the user to input the result of the matches of a turn"""
        self.view.basic_output(turn)
        for match in turn.matches:
            if match[0][1] is None and match[1][1] is None:
                # The match results are not set
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
                elif match_winner == "4":
                    self.tournamentsController.run()
                    return
                self.tournamentsController.write_tournaments_to_json()
        now = datetime.now()
        turn_end = f"{str(now.hour).rjust(2, '0')}:{str(now.minute).rjust(2, '0')}"
        turn.end_time = turn_end
        tournament.current_turn += 1
        self.tournamentsController.write_tournaments_to_json()
        self.view.basic_output("TOUR TERMINE - RECAPITULATIF", turn)
        self.assess(tournament)

    def run(self):
        """Function called by the AppController. Runs the Subcontroller."""
        pass
