count = 0

traffic = ".><.>>.<<"

def check_traffic_right(car, key):
    # Проверка на движение машини в правую сторону, в случае нахождения, мы берём его местоположение в строке
    if car == ">":
        return (True, key)
    else:
        return (False, key)

def check_traffic_left(car, key):
    # Абсолютно такой же принцип, только при движении в обратную сторону
    if car == "<":
        return (True, key)
    else:
        return (False, key)

for key, car in enumerate(list(traffic)):
    checked = check_traffic_right(car, key)
    for on_road in list(traffic)[key:]:
        if checked[0] == True and on_road == ".":
            count += 1
            print(f"{car} => {on_road} => {count}")

for key, car in enumerate(reversed(list(traffic))):
    checked = check_traffic_left(car, key)
    for on_road in list(reversed(list(traffic)))[key:]:
        if checked[0] == True and on_road == ".":
            count += 1
            print(f"{car} => {on_road} => {count}")