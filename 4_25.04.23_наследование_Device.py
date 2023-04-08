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


class CoffeeMachine(Device):
    def __init__(self, name: str, power: int, voltage: int, colour: str, date_manufacture: Dict[str, str],
                 pressure: int, number_drinks: int = None):
        super().__init__(name, power, voltage, colour, date_manufacture)
        self.__pressure = pressure
        self.__number_drinks = number_drinks

class Blender(Device):
    def __init__(self, name: str, power: int, voltage: int, colour: str, date_manufacture: Dict[str, str],
                 type_blender: str, number_speeds: int = None):
        super().__init__(name, power, voltage, colour, date_manufacture)
        self.__type_blender = type_blender
        self.__number_speeds = number_speeds

def execute_application():
    pass




if __name__ == "__main__":
    execute_application()