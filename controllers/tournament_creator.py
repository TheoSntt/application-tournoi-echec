"""Define the Tournament Creation module of the Tournaments Subcontroller."""

from models.tournament import Tournament
from datetime import datetime


class TournamentCreator:
    """Tournament Creation Module."""
    def __init__(self, view, tournamentscontroller):
        """Has a view and a reference to the Tournament Controller."""
        self.view = view
        self.tournamentsController = tournamentscontroller

    def create_tournament(self):
        """Main function, called by the Tournaments Controller. Runs all the steps to create a tournament."""
        must_prompt = True
        while must_prompt:
            already_exist = False
            name = self.view.prompt_for_name()
            place = self.view.prompt_for_place()
            start_date = self.view.prompt_for_start_date()
            if start_date == "a":
                now = datetime.now()
                start_date = f"{str(now.year)}/{str(now.month).rjust(2, '0')}/{str(now.day).rjust(2, '0')}"
            for tournament in self.tournamentsController.tournaments:
                if name == tournament.name and start_date == tournament.start_date and place == tournament.place:
                    self.view.basic_output("Ce tournoi existe déjà :\n\n", repr(tournament))
                    already_exist = True
            if already_exist:
                continue
            else:
                must_prompt = False

        tournament = self.view.prompt_for_tournament(name, place, start_date)
        new_tournament = Tournament(name=tournament["name"],
                                    place=tournament["place"],
                                    start_date=tournament["start_date"],
                                    end_date=None,
                                    description=tournament["description"],
                                    number_of_turns=tournament["number_of_turns"],
                                    current_turn=0,
                                    in_progress=True,
                                    turns_list=[],
                                    players_list=[])
        # Saving the tournaments info to JSON
        self.tournamentsController.tournaments.append(new_tournament)
        self.tournamentsController.write_tournaments_to_json()
        # Adding the players
        self.tournamentsController.appController.playersController.players.sort(key=lambda x: x.surname)
        self.add_players(new_tournament, self.tournamentsController.appController.playersController.players)
        self.tournamentsController.write_tournaments_to_json()
        self.tournamentsController.tournamentModifier.assess(new_tournament)

    def add_players(self, tournament, players):
        selected_players = []
        keep_prompting = True
        while keep_prompting:
            self.view.print_players_for_selection(players)
            # self.player_selection_process(players)
            player_selection = self.view.prompt_for_players_selection(selected_players)
            selection_list = player_selection.split()
            for input in selection_list:
                try:
                    index = int(input)-1
                    selected_players.append(players[index])
                except ValueError:
                    if len(input) == 7:
                        # Input is a player ID
                        for player in players:
                            if player.chess_id == input:
                                selected_players.append(player)
                                break
                    elif input == "a":
                        # Selection is over
                        keep_prompting = False
                    else:
                        self.view.basic_output("Problème, mauvais input")
                        continue
        tournament.players_list = selected_players
        self.view.prompt_selection_recap(selected_players)

    def player_selection_process(self, players):
        selected_players = []
        while True:
            self.view.prompt_for_players_selection()

    def run(self):
        """Function called by the AppController. Runs the Subcontroller."""
        pass



