from typing import List

from pydantic import BaseModel


class BaseMessage(BaseModel):
    body: str
    ssaf_number: str
    user_number: List[str]


class Message(BaseModel):
    data: List[BaseMessage]


message_data = [
    {
        "body": "SSAF TEST MESSAGE: The Item Is Delivered",
        "ssaf_number": 'whatsapp:+14155238886',
        "user_number": ['+2348085690901', '+2348085690901', '+2348085690901', '+2348085690901', '+2348085690901']
    },
    {
        "body": "SSAF TEST MESSAGE:The Shipment is Currently At Minnesota Office",
        "ssaf_number": 'whatsapp:+14155238886',
        "user_number": ['+2348085690901', '+2348085690901', '+2348085690901']
    }
]
data = {
    "body": "The Item Is Delivered",
    "ssaf_number": 'whatsapp:+14155238886',
    "user_number": ['+2348139207668', '+2348085690901']
}
