from bs4 import BeautifulSoup
import requests

url = 'https://www.livelib.ru/genre/%D0%A2%D1%80%D0%B8%D0%BB%D0%BB%D0%B5%D1%80%D1%8B/top'
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.content,'html.parser')
titles = soup.find_all('a', class_='book-item__title')
authors = soup.find_all('a', class_='book-item__author')
rating = soup.find_all('div', class_='book-item__rating')
i = 1
for t, a, r in zip(titles, authors, rating):
    print(f'{i}. "{t.get_text()}", {a.get_text()} - {r.get_text()}')
    i += 1