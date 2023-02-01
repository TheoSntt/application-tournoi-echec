"""Entry point."""
# import json
# from models.tournament import Tournament
# from models.player import Player
# from models.turn import Turn
from controllers.base import Controller
from views.base import View


def main():
    view = View()
    session = Controller(view)
    session.run()

    # """Retrieve the players stored in JSON"""
    # with open('data/players/players.json', encoding='utf-8') as f:
    #     json_content = json.load(f)
    #     saved_players = json_content["players"]
    # """Retrieve the tournaments stored in JSON"""
    # with open('data/tournaments/tournaments.json', encoding='utf-8') as f:
    #     json_content = json.load(f)
    #     saved_tournaments = json_content["tournaments"]
    # """Create (and print) the Player Objects from the players stored in JSON"""
    # players = []
    # for saved_player in saved_players:
    #     player = Player(saved_player["name"], saved_player["surname"], saved_player["chess_ID"], saved_player["date_of_birth"])
    #     players.append(player)
    # for player in players:
    #     print(player)
    # """Create (and print) the Tournament Objects from the tournaments stored in JSON"""
    # tournaments = []
    # for saved_tournament in saved_tournaments:
    #     tournament = Tournament(
    #         saved_tournament["name"],
    #         saved_tournament["place"],
    #         saved_tournament["start_date"],
    #         saved_tournament["end_date"],
    #         saved_tournament["description"],
    #         saved_tournament["number_of_turns"],
    #         saved_tournament["current_turn"],
    #         saved_tournament["in_progress"],
    #         saved_tournament["turns_list"],
    #         saved_tournament["players_list"])
    #     tournaments.append(tournament)
    # for tournament in tournaments:
    #     for player in tournament.players_list:
    #         print(player)

    # with open('data/tournaments/tournaments.json', 'w', encoding='utf-8') as f:
    #     json.dump(tournaments, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
