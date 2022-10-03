from bs4 import BeautifulSoup
import requests
import json

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
}
url = "https://dota2.ru/items"
host = "https://dota2.ru/"
html = requests.get(url, headers=headers)

soup = BeautifulSoup(html.text, 'lxml')

info = []
main_info_items = []

items = soup.find_all("div", class_="base-items__shop-descr-wrap")
for item in items[:167]:
    image = host + item.find('img').attrs['src']
    item_info = item.find("div", class_="base-items__shop-descr-top").find_all('p')
    name = item_info[0].text
    if len(item_info) > 1:
        cost = item_info[1].text.strip()
    else:
        cost = 0

    info.append({
        "Image_url": image,
        "Name": name,
        "Cost": int(cost)
    })

with open("items.json", "w", encoding="utf-8") as file:
    json.dump(info, file, indent=4, ensure_ascii=False)

print(len(info))

