"""Base view."""


class TournamentsView:
    """Card game view."""

    def __init__(self):
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

        # def validate_user_input(self, input, accepted_values):
    #     """Check if the user imput is one of the expected values"""
    #     if input in accepted_values:
    #         return True
    #     return False

    def get_correct_input(self, prompt, accepted_values):
        while True:
            value = input(prompt)
            if value not in accepted_values:
                print("Veuillez choisir une des options proposées.")
                continue
            else:
                break
        return value

    def prompt_main_menu(self):
        """Prompt app main menu."""
        user_choice = self.get_correct_input(self.MAIN_MENU_PROMPT, self.MAIN_MENU_VALUES)
        return user_choice

    def prompt_selector_menu(self, number_of_tournaments):
        """Prompt app main menu."""
        values = self.SELECTOR_MENU_VALUES
        for i in range(1, number_of_tournaments+1):
            values.append(str(i))
        # print(values)
        user_choice = self.get_correct_input(self.SELECTOR_MENU_PROMPT, values)
        return user_choice

    def prompt_tournament_options(self):
        """Prompt app main menu."""
        user_choice = self.get_correct_input(self.TOURNAMENT_OPTIONS_PROMPT, self.TOURNAMENT_OPTIONS_VALUES)
        return user_choice

    def pretty_print_decorator(function):
        def wrapper(*args, **kwargs):
            print("_________________________")
            function(*args, **kwargs)
            print("_________________________")
            print()

        return wrapper

    @pretty_print_decorator
    def basic_output(self, *args):
        for arg in args:
            print(arg)

    @pretty_print_decorator
    def print_all_tournaments(self, tournaments_list):
        tournaments_list.sort(key=lambda x: x.start_date)
        print("LISTE DE TOUS LES TOURNOIS ENREGISTRES DANS L'APPLICATION")
        print()
        i = 1
        for tournament in tournaments_list:
            print(f"{i} - {tournament}")
            i += 1

    @pretty_print_decorator
    def print_tournament_details(self, tournament):
        print(repr(tournament))