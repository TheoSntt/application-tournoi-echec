"""View : View for the Players Manager SubController."""

from views.ABC_view import View


class PlayersView(View):
    """View for the Players Manager SubController."""
    def __init__(self):
        """Menus prompts are declared here."""
        self.MAIN_MENU_PROMPT = ("Que voulez-vous faire ?\n"
                                 "1 - Lister tous les joueurs (nom, prénom, ID)\n"
                                 "2 - Lister tous les détails de tous les joueurs\n"
                                 "3 - Ajouter un nouveau joueur\n"
                                 "4 - Retour au menu principal\n")
        self.MAIN_MENU_VALUES = [1, 2, 3, 4]

    def prompt_main_menu(self):
        """Prompt the Players Manager Main Menu."""
        user_choice = self.get_correct_input(self.MAIN_MENU_PROMPT, self.MAIN_MENU_VALUES)
        return user_choice

    def prompt_for_chess_id(self):
        """Prompt for a new player's chess_id."""
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

    def prompt_for_player(self, chess_id):
        """Once the unicity of the new player's chess id has been established,
        prompts for the rest of the information."""
        name = input("Saisir le prénom du joueur : ")
        surname = input("Saisir le nom du joueur : ")
        date_of_birth = input("Saisir la date de naissance du joueur : ")
        return {"name": name,
                "surname": surname,
                "chess_id": chess_id,
                "date_of_birth": date_of_birth}

    @View.pretty_print_decorator
    def print_all_players(self, player_list, show_detail=False):
        """Display a list of all players, in a compact or detailed way."""
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
