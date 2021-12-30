from unittest import TestCase

from model.notification_model import data, message_data
from notification_service.whatsapp_notification import SendWhatsappNotification
from utils import *


class TestSendWhatsappNotification(TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        print("close.....")

    def test_ThatUser_phoneNUmber_IsValid(self):
        valid_user_phone_number = validate_number("+2348085690901")
        valid_user_phone_number1 = validate_number("+2349043910175")
        valid_user_phone_number2 = validate_number("+447852379439")
        assert valid_user_phone_number == True
        assert valid_user_phone_number1 == True
        assert valid_user_phone_number2 == True

    def test_That__User_phoneNumber_Is_InValid(self):
        valid_user_phone_number = validate_number("e0856kfkfkfkf90901")
        valid_user_phone_number1 = validate_number("+e490kkkk3910175")
        valid_user_phone_number2 = validate_number("+99989447852379439")
        self.assertFalse(valid_user_phone_number)
        self.assertFalse(valid_user_phone_number1)
        self.assertFalse(valid_user_phone_number2)


    def test_ThatUser_PhoneNumber_Is_A_Valid_Twilio_Number(self):
        test_data = data
        valid_user_phone_number = SendWhatsappNotification._checkNumbers(test_data['user_number'])
        assert len(valid_user_phone_number) == 2
        assert valid_user_phone_number == ['whatsapp:+2348139207668', 'whatsapp:+2348085690901']

    def test_That_MultipleMessage_Was_Sent_Successfully(self):
        test_data = message_data
        notification = SendWhatsappNotification(message_data)
        message_sent_successfully = notification.send_whatsapp_message(test_data)
        print(message_sent_successfully)
        assert message_sent_successfully is None
