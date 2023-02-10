"""Main View : View for the App Controller."""

from views.ABC_view import View


class AppView(View):
    """View for the App Controller."""
    def __init__(self):
        """Menus prompts are declared here."""
        self.MAIN_MENU_PROMPT = ("MENU PRINCIPAL :\n"
                                 "1 - Gestion des joueurs\n"
                                 "2 - Gestion des tournois\n"
                                 "3 - Quitter l'application\n")
        self.MAIN_MENU_VALUES = ["1", "2", "3"]

    def prompt_main_menu(self):
        """Prompt the app Main Menu."""
        user_choice = self.get_correct_input(self.MAIN_MENU_PROMPT, self.MAIN_MENU_VALUES)
        return user_choice
