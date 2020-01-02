from practice_2.enums import Session
from practice_2.exception import InvalidValueException

class Step:
    # __init__(number_of_sessions: int, number_of_stars: string)
    def __init__(self, number_of_sessions, number_of_stars):
        # validate inputs
        if number_of_sessions not in Session.NUMBER_TO_TEXT_MAP:
            raise InvalidValueException("Invalid number of sessions")
        if number_of_stars not in Session.TEXT_TO_NUMBER_MAP:
            raise InvalidValueException("Invalid number of stars")

        self.number_of_sessions = Session.NUMBER_TO_TEXT_MAP[number_of_sessions]
        self.number_of_stars = Session.TEXT_TO_NUMBER_MAP[number_of_stars]

    def make_step(self):
        return "I completed %s sessions and I rated my expert %s stars" % (self.number_of_sessions, self.number_of_stars )