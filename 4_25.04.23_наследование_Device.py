from typing import Dict

# Наследование

# Создайте класс Device, который содержит информацию об устройстве.
# С помощью механизма наследования, реализуйте класс CoffeeMachine
# (содержит информацию о кофемашине), класс Blender (содержит информацию
# о блендере).

class Device:
    def __init__(self, name: str, power: int, voltage: int, colour: str, date_manufacture: Dict[str, str]):
        self.__name = name
        self.__power = power
        self.__voltage = voltage
        self.__colour = colour
        self.__date_manufacture = date_manufacture.copy()

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def power(self):
        return self.__power
    @power.setter
    def power(self, power: int):
        self.__power = power

    @property
    def voltage(self):
        return self.__voltage
    @voltage.setter
    def voltage(self, voltage: int):
        self.__voltage = voltage

    @property
    def colour(self):
        return self.__colour
    @colour.setter
    def colour(self, colour: str):
        self.__colour = colour

    @property
    def date_manufacture(self):
        return self.__date_manufacture.values()
    @date_manufacture.setter
    def date_manufacture(self, date_manufacture: Dict[str, str]):
        self.__date_manufacture = date_manufacture.copy()

    def info(self):
        print(f"Класс: {self.__class__.__name__} \n"
              f"Наименование изделия: {self.__name} \n"
              f"Мощность: {self.__power} \n"
              f"Напряжение: {self.__voltage} \n"
              f"Цвет: {self.__colour} \n"
              f"Дата изготовления: {list(self.__date_manufacture.values())}")


class CoffeeMachine(Device):
    def __init__(self, name: str, power: int, voltage: int, colour: str, date_manufacture: Dict[str, str],
                 pressure: int, number_drinks: int = None):
        super().__init__(name, power, voltage, colour, date_manufacture)
        self.__pressure = pressure
        self.__number_drinks = number_drinks

    @property
    def pressure(self):
        return self.__pressure
    @pressure.setter
    def pressure(self, pressure: int):
        self.__pressure = pressure

    @property
    def number_drinks(self):
        return self.__number_drinks
    @number_drinks.setter
    def number_drinks(self, number_drinks: int):
        self.__number_drinks = number_drinks

    def info(self):
        super().info()
        print(f"Давление: {self.__pressure} \n"
              f"Количество напитков: {self.__number_drinks}")


class Blender(Device):

    def __init__(self, name: str, power: int, voltage: int, colour: str, date_manufacture: Dict[str, str],
                 type_blender: str, number_speeds: int = None):
        super().__init__(name, power, voltage, colour, date_manufacture)
        self.__type_blender = type_blender
        self.__number_speeds = number_speeds

    @property
    def type_blender(self):
        return self.__type_blender

    @type_blender.setter
    def type_blender(self, type_blender: str):
        self.__type_blender = type_blender

    @property
    def number_speeds(self):
        return self.__number_speeds

    @number_speeds.setter
    def number_speeds(self, number_speeds: int):
        self.__number_speeds = number_speeds

    def info(self):
        super().info()
        print(f"Тип блендера: {self.__type_blender} \n"
              f"Количество скоростей: {self.__number_speeds}")


def execute_application():

    coffeeMachine = CoffeeMachine("Кофемашина", 2000, 220, "белая", {"число": 12,"месяц": "января", "год": 2022}, 19, 5)
    coffeeMachine.info()
    print()

    blender = Blender("Блендер", 1500, 220, "черный", {"число": 5,"месяц": "октября", "год": 2021}, "погружной", 15)
    blender.info()

if __name__ == "__main__":
    execute_application()