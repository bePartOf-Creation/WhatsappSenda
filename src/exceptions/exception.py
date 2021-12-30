class InvalidPhoneNumberError(Exception):
    def __init__(self, arg):
        message = f"This {arg} provided is Invalid"
        super().__init__(message)


class GeneralError(Exception):
    def __init__(self, arg):
        message = f"Error --> {arg}"
        super().__init__(message)
