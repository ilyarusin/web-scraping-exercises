from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.livelib.ru/book/1002978643-ohotnik-za-tenyu-donato-karrizi'
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
sp = soup.find('div', class_='bc-menu__book-cover book-cover')
img_url = re.findall(r'(?:https\:)?//.*\.(?:jpeg)', str(sp))[0]
response = requests.get(img_url, headers=headers)
if response.status_code == 200:
    file_name = url.split('-', 1)[1]
    with open(file_name + '.jpeg', 'wb') as file:
        file.write(response.content)