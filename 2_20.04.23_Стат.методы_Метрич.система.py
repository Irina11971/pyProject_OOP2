# Создайте класс для перевода из метрической системы в английскую и
# наоборот. Функциональность необходимо реализовать в виде статических
# методов.


class ConverterLengthMeasure:
    def __init__(self, inch: float = None, foot: float = None, yard: float = None, mile: float = None, \
                 millimeter: float = None, centimetre: float = None, metre: float = None, kilometer: float = None):
        self.inch = inch
        self.foot = foot
        self.yard = yard
        self.mile = mile
        self.millimeter = millimeter
        self.centimetre = centimetre
        self.metre = metre
        self.kilometer = kilometer

    def __str__(self):
        return f"Дюйм: {self.inch} \n" \
               f"Фут: {self.foot} \n" \
               f"Ярд: {self.yard} \n" \
               f"Миля: {self.mile} \n" \
               f"Милиметр: {self.millimeter} \n" \
               f"Сантиметр: {self.centimetre} \n" \
               f"Метр: {self.metre} \n" \
               f"Километр: {self.kilometer} \n"


    @staticmethod
    def get_inch_in_metricSystem(inch: float) -> float:
        """
        Переводит дюймы в милиметры

        :param inch (float): количесвто дюймов
        :return:
            float: милиметры
        """
        return 25.4 * inch

    @staticmethod
    def get_foot_in_metricSystem(foot: float) -> float:
        """
        Переводит футы в метры

        :param foot (float): количесвто футов
        :return:
            float: метры
        """
        return 0.3048 * foot

    @staticmethod
    def get_yard_in_metricSystem(yard: float) -> float:
        """
        Переводит ярды в метры

        :param yard (float): количесвто ярдов
        :return:
            float: метры
        """
        return 0.9144 * yard

    @staticmethod
    def get_mile_in_metricSystem(mile: float) -> float:
        """
        Переводит мили в километры

        :param mile (float): количесвто миль
        :return:
            float: километры
        """
        return 1.609 * mile

    @staticmethod
    def get_millimeter_in_englishSystem(millimeter: float) -> float:
        """
        Переводит милиметры в дюймы

        :param millimeter (float): количесвто милиметров
        :return:
            float: дюймы
        """
        return millimeter / 25.4

    @staticmethod
    def get_centimetre_in_englishSystem(centimetre: float) -> float:
        """
        Переводит сантиметры в дюймы

        :param centimetre(float): количесвто сантиметров
        :return:
            float: дюймы
        """
        return centimetre / 2.54

    @staticmethod
    def get_metre_in_englishSystem(metre: float) -> float:
        """
        Переводит метры в ярды

        :param metre(float): количесвто метров
        :return:
            float: ярды
        """
        return metre / 0.9144

    @staticmethod
    def get_kilometer_in_englishSystem(kilometer: float) -> float:
        """
        Переводит километры в мили

        :param kilometer(float): количесвто киолометров
        :return:
            float: мили
        """
        return kilometer / 1.609


def execute_application():
    print("1 - перевод дюймов в метрическую систему \n"
          "2 - перевод футов в метрическую систему \n"
          "3 - перевод ярдов в метрическую систему \n"
          "4 - перевод миль в метрическую систему \n"
          "5 - перевод милиметров в английскую систему \n"
          "6 - перевод сантиметров в английскую систему \n"
          "7 - перевод метров в английскую систему \n"
          "8 - перевод километров в английскую систему \n"
          "9 - выход из конвертора \n")

    while (True):
        try:
            N = int(input("Введите вариант действия (цифры 1-9): "))
            if N == 1:
                inch = float(input("Введите количество дюймов: "))
                millimeter = ConverterLengthMeasure.get_inch_in_metricSystem(inch)
                print(f"{inch} дюйм(а/ов) это {millimeter: 0.2f} милиметра.")
                continue
            elif N == 2:
                foot = float(input("Введите количество футов: "))
                meter = ConverterLengthMeasure.get_foot_in_metricSystem(foot)
                print(f"{foot} фут(а/ов) это {meter: 0.2f} метра.")
                continue
            elif N == 3:
                yard = float(input("Введите количество ярдов: "))
                meter = ConverterLengthMeasure.get_yard_in_metricSystem(yard)
                print(f"{yard} ярд(а/ов) это {meter: 0.2f} метра.")
                continue
            elif N == 4:
                mile = float(input("Введите количество миль: "))
                kilometer = ConverterLengthMeasure.get_mile_in_metricSystem(mile)
                print(f"{mile} миля(ей/и) это {kilometer: 0.2f} километра.")
                continue
            elif N == 5:
                millimeter = float(input("Введите количество милиметров: "))
                inch = ConverterLengthMeasure.get_millimeter_in_englishSystem(millimeter)
                print(f"{millimeter} милиметр(а/ов) это {inch: 0.2f} дюйма.")
                continue
            elif N == 6:
                centimetre = float(input("Введите количество сантиметров: "))
                inch = ConverterLengthMeasure.get_centimetre_in_englishSystem(centimetre)
                print(f"{centimetre} сантиметр(а/ов) это {inch: 0.2f} дюйма.")
                continue
            elif N == 7:
                metre = float(input("Введите количество метров: "))
                foot = ConverterLengthMeasure.get_metre_in_englishSystem(metre)
                print(f"{metre} метр(а/ов) это {foot: 0.2f} ярда.")
                continue
            elif N == 8:
                kilometer = float(input("Введите количество километров: "))
                mile = ConverterLengthMeasure.get_kilometer_in_englishSystem(kilometer)
                print(f"{kilometer} километр(а/ов) это {mile: 0.2f} мили.")
                continue
            elif N == 9:
                print("Вы вышли из конвертора единиц длины.")
                break
            else:
                print(f"Некорректно введен вариант действий. Введите цифру от 1 до 9. \n")
                continue

        except ValueError as e:
            print("Невозможно привести к числовому значению. Введите данные повторно.")


if __name__ == "__main__":
    execute_application()