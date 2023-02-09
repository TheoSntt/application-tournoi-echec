"""View : View for the Tournament Creation Module of the Tournaments Controller."""

from models.app_parameters import appParams

class TournamentCreatorView:
    """View for the Tournament Creation Module."""
    def __init__(self):
        """Menus prompts are declared here."""
        self.NAME_PROMPT = "Saisir le nom du tournoi :\n"
        self.PLACE_PROMPT = "Saisir le lieu :\n"
        self.DATE_PROMPT = "Saisir la date de début (Taper a pour la date du jour) :\n"
        self.DESCRIPTION_PROMPT = "Saisir la description du tournoi :\n"
        self.NUMBER_OF_TURN_PROMPT = "Saisir le nombre de tour (Taper a pour valeur par défaut) :\n"
        self.PLAYER_SELECTION_PROMPT = ("Saisir le numéro d'un joueur dans la liste ou son identifiant d'échec\n"
                                        "Vous pouvez en sélectionner plusieurs, séparés par des espaces\n"
                                        "Une fois votre sélection terminée, taper a\n")

    def get_correct_input(self, prompt, accepted_values):
        """Prompt a menu and verifies that the user input is one of the accepted values."""
        while True:
            value = input(prompt)
            if value not in accepted_values:
                print("Veuillez choisir une des options proposées.")
                continue
            else:
                break
        return value

    def prompt_for_name(self):
        """Prompt for the name of the tournament"""
        name = input(self.NAME_PROMPT)
        return name

    def prompt_for_place(self):
        """Prompt for the place where the tournament takes place"""
        place = input(self.PLACE_PROMPT)
        return place

    def prompt_for_start_date(self):
        """Prompt for the start date of the tournament"""
        date = input(self.DATE_PROMPT)
        return date

    def prompt_for_players_selection(self, selected_players):
        """Bellow a printed list of players, show the already selected player and prompt for more player selection."""
        if len(selected_players) != 0:
            print("JOUEURS SELECTIONNES\n")
            for player in selected_players:
                print(player)
            print("\n_________________________")
        player_selection = input(self.PLAYER_SELECTION_PROMPT)
        return player_selection

    def prompt_for_tournament(self, name, place, start_date):
        """Once the name, place and date are set and their unicity is verified,
        prompt for the rest of the information"""
        tournament = {"name": name,
                      "place": place,
                      "start_date": start_date}
        description = input(self.DESCRIPTION_PROMPT)
        tournament["description"] = description
        while True:
            number_of_turns = input(self.NUMBER_OF_TURN_PROMPT)
            if number_of_turns == "a":
                number_of_turns = appParams['DEFAULT_NUMBER_OF_TURNS']
                break
            else:
                try:
                    number_of_turns = int(number_of_turns)
                    break
                except ValueError:
                    print("Veuillez saisir un nombre")
                    continue
        tournament["number_of_turns"] = number_of_turns
        return tournament

    def pretty_print_decorator(function):
        """Decorator for printing functions."""
        def wrapper(*args, **kwargs):
            print("_________________________")
            function(*args, **kwargs)
            print("_________________________")
            print()

        return wrapper

    @pretty_print_decorator
    def print_players_for_selection(self, players):
        """Print the list of players in the app to allow the user to add them to the tournament"""
        i = 1
        for player in players:
            print(f"{i} - {str(player)}")
            i += 1

    @pretty_print_decorator
    def prompt_selection_recap(self, selected_players):
        """Once player selection is over, print a recap of the selected players"""
        if len(selected_players) != 0:
            print("PHASE DE SELECTION DES JOUEURS TERMINEES\nJOUEURS SELECTIONNES\n")
            for player in selected_players:
                print(player)
        else:
            print("AUCUN JOUEUR SELECTIONNE.")

    @pretty_print_decorator
    def basic_output(self, *args):
        """Basic information printing function."""
        for arg in args:
            if type(arg) is list:
                for element in arg:
                    print(element)
            else:
                print(arg)


