from bs4 import BeautifulSoup
import requests
url = 'https://www.oreilly.com/radar/'
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
sp = soup.find_all('h2', class_='post-title')
for post in sp:
    print(post.get_text())