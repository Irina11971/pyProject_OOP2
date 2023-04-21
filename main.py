from typing import Dict

# Объектно-ориентированное программирование
# Статические методы класса

# Создайте класс Device, который содержит информацию об устройстве.
# С помощью механизма наследования, реализуйте класс CoffeeMachine
# (содержит информацию о кофемашине), класс Blender (содержит информацию
# о блендере).

class Device:
    def __init__(self, passport_number: str, surname: str, name: str, gender: str, birthdate: Dict[str, str],
                 birthplace: str, date_of_issue: Dict[str, str], patronymic: str = None):
        self.__passport_number = passport_number
        self.__surname = surname
        self.__name = name
        self.__patronymic = patronymic
        self.__gender = gender
        self.__birthdate = birthdate.copy()
        self.__birthplace = birthplace
        self.__date_of_issue = date_of_issue.copy()



class International_passport(Passport):

    def __init__(self, passport_number: str, surname: str, name: str, gender: str, birthdate: Dict[str, str], \
                 birthplace: str, date_of_issue: Dict[str, str], code_of_issuing_State: str, \
                 date_of_expiry: Dict[str, str], patronymic: str = None):
        super().__init__(passport_number, surname, name, gender, birthdate, birthplace, date_of_issue, patronymic)
        self.__code_of_issuing_State = code_of_issuing_State
        self.__date_of_expiry = date_of_expiry.copy()



def execute_application():
    pass




if __name__ == "__main__":
    execute_application()