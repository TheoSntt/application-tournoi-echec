"""Base view."""
from pprint import pprint

class PlayersView:
    """Card game view."""

    def __init__(self):
        self.MAIN_MENU_PROMPT = ("Que voulez-vous faire ?\n"
                                 "1 - Lister tous les joueurs (nom, prénom, ID)\n"
                                 "2 - Lister tous les détails de tous les joueurs\n"
                                 "3 - Ajouter un nouveau joueur\n"
                                 "4 - Retour au menu principal\n")
        self.MAIN_MENU_VALUES = [1, 2, 3, 4]

        # def validate_user_input(self, input, accepted_values):
    #     """Check if the user imput is one of the expected values"""
    #     if input in accepted_values:
    #         return True
    #     return False

    def get_correct_input(self, prompt, accepted_values):
        while True:
            try:
                value = int(input(prompt))
            except ValueError:
                print("Veuillez choisir une des options proposées.")
                continue
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

    def prompt_for_chess_id(self):
        """Prompt for a new players infos."""
        while True:
            value = input("Saisir l'identifiant d'échec du joueur : ")
            if len(value) != 7:
                print("L'identifiant n'a pas le format correct : AA12345.")
                print(value[2:])
                print(value[:2])
                continue
            else:
                break
        return value

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

    def prompt_for_player(self, chess_id):
        name = input("Saisir le prénom du joueur : ")
        surname = input("Saisir le nom du joueur : ")
        date_of_birth = input("Saisir la date de naissance du joueur : ")
        return {"name": name,
                "surname": surname,
                "chess_id": chess_id,
                "date_of_birth": date_of_birth}

    @pretty_print_decorator
    def print_all_players(self, player_list, show_detail=False):
        if show_detail:
            player_list.sort(key=lambda x: x.surname)
            print("LISTE DE TOUS LES JOUEURS ENREGISTRES DANS L'APPLICATION")
            print()
            for player in player_list:
                print(repr(player))
                print()
        else:
            player_list.sort(key=lambda x: x.surname)
            print("LISTE DE TOUS LES JOUEURS ENREGISTRES DANS L'APPLICATION")
            print()
            for player in player_list:
                print(player)

