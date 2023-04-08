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
    pass




if __name__ == "__main__":
    execute_application()