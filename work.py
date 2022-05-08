from bs4 import BeautifulSoup
import requests
req = requests.get('https://wall.alphacoders.com/by_category.php?id=3&name=Anime+Wallpapers')
soup = BeautifulSoup(req.content, 'html.parser')
for i in soup.find_all('img'):
    file = i.get('src')
    t = file.split('/')[-1]
    print(t)
    with open(t, "wb") as f:
        f.write(requests.get(file).content)