"""Entry point. This is the file that runs the app."""

from controllers.appcontroller import AppController
from views.appview import AppView


def main():
    """Main function. This function creates the app Controller and its view, then run it."""
    view = AppView()
    session = AppController(view)
    session.run()


if __name__ == "__main__":
    main()
