"""Abstract class for views. Implement the functions all views use throughout the app."""

from abc import ABC, abstractmethod


class View(ABC):
    """The View class has all the functions common to all the views in the app."""
    def pretty_print_decorator(function):
        """Decorator for printing functions."""
        def wrapper(*args, **kwargs):
            print("_________________________")
            function(*args, **kwargs)
            print("_________________________")
            print()

        return wrapper

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

    @pretty_print_decorator
    def basic_output(self, *args):
        """Basic information printing function."""
        for arg in args:
            if type(arg) is list:
                for element in arg:
                    print(element)
            else:
                print(arg)

