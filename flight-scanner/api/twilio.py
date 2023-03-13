import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()


class TwilioAPI:
    def alert(self):
        client = Client(os.getenv('twilioAccountId'), os.getenv('twilioToken'))
        message = client.messages.create(
            body="Hello from Twilio",
            from_=os.getenv('twilioFrom'),
            to=os.getenv('twilioTo')
        )

        return message
