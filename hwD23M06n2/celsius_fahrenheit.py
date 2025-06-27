class Convert_temperature:

    count_in_cels = 0
    count_in_fahr = 0

    @staticmethod
    def celsius_in_fahrenheit(cels):
        fahr = (cels * 1.8) + 32
        Convert_temperature.count_in_fahr += 1
        return round(fahr, 1)

    @staticmethod
    def fahrenheit_in_celsius(fahr):
        cels = (fahr - 32) / 1.8
        Convert_temperature.count_in_cels += 1
        return round(cels, 1)

    @staticmethod
    def count_of_conv():
        return Convert_temperature.count_in_cels, Convert_temperature.count_in_fahr

convTemper = Convert_temperature()

print(convTemper.celsius_in_fahrenheit(36.6))
print(convTemper.celsius_in_fahrenheit(38))

print(convTemper.fahrenheit_in_celsius(97.9))

print(f"Было раз посчитано из фаренгейт в цельсии: {convTemper.count_of_conv()[0]}\n"
      f"Было раз посчитано из цельсии в фаренгейт: {convTemper.count_of_conv()[1]}")

