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
    def temperature_Celsius_in_temperature_Fahrenheit(temperature_Celsius: float):
        """
        Переводит температуру из градосов Цельсия в градусы по Фаренгейту

        :param temperature_Celsius (float): температура в градусах Цельсия
        :return:
            float: температура в градусах по Фаренгейту
        """
        return 1.8 * temperature_Celsius + 32

    @staticmethod
    def temperature_Fahrenheit_in_temperature_Celsius(temperature_Fahrenheit: float):
        """
        Переводит температуру из градусов по Фаренгейту в градусы Цельсия

        :param temperature_Fahrenheit (float): температура в градусах по Фаренгейту
        :return:
            float: температура в градусах Цельсия
        """

        return (temperature_Fahrenheit-32) / 1.8


def execute_application():

    print("Если нужно конвертироть температуру из Цельсия в Фаренгейт нажмите 1 \n"
          "Если нужно конвертироть температуру из градусов по Фаренгейту в градусы Цельсия нажмите 2 \n"
          "Для выхода из конвектора нажмите 3 \n")
    while(True):
        try:
            N = int(input("Введите вариант действия (цифры 1-3): "))
            if N == 1:
                temperature_Celsius = float(input("Введите температуру в градусах Цельсия: "))
                temperature_Fahrenheit = ConversionTemperature.temperature_Celsius_in_temperature_Fahrenheit(temperature_Celsius)
                print(f"{temperature_Celsius} градус(а/ов) по Цельсию это {temperature_Fahrenheit: 0.2f} градусов по Фаренгейту.")
                continue
            elif N == 2:
                temperature_Fahrenheit = float(input("Введите температуру в градусах по Фаренгейту: "))
                temperature_Celsius = ConversionTemperature.temperature_Fahrenheit_in_temperature_Celsius((temperature_Fahrenheit))
                print(f"{temperature_Fahrenheit} градус(а/ов) по Фаренгейту это {temperature_Celsius: 0.2f} градусов Цельсия.")
                continue
            elif N == 3:
                print("Вы вышли из конвертора температур.")
                break
            else:
                print(f"Некорректно введен вариант действий. Введите цифру от 1 до 3. \n")
                continue

        except ValueError as e:
            print("Невозможно привести к целому значению. Введите данные повторно.")



if __name__ == "__main__":
    execute_application()