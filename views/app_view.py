"""Main View : View for the App Controller."""


class AppView:
    """View for the App Controller."""
    def __init__(self):
        """Menus prompts are declared here."""
        self.MAIN_MENU_PROMPT = ("MENU PRINCIPAL :\n"
                                 "1 - Gestion des joueurs\n"
                                 "2 - Gestion des tournois\n"
                                 "3 - Quitter l'application\n")
        self.MAIN_MENU_VALUES = [1, 2, 3]

    def get_correct_input(self, prompt, accepted_values):
        """Prompt a menu and verifies that the user input is one of the accepted values."""
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
        """Prompt the app Main Menu."""
        user_choice = self.get_correct_input(self.MAIN_MENU_PROMPT, self.MAIN_MENU_VALUES)
        return user_choice