"""Define the Match Object."""

from models.appparameters import appParams


class Match(tuple):
    """The Match class is just a tuple, with a few methods to print infos in console and export to json"""
    def __str__(self):
        """Used in print."""
        if self[0][1] == appParams['POINTS_FOR_VICTORY'] and self[1][1] == appParams['POINTS_FOR_DEFEAT']:
            return f"Match entre {str(self[0][0])} (Vainqueur) et {str(self[1][0])}"
        elif self[0][1] == appParams['POINTS_FOR_TIE'] and self[1][1] == appParams['POINTS_FOR_TIE']:
            return f"Match entre {str(self[0][0])} et {str(self[1][0])} (Match nul)"
        elif self[0][1] == appParams['POINTS_FOR_DEFEAT'] and self[1][1] == appParams['POINTS_FOR_VICTORY']:
            return f"Match entre {str(self[1][0])} (Vainqueur) et {str(self[0][0])}"
        else:
            return f"Match entre {str(self[0][0])} et {str(self[1][0])} : MATCH EN COURS"

    def get_winner(self):
        """Get the winner of the match"""
        if self[0][1] == appParams['POINTS_FOR_VICTORY']:
            return self[0][0]
        elif self[1][1] == appParams['POINTS_FOR_VICTORY']:
            return self[1][0]
        elif self[0][1] == appParams['POINTS_FOR_TIE'] and self[1][1] == appParams['POINTS_FOR_TIE']:
            return None
        else:
            return "Match en cours"

    def to_json(self):
        """Export the match to a dict format, so it can be written to JSON"""
        match = [[self[0][0].to_json(), self[0][1]], [self[1][0].to_json(), self[1][1]]]
        return match
