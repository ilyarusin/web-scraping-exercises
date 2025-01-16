from bs4 import BeautifulSoup
import requests

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
models = soup.find_all('a', class_='title')
description = soup.find_all('p', class_='description card-text')
prices = soup.find_all('h4', class_='price float-end card-title pull-right')
with open('laptops.csv', 'w', encoding='utf-8') as file:
    file.write(f'Модель;Описание;Цена\n')
    for m, d, p in zip(models, description, prices):
        file.write(f"{m['title']};{d.get_text()};{p.get_text()}\n")