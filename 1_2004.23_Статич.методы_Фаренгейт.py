# Задание 1.
# Создайте класс для конвертирования температуры из Цельсия в
# Фаренгейт и наоборот. У класса должно быть два статических метода: для
# перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий.

class ConversionTemperature:
    def __init__(self, temperature_Celsius: float = None, temperature_Fahrenheit: float = None):
        self.temperature_Celsius = temperature_Celsius
        self.temperature_Fahrenheit = temperature_Fahrenheit

    def __str__(self):
        return f"Температура по Цельсию: {self.temperature_Celsius} \n" \
               f"Температура по Фаренгейту: {self.temperature_Fahrenheit} \n"



    @staticmethod
    def get_temperature_Celsius_in_temperature_Fahrenheit(temperature_Celsius: float):
        """
        Переводит температуру из градосов Цельсия в градусы по Фаренгейту

        :param temperature_Celsius (float): температура в градусах Цельсия
        :return:
            float: температура в градусах по Фаренгейту
        """
        return 1.8 * temperature_Celsius + 32

    @staticmethod
    def get_temperature_Fahrenheit_in_temperature_Celsius(temperature_Fahrenheit: float):
        """
        Переводит температуру из градусов по Фаренгейту в градусы Цельсия

        :param temperature_Fahrenheit (float): температура в градусах по Фаренгейту
        :return:
            float: температура в градусах Цельсия
        """

        return (temperature_Fahrenheit-32) / 1.8

