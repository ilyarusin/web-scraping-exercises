from bs4 import BeautifulSoup
import requests

url = 'https://habr.com/ru/news/'
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
           "Accept-Language": "ru-RU"}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.content,'html.parser')
articles = soup.find_all('a', class_='tm-title__link')
for a in articles:
    print(f'{a.get_text()}\nhttps://habr.com{a.get("href")}')