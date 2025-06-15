class Auto:
    def __init__(self, brand, model, year, engcap, color, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.engcap = engcap
        self.color = color
        self.price = price
    def info(self):
        print(f"\nПредоставляем информацию по автомобилю:\n"
              f"Автомобиль {self.brand} {self.model} {self.year} года выпуска\n"
              f"Имеет объём двигателя {self.engcap} литра\n"
              f"Цвет автомобиля {self.color}\n"
              f"И стоимость автомобиля составляет {self.price} рублей\n")

brandYC = input("\nВведите марку автомобиля >>> ").capitalize()
modelYC = input("\nВведите модель >>> ").capitalize()
yearYC = int(input("\nВведите год выпуска >>> "))
engcapYC = input("\nВведите объём двигателя (в литрах, пример: 2.6) >>> ")
colorYC = input("\nВведите цвет >>> ").lower()
priceYC = int(input("\nВведите цену >>> "))

your_car = Auto(brandYC, modelYC, yearYC, engcapYC, colorYC, priceYC)

act = input("\nВывести информацию вашего авто? Yes(y)/No(any)")
if "y" in act:
    your_car.info()