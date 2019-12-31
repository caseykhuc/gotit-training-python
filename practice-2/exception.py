class InvalidValueException(Exception):
    # message: string
    # __init__(message: string)
    def __init__(self, message):
        self.message = message