from bs4 import BeautifulSoup
import requests

ycomb = requests.get("https://news.ycombinator.com/show").text
soup = BeautifulSoup(ycomb, 'html.parser')

titles = [title.getText()
          for title in soup.find_all(name="span", class_="titleline")]
links = [link.find("a")["href"]
         for link in soup.find_all(name="span", class_="titleline")]
scores = [int(score.getText().split()[0])
          for score in soup.find_all(name="span", class_="score")]

index = scores.index(max(scores))

print(titles[index])
print(links[index])
