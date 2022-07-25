class Engine:

    def __init__(self, power, volume) -> None:
        self.__power = power
        self.__volume = volume

    def get_power(self):
        return self.__power

    def get_volume(self):
        return self.__volume

    power = property(get_power)
    volume = property(get_volume)

class Car:

    def __init__(self, make, model) -> None:
        self.__make = make
        self.__model = model

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    make = property(get_make)
    model = property(get_model)


class SuperCar(Car):

    def __init__(self, make, model, power, volume) -> None:
        super().__init__(make, model)
        self.__engine = Engine(power, volume)

    def get_engine(self):
        return self.__engine

    # def get_power(self):                          as an option
    #     return self.__engine.get_power()

    # def get_volume(self):
    #     return self.__engine.get_volume()

    
    engine = property(get_engine)


class SerialCar(Car):

    def __init__(self, make, model, engine) -> None:
        super().__init__(make, model)
        self.__engine = engine

    def get_engine(self):
        return self.__engine

    def set_engine(self, engine):
        self.__engine = engine

    engine = property(get_engine, set_engine)



super_car = SuperCar("Ferrari", "la Ferrari", 300, 12)

print(super_car.engine.volume)

v4 = Engine(100, 3.6)

camry = SerialCar("toyota", "camry", v4)
print(camry.engine.volume)

v8 = Engine(250, 8)

camry.engine = v8
print(camry.engine.volume)

input()