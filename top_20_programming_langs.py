import requests
from lxml import html

url = 'https://www.tiobe.com/tiobe-index/'
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
page = requests.get(url, headers=headers)
tree = html.fromstring(page.content)
languages, rating = [], []
for i in range(1, 21):
    languages.append(tree.xpath(f'//*[@id="top20"]/tbody/tr[{i}]/td[5]/text()')[0])
    rating.append(tree.xpath(f'//*[@id="top20"]/tbody/tr[{i}]/td[6]/text()')[0])
i = 1
for l, r in zip(languages, rating):
    print(f'{i}. {l}: {r}')
    i += 1