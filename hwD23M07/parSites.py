import requests
from bs4 import BeautifulSoup
import os

tags_txt = ["title", "h1", "h2", "p"]
response = requests.get("https://steamcommunity.com/sharedfiles/filedetails/?id=2949154689")

content_txt = {}
content_img = {}

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    for i in tags_txt:
        el = soup.find(i)
        if el:
            content_txt[i] = el.get_text()
        else:
            content_txt[i] = "Не найден"

    print("Заголовок страницы -", content_txt[tags_txt[0]])
    print("Заголовок h1 -", content_txt[tags_txt[1]])
    print("Заголовок h2 -", content_txt[tags_txt[2]])
    print("Текст страницы -", content_txt[tags_txt[3]])

    if not os.path.isdir("source"):
        os.mkdir("source")

    if not os.path.isdir(os.path.join("source", "images")):
        os.mkdir(os.path.join("source", "images"))

    count = 0
    for img in soup.find_all("img"):
        count += 1
        img_url = img.get("src")

        try:
            img_data = requests.get(img_url).content
            filename = os.path.join("source", "images", img_url.split("/")[-1])
            with open(os.path.join("source", "images", f"{count}.jpg") ,"wb") as file:
                file.write(img_data)
        except Exception as e:
            print(f"Произошла ошибка с {img_url}: {e}")

    for k, tg in enumerate(tags_txt):
        with open(os.path.join("source", f"{tg}.txt"), "w", encoding="utf-8") as file:
            file.write(content_txt[tags_txt[k]])

else:
    print("Ошибка чтения страницы", response.status_code)