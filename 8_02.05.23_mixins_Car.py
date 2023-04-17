

# 9.6 Объектно-ориентированное программирование
# Миксины

# Используя механизм множественного наследования разработайте класс
# «Автомобиль». Создайте несколько классов-наследников согласно
# классификации. Используя классы-миксины «примешайте» к классам
# наследникам методы, которые выводят информацию об объекте из классов
# «Колесо», «Двигатель», «Двери» и т.п.



class Engine: #двигатель
    def __init__(self):
        self.__state = False

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value: bool):
        self.__state = value

    def print_state(self):
        return "Двигатель заведен" if self.__state else "Двигатель не заведен"

class GasEngine(Engine):
    pass

class DieselEngine(Engine):
    pass

# миксин
class EngineState:    # состояние двигателя (включен или не включен)
    @staticmethod
    def get_state(engine: Engine):
        print(engine.print_state())



class Door: # дверь
    def __init__(self):
        self.__position = True

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value: bool):
        self.__position = value

    def print_position(self):
        return "Дверь закрыта" if self.__position else "Дверь открыта"

class OpenForward(Door):   #  открывается вперед
    pass

class OpenUp(Door):        #  открывается вверх
    pass

# миксин
class DoorPosition:
    @staticmethod
    def get_position(door: Door):
        print(door.print_position())

class Car(EngineState, DoorPosition):
    def __init__(self, brand: str, year: int, color: str):
        self.__brand = brand
        self.__year = year
        self.__color = color

    def __str__(self):
        return f"Марка: {self.__brand} год: {self.__year} цвет: {self.__color}"

def execute_application():

    engine = DieselEngine()
    car = Car("BMW", 2009, "black")
    print(car)
    car.get_state(engine)

    door = OpenForward()
    car.get_position(door)

    engine.state = True
    car.get_state(engine)
    door.position = False
    car.get_position(door)


if __name__ == "__main__":
    execute_application()

