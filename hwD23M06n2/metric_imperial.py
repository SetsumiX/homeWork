class Convert_measures:

    @staticmethod
    def meter_in_yard(meter):
        yard = meter / 0.914
        return round(yard, 1)

    @staticmethod
    def yard_in_meter(yard):
        meter = yard * 0.914
        return round(meter, 1)

convMeasure = Convert_measures()

print(f"{convMeasure.meter_in_yard(5)} ярдов.")

print(f"{convMeasure.yard_in_meter(5)} метров.")

