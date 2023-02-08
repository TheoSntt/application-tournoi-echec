"""Define the Tournament Object."""


from models.tools.player_creator import create_player_from_dict
from models.tools.turn_creator import create_turn_from_dict
from models.app_parameters import appParams
from random import randrange
from datetime import datetime
import math


class Tournament:
    """The Tournament Class is the main class of the App Model. It includes all other classes."""
    def __init__(self, name, place, start_date, end_date, description, players_list, turns_list,
                 number_of_turns=appParams['DEFAULT_NUMBER_OF_TURNS'],
                 current_turn=1, in_progress=True):
        """Has a name, place, start and end date, description, number of turns, current turn, in progress."""
        """Has a players_list and a turns_list that include respectively Player objects and Turn objects"""
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        # Generate the Player list
        self.players_list = []
        for player in players_list:
            player_object = create_player_from_dict(player)
            self.players_list.append(player_object)
        # Generate the Turn list
        self.turns_list = []
        for turn in turns_list:
            turn_object = create_turn_from_dict(turn)
            self.turns_list.append(turn_object)

        self.number_of_turns = number_of_turns
        self.current_turn = current_turn
        self.in_progress = in_progress

        # self.hand: List[Card] = Hand()

    def __str__(self):
        """Used to print tournament name and dates in a list."""
        if self.end_date is None:
            return f"{self.name}, débuté le {self.start_date}, et encore en cours."
        return f"{self.name}, du {self.start_date} au {self.end_date}"

    def __repr__(self):
        """Used to print all the tournament details and information."""
        tournament_str = ""
        if self.end_date is False:
            tournament_str += f"{self.name.capitalize()}\nDébuté le {self.start_date}, et encore en cours.\n"
        else:
            tournament_str += f"{self.name.capitalize()}\nDu {self.start_date} au {self.end_date}\n"
        tournament_str += self.description
        tournament_str += f"\n\nLISTE DES JOUEURS :\n"
        i = 1
        self.players_list.sort(key=lambda x: x.score, reverse=True)
        for player in self.players_list:
            tournament_str += f"{i} - {str(player)} - Score final : {player.score}\n"
            i += 1
        tournament_str += f"\n\nLISTE DES TOURS DE JEU :\n"
        for turn in self.turns_list:
            tournament_str += f"{str(turn)}\n"
        return tournament_str

    def list_players(self):
        """Used to print all the players of the tournament in alphabetical order."""
        player_list = []
        for player in self.players_list:
            player_list.append(str(player))
        # print(player_list)
        return player_list

    def generate_new_turn(self):
        try:
            number_of_match = math.floor(len(self.players_list)/2)
        except ValueError:
            print("Problème : le tournoi a un nombre de joueur impair")
        players_list = []
        for player in self.players_list:
            players_list.append(player)
        matches = []
        for i in range(number_of_match):
            player1 = players_list.pop(randrange(len(players_list)))
            player2 = players_list.pop(randrange(len(players_list)))
            matches.append(([player1.to_json(), 0], [player2.to_json(), 0]))
        turn_name = f"Round {len(self.turns_list)+1}"
        now = datetime.now()
        turn_start = f"{str(now.hour).rjust(2, '0')}:{str(now.minute).rjust(2, '0')}"
        turn = create_turn_from_dict({"name": turn_name,
                                      "start_time": turn_start,
                                      "end_time": None,
                                      "matches": matches})
        self.turns_list.append(turn)
        return turn

    def to_json(self):
        """Used to write tournament to JSON."""
        tournament = {"name": self.name,
                      "place": self.place,
                      "start_date": self.start_date,
                      "end_date": self.end_date,
                      "description": self.description,
                      "number_of_turns": self.number_of_turns,
                      "current_turn": self.current_turn,
                      "in_progress": self.in_progress,
                      "turns_list": [],
                      "players_list": []
                      }
        for player in self.players_list:
            tournament['players_list'].append(player.to_json(include_score=True))
        for turn in self.turns_list:
            tournament['turns_list'].append(turn.to_json())

        return tournament
