import asyncio #Я даже не дошёл до асинхрона, я просто сдался на этом моменте. Слишком сложное для меня задание.
import os

path = input('Введите путь к папке для поиска >>> ')
word = input('Введите слово по которому хотите найти текст >>> ')
all_txt = ""
unread_file = "new_file.txt"
ban_words = []

files = list(os.walk(path))[0][2]
print(files)

with open("banWords.txt", "r", encoding="utf-8") as bw:
    ban_cont = bw.read().split("\n")
    for wrdB in ban_cont:
        if wrdB != "":
            ban_words.append(wrdB)

print(ban_words)

for file in files:
    if unread_file != file:
        with open(os.path.join(path, file), "r", encoding="utf-8") as f:
            content = f.read()
            # for banned in ban_words:
            #     if banned:
            #         content = content.replace(banned, "[данные удалены]")

            if word.lower() in content or word.capitalize() in content:
                all_txt += content

print(all_txt)

with open(os.path.join(path, "new_file.txt"), "w", encoding="utf-8") as nf:
    nf.write(all_txt)

# async def find_files(path_dir, word):
#     ...