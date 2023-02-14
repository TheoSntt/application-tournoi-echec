"""Define the Tournament Object."""


from models.player import Player
from models.turn import Turn
from models.match import Match
from models.appparameters import appParams
from random import randrange
from datetime import datetime
import math


class Tournament:
    """The Tournament Class is the main class of the App Model. It includes all other classes."""
    def __init__(self, name, place, start_date, end_date, description, players_list, turns_list,
                 number_of_turns=appParams['DEFAULT_NUMBER_OF_TURNS'],
                 current_turn=0,
                 in_progress=True):
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
            player_object = Player(name=player["name"],
                                   surname=player["surname"],
                                   chess_id=player["chess_id"],
                                   date_of_birth=player["date_of_birth"],
                                   score=player["score"])
            self.players_list.append(player_object)
        # Generate the Turn list
        self.turns_list = []
        for turn in turns_list:
            # For each Turn in the Turn list, we must generate the Match objects, that include Players objects
            matches_list = []
            for match in turn["matches"]:
                # For each match, retrieve the first player from the players list
                id1 = match[0][0]["chess_id"]
                for player in self.players_list:
                    if player.chess_id == id1:
                        player1 = player
                        break
                # For each match, retrieve the second player from the players list
                id2 = match[1][0]["chess_id"]
                for player in self.players_list:
                    if player.chess_id == id2:
                        player2 = player
                        break
                # Create the Match Object with the Players within and adding it to the Turn object Match list.
                match_object = Match(([player1, match[0][1]], [player2, match[1][1]]))
                matches_list.append(match_object)
            # We can now create the Turn object, including Match objects including Players objects
            turn_object = Turn(name=turn["name"],
                               start_time=turn["start_time"],
                               end_time=turn["end_time"],
                               matches=matches_list)
            self.turns_list.append(turn_object)

        self.number_of_turns = number_of_turns
        self.current_turn = current_turn
        self.in_progress = in_progress

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
        tournament_str += "\n\nLISTE DES JOUEURS :\n"
        i = 1
        self.players_list.sort(key=lambda x: x.score, reverse=True)
        for player in self.players_list:
            tournament_str += f"{i} - {str(player)} - Score final : {player.score}\n"
            i += 1
        tournament_str += "\n\nLISTE DES TOURS DE JEU :\n"
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
        """Create a new Turn obect. Main feature is to pair the player in the turn matches."""
        # Generating the matches for the new turn
        number_of_match = math.floor(len(self.players_list)/2)
        # Creating a copy of the player list so Players can be pop() from it
        players_list = []
        self.players_list.sort(key=lambda x: x.score, reverse=True)
        for player in self.players_list:
            players_list.append(player)
        matches = []
        # Testing if the players have scores already or if it is the first match
        if players_list[0].score == 0:
            # In the situation where everyone's score is 0. Pair the player randomly.
            for i in range(number_of_match):
                player1 = players_list.pop(randrange(len(players_list)))
                player2 = players_list.pop(randrange(len(players_list)))
                matches.append(Match(([player1, None], [player2, None])))
        else:
            # It isn't the first match. Pairing the Players, considering their score, and previous pairings.
            for i in range(number_of_match):
                # Removing the first player (the highest score) from the list, in order to find its partner.
                player1 = players_list.pop(0)
                # Retrieve the previous adversaries of the player
                previous_adversaries = []
                for turn in self.turns_list:
                    for match in turn.matches:
                        if match[0][0] == player1:
                            previous_adversaries.append(match[1][0])
                            break
                        elif match[1][0] == player1:
                            previous_adversaries.append(match[0][0])
                            break
                # Now looping through the other players to find the highest scoring player not previously faced.
                perfect_match = None
                for player in players_list:
                    if player not in previous_adversaries:
                        perfect_match = players_list.pop(players_list.index(player))
                        break
                if perfect_match:
                    # If there is such a match, create it with this perfect pair
                    matches.append(Match(([player1, None], [perfect_match, None])))
                else:
                    # All the players already faced each other. Pit the 2 highest scores together.
                    player2 = players_list.pop(0)
                    matches.append(Match(([player1, None], [player2, None])))

        # Now that the matches are done, creating the Turn Object itself
        turn_name = f"Round {len(self.turns_list)+1}"
        now = datetime.now()
        turn_start = f"{str(now.hour).rjust(2, '0')}:{str(now.minute).rjust(2, '0')}"
        turn = Turn(name=turn_name,
                    start_time=turn_start,
                    end_time=None,
                    matches=matches)
        self.turns_list.append(turn)
        # self.current_turn += 1
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
