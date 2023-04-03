from typing import Dict

# Создайте класс Passport (паспорт), который будет содержать
# паспортную информацию о гражданине страны. С помощью механизма
# наследования, реализуйте класс ForeignPassport (загран.паспорт)
# производный от Passport.


class Passport:
    def __init__(self, passport_number: int, surname: str, name: str, patronymic: str = None, \
                 gender: str, birthdate: Dict[str, int], birthplace: Dict[str, str], date_of_issue: Dict[str, int]):
        self.__passport_number = passport_number
        self.__surname = surname
        self.__name = name
        self.__patronymic = patronymic
        self.__gender = gender
        self.__birthdate = birthdate
        self.__birthplace = birthplace
        self.__date_of_issue = date_of_issue


    def __str__(self):
        return f"Номер паспорта: {self.__passport_number} \n" \
               f"Фамилия: {self.__surname} \n" \
               f"Имя: {self.__name} \n" \
               f"Отчество: {self.__patronymic} \n" \
               f"Пол: {self.__gender} \n"\
               f"Дата рождения: {self.__birthdate} \n" \
               f"Место рождения: {self.__birthplace} \n" \
               f"Дата выдачи: {self.__date_of_issue} \n"






def execute_application():

if __name__ == "__main__":
        execute_application()