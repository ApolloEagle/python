from api import sheety, twilio, tequila, currency

prices = sheety.SheetyAPI()
message = twilio.TwilioAPI()
flights = tequila.TequilaAPI()
curr = currency.CurrencyAPI()


def update_iata_codes():
    items = prices.get()["prices"]
    index = 2
    for item in items:
        if (item['iataCode'] == ''):
            locations = flights.get_iata(item["city"])["locations"][0]
            prices.put({
                'price': {
                    'iataCode': locations["code"]
                },
            }, index)
            index += 1


def flight_alert():
    items = prices.get()["prices"]
    for item in items:
        if (item['iataCode'] != ''):
            price = flights.search_flights(
                fly_from=item["departureCityCode"], fly_to=item["iataCode"])['data'][0]["price"]

            dollars = curr.convert(
                from_country='EUR', to_country='USD', amount=price)

            print(f'{item["city"]}: ${int(dollars["result"])}')


update_iata_codes()
flight_alert()
