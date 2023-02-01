"""Player and Hand."""


from models.turn import Turn


def create_turn_from_dict(turn_dict):
    """Create a Player object from a dict, imported from JSON"""
    turn = Turn(name=turn_dict["name"],
                start_time=turn_dict["start_time"],
                end_time=turn_dict["end_time"],
                games=turn_dict["games"])
    return turn
