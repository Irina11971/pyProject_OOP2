from typing import Dict

# Создайте класс Passport (паспорт), который будет содержать
# паспортную информацию о гражданине страны. С помощью механизма
# наследования, реализуйте класс ForeignPassport (загран.паспорт)
# производный от Passport.


class Passport:
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


    @property
    def passport_number(self):
        return self.__passport_number
    @passport_number.setter
    def passport_number(self,passport_number: str):
        self.__passport_number = passport_number

    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def patronymic(self):
        return self.__patronymic
    @patronymic.setter
    def patronymic(self, patronymic: str):
        self.__patronymic = patronymic

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def birthdate(self):
        return list(self.__birthdate.values())
    @birthdate.setter
    def birthdate(self, birthdate: Dict[str, str]):
        self.__birthdate = birthdate

    @property
    def birthplace(self):
        return self.__birthplace
    @birthplace.setter
    def birthplace(self, birthplace: str):
        self.__birthplace = birthplace

    @property
    def date_of_issue(self):
        return list(self.__date_of_issue.values())
    @date_of_issue.setter
    def date_of_issue(self, date_of_issue: Dict[str, int]):
        self.__date_of_issue = date_of_issue

    def info(self):
        print(f"Класс: {self.__class__.__name__} \n"
              f"Номер паспорта: {self.__passport_number} \n"
              f"Фамилия: {self.__surname} \n"
              f"Имя: {self.__name} \n"
              f"Отчество: {self.__patronymic} \n"
              f"Пол: {self.__gender} \n"
              f"Дата рождения: {list(self.__birthdate.values())} \n"
              f"Место рождения: {self.__birthplace} \n"
              f"Дата выдачи: {list(self.__date_of_issue.values())}")

class ForeignPassport(Passport):

    def __init__(self, passport_number: str, surname: str, name: str, gender: str, birthdate: Dict[str, str], \
                 birthplace: str, date_of_issue: Dict[str, str], code_of_issuing_State: str, \
                 date_of_expiry: Dict[str, str], patronymic: str = None):
        super().__init__(passport_number, surname, name, gender, birthdate, birthplace, date_of_issue, patronymic)
        self.__code_of_issuing_State = code_of_issuing_State
        self.__date_of_expiry = date_of_expiry.copy()

    @property
    def code_of_issuing_State(self):
        return self.__code_of_issuing_State
    @code_of_issuing_State.setter
    def code_of_issuing_State(self, code_of_issuing_State: str):
        self.__code_of_issuing_State = code_of_issuing_State

    @property
    def date_of_expiry(self):
        return list(self.__date_of_expiry.values())
    @date_of_expiry.setter
    def date_of_expiry(self, date_of_expiry: Dict[str, str]):
        self.__date_of_expiry = date_of_expiry

    def info(self):
        super().info()
        print(f"Код государства выдачи: {self.__code_of_issuing_State} \n" \
              f"Дата окончания срока действия: {list(self.__date_of_expiry.values())} \n")

def execute_application():

    passport = Passport("7800 628314", "Иванов", "Сергей", "муж", {"число": 23, "месяц": '11', "год": 1989},\
                        "Г.ЯРОСЛАВЛЬ, ЯРОСЛАВСКАЯ ОБЛАСТЬ", {"число": 14, "месяц": "12", "год": 2003}, "Степанович")
    passport.info()
    print()


    international_passport = ForeignPassport("75 0185892", "Иванов", "Сергей", "муж", \
                                                    {"число": 23, "месяц": '11', "год": 1989}, \
                                                    "Г.ЯРОСЛАВЛЬ, ЯРОСЛАВСКАЯ ОБЛАСТЬ", \
                                                    {"число": '08', "месяц": '05', "год": 2015}, "RUS", \
                                                    {"число": '07', "месяц": '05', "год": 2025}, "Степанович")
    international_passport.info()
    print()


if __name__ == "__main__":
    execute_application()

