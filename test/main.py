from api import sheety, twilio, tequila

prices = sheety.SheetyAPI()
message = twilio.TwilioAPI()
flights = tequila.TequilaAPI()


def update_prices():
    items = prices.get()["prices"]
    for item in items:
        if (item["iataCode"] == ''):
            prices.put({
                'price': {
                    'iataCode': ''
                }
            }, item['id'])


print(flights.get('DEN')["locations"])
