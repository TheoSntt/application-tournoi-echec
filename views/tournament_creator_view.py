"""View : View for the Tournaments Manager SubController."""

from models.app_parameters import appParams

class TournamentCreatorView:
    """View for the Tournaments Manager SubController."""
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

        self.MAIN_MENU_PROMPT = ("Que voulez-vous faire ?\n"
                                 "1 - Lister tous les tournois\n"
                                 "2 - Créer un tournoi\n"
                                 "3 - Continuer un tournoi en cours\n"
                                 "4 - Retour au Menu principal\n")
        self.MAIN_MENU_VALUES = ["1", "2", "3", "4"]

        self.SELECTOR_MENU_PROMPT = ("Selectionnez un tournoi pour voir les options \n"
                                     "R - Retour au menu précédent\n"
                                     "A - Retour au Menu Principal\n")
        self.SELECTOR_MENU_VALUES = ["R", "A", "r", "a"]

        self.TOURNAMENT_OPTIONS_PROMPT = ("Tournoi sélectionné :\n"
                                          "<>\n"
                                          "1 - Lister les participants par ordre alphabétique\n"
                                          "2 - Afficher toutes les informations sur le tournoi\n"
                                          "3 - Modifier le tournoi\n"
                                          "4 - Retour au menu des tournois\n")
        self.TOURNAMENT_OPTIONS_VALUES = ["1", "2", "3", "4"]

        self.TOURNAMENT_MODIFYING_OPTIONS_PROMPT = ("Tournoi sélectionné :\n"
                                                    "<>\n"
                                                    "1 - Continuer la saisie des tours\n"
                                                    "2 - Retour au menu des tournois\n")
        self.TOURNAMENT_MODIFYING_OPTIONS_VALUES = ["1", "2"]

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

    # def prompt_main_menu(self):
    #     """Prompt the Tournaments Manager Main Menu."""
    #     user_choice = self.get_correct_input(self.MAIN_MENU_PROMPT, self.MAIN_MENU_VALUES)
    #     return user_choice

    def prompt_for_name(self):
        name = input(self.NAME_PROMPT)
        return name

    def prompt_for_place(self):
        place = input(self.PLACE_PROMPT)
        return place

    def prompt_for_start_date(self):
        date = input(self.DATE_PROMPT)
        if date == "a":
            return "Aujourd'hui"
        else:
            return date

    def prompt_for_players_selection(self, selected_players):
        if len(selected_players) != 0:
            print("JOUEURS SELECTIONNES\n")
            for player in selected_players:
                print(player)
        player_selection = input(self.PLAYER_SELECTION_PROMPT)
        return player_selection

    def prompt_selection_recap(self, selected_players):
        if len(selected_players) != 0:
            print("JOUEURS SELECTIONNES\n")
            for player in selected_players:
                print(player)
        else:
            print("AUCUN JOUEUR SELECTIONNE.")

    def prompt_for_tournament(self, name, place, start_date):
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

    def print_players_for_selection(self, players):
        i = 1
        for player in players:
            print(f"{i} - {str(player)}")
            i += 1

    def pretty_print_decorator(function):
        """Decorator for printing functions."""
        def wrapper(*args, **kwargs):
            print("_________________________")
            function(*args, **kwargs)
            print("_________________________")
            print()

        return wrapper

    @pretty_print_decorator
    def basic_output(self, *args):
        """Basic information printing function."""
        for arg in args:
            if type(arg) is list:
                for element in arg:
                    print(element)
            else:
                print(arg)


