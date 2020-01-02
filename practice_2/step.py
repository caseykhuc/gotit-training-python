from enums import Session
from exception import InvalidValueException

class Step():
    # __init__(number_of_sessions: int, number_of_stars: string)
    def __init__(self, number_of_sessions, number_of_stars):
        # validate inputs
        if number_of_sessions not in Session.NUMBER_TO_TEXT_MAP or number_of_stars not in Session.TEXT_TO_NUMBER_MAP:
            raise InvalidValueException("Invalid number of sessions")

        self.number_of_sessions = number_of_sessions
        self.number_of_stars = number_of_stars

    def make_step(self):
        return Session.NUMBER_TO_TEXT_MAP[self.number_of_sessions], Session.TEXT_TO_NUMBER_MAP[self.number_of_stars]


# print(Step(2, 'five').make_step())
try:
    print(Step(2, 'five').make_step())
except InvalidValueException as e:
    print(e)
