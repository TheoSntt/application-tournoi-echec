"""Entry point. This is the file that runs the app."""

from controllers.app_controller import AppController
from views.app_view import AppView


def main():
    """Main function. This function runs the app."""
    view = AppView()
    session = AppController(view)
    session.run()


if __name__ == "__main__":
    main()
