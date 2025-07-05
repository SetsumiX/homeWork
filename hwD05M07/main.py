import heapq

words = ["Трамвай", "Ком", "Машинист", "Огонь", "ТВ", "Берёза", "Вагонетка", "Безделушка", "Фарш", "Колонка", "Телефон", "Воздух", "Я", "Меч", "Колесо"]

data = []

for k, i in enumerate(words):
    data.append({
        "word": i,
        "len": len(i),
        "key": k,
    })

print(data)

_sortHeap_words = []

for c in data:
    heapq.heappush(_sortHeap_words, (c["len"], c["key"], c["word"]))

while _sortHeap_words:
    leng, key, word = heapq.heappop(_sortHeap_words)
    print(f"{key}. {word} - длинна составляет {leng} букв")