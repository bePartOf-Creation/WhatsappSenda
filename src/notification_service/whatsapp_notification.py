from decouple import config
import logging
from twilio.rest import Client
from exceptions.exception import InvalidPhoneNumberError
from utils import validate_number
from model.notification_model import Message, message_data, data


class SendWhatsappNotification:
    def __init__(self, payloads):
        logging.info("PAYLOAD WAS PASSED --> {}", payloads)
        self.payload = payloads
        logging.info("PAYLOAD INITIALISED --> {}", self.payload)


    @classmethod
    def _checkNumbers(cls, numbers: list):
        try:
            validate_numbers = [f"whatsapp:{num}" for num in numbers if validate_number(num)]
            return validate_numbers
        except Exception as e:
            raise InvalidPhoneNumberError(num)

    def send_whatsapp_message(self, payload : list = None):
        logging.info("LIST OF MESSAGE PAYLOAD WAS PASSED --> {}", payload)
        account_sid = config('SSAF_TEST_ACCOUNT_SID')
        auth_token = config('SSAF_TEST_AUTH_TOKEN')
        logging.info("CONNECTION RUNNING")
        client = Client(account_sid, auth_token)
        logging.info("TWILIO CLIENT HAS BEEN INITIALISED --> {}", client)
        try:
            for each_data in payload:
                valid_numbers = SendWhatsappNotification._checkNumbers(each_data.get('user_number'))
                print("NUMBER VALIDATION -> {}", valid_numbers)
                logging.info("Whatsapp Message Initiating...")
                for recipent_number in valid_numbers:
                    client.messages.create(
                        body=each_data['body'],
                        from_=each_data['ssaf_number'],
                        to=recipent_number
                    )
            print("Whatsapp Notification sent")
        except InvalidPhoneNumberError as e:
            print(e.__str__())


if __name__ == '__main__':
    notification = SendWhatsappNotification(message_data)
    notification.send_whatsapp_message(message_data)
