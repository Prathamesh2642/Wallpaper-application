import requests
from bs4 import BeautifulSoup

page = "https://hdqwalls.com/latest-wallpapers"
tree = requests.get(page)
soup = BeautifulSoup(tree.content, 'html.parser')
imgs = [a.find('img') for a in soup.find_all("a", {"class": "caption hidden-md hidden-sm hidden-xs"}) if a.find('img')]
team = [img.get('alt') for img in imgs]

print(imgs)
print(team)
