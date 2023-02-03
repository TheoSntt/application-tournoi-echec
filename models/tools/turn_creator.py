"""Create a Turn Object from a dictionary."""


from models.turn import Turn


def create_turn_from_dict(turn_dict):
    """Create a Turn object from a dict, imported from JSON"""
    turn = Turn(name=turn_dict["name"],
                start_time=turn_dict["start_time"],
                end_time=turn_dict["end_time"],
                matches=turn_dict["matches"])
    return turn
