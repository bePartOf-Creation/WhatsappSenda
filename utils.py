import phonenumbers
from fastapi.logger import logger
from exceptions.exception import InvalidPhoneNumberError


def validate_number(my_string_number: str):
    try:
        my_number = phonenumbers.parse(my_string_number)
        logger.info(my_number, "--> {} is a valid")
        return phonenumbers.is_possible_number(my_number)
    except Exception as e:
        print(f"Invalid Number ({my_string_number}) ", e.__str__())


def checkNumbers(numbers: list):
    try:
        validate_numbers = [f"whatsapp:{numb}" for numb in numbers if validate_number(numb)]
        return validate_numbers
    except Exception as e:
        raise InvalidPhoneNumberError(e)


figures = ['+2348139207668', '+2348085690901']

# Testing Utils methods.


if __name__ == '__main__':
    checkNumbers(figures)


