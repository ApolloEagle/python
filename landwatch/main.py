from bs4 import BeautifulSoup
import requests

locations = ['']
baseUrl = 'https://www.land.com'

for location in locations:
    url = f'{baseUrl}/{location}/riverfront-property/no-house/under-50000/over-5-acres/is-active/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    content = requests.get(url, headers=headers).text
    soup = BeautifulSoup(content, 'html.parser')

    titles = [title.getText() for title in soup.find_all(
        name="div", class_="_12a2b")]

    listings = [listing.find('a')['href'] for listing in soup.find_all(
        name="div", class_="_12a2b")]

    print('**********')
    print(location)
    print('**********')

    for i in range(0, len(titles)):
        try:
            acres = float(titles[i].split()[0].replace(',', ''))
            price = int(titles[i].split()[3].replace(',', '').replace('$', ''))
        except IndexError:
            pass

        if acres >= 5 and 50000 >= price >= 0:
            print('     ' + baseUrl + listings[i])
