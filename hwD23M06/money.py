class Money:
    def __init__(self, rubles):
        self.rubles = rubles
        self.usd = 0.012786 * rubles
        self.euro = 0.01091 * rubles

    def show_rub(self):
        money_arr = str(round(float(self.rubles), 2)).split(".")

        if len(money_arr[1]) == len(range(1)):
            money_arr[1] += "0"

        print(f"У вас в кошельке {money_arr[0]} рублей {money_arr[1]} копеек.")

    def show_in_usd(self):
        money_arr_rub = str(round(float(self.rubles), 2)).split(".")
        money_arr_usd = str(round(float(self.usd), 2)).split(".")

        if len(money_arr_rub[1]) == len(range(1)):
            money_arr_rub[1] += "0"

        if len(money_arr_usd[1]) == len(range(1)):
            money_arr_usd[1] += "0"

        print(f"{money_arr_rub[0]} рублей {money_arr_rub[1]} копеек = {money_arr_usd[0]} долларов {money_arr_usd[1]} центов.")

    def show_in_euro(self):
        money_arr_rub = str(round(float(self.rubles), 2)).split(".")
        money_arr_eu = str(round(float(self.euro), 2)).split(".")

        if len(money_arr_rub[1]) == len(range(1)):
            money_arr_rub[1] += "0"

        if len(money_arr_eu[1]) == len(range(1)):
            money_arr_eu[1] += "0"

        print(f"{money_arr_rub[0]} рублей {money_arr_rub[1]} копеек = {money_arr_eu[0]} евро {money_arr_eu[1]} центов.")

myMoney = Money(100.1)
myMoney.show_rub()
myMoney.show_in_usd()
myMoney.show_in_euro()