# 9.6 Объектно-ориентированное программирование
# Абстрактные классы

# Создайте базовый класс Shape для хранения плоских фигур.
# Определите производные классы:
# Square — квадрат, который характеризуется координатами левого
# верхнего угла и длиной стороны;
# Rectangle — прямоугольник с заданными координатами верхнего
# левого угла и размерами;
# Circle — окруж
# ность с заданными координатами цен-тра и радиусом;
# Ellipse — эллипс с заданными координатами верхнего угла описанного
# вокруг него прямоугольника со сторонами, параллельными осям координат,
# и размерами этого прямоугольника.
# Создайте список фигур. Определите класс, который сохраняет фигуры
# в файлы, загружает из файла и отобразите информацию о каждой из фигур.


class ShapeWriteline: #  класс для записи информации о фигурах в файл
    def writelines_in_file(self, path: str) -> None:
        """
        Добавляет запись о фигуре в файл
        :param path (str): путь к файлу
        :return:
        """

        with open(path, 'a', encoding='UTF-8') as file:
            file.writelines(self.__class__.__name__ + "\n")
            for val in self.__dict__.values():
                file.writelines(str(val) + '\n')
class ShapeRead: # класс для чтения информации о фигурах из файла

    def square_read_data_from_file(path: str):
        """
        Читает данные о квадрате из файла
        :param path(str): путь к файлу

        :return:
            tuple: кортеж с данными
        """

        with open(path, 'r', encoding='UTF-8') as file:
            record = file.readline().rstrip('\n').split(',')
            x = int(record[0])
            y = int(record[1])
            width = int(record[2])
            return x, y, width

    def rectangle_read_data_from_file(path: str):
        """
        Читает данные о прямоугольнике из файла
        :param path(str): путь к файлу

        :return:
            tuple: кортеж с данными
        """

        with open(path, 'r', encoding='UTF-8') as file:
            record = file.readline().rstrip('\n').split(',')
            x = int(record[0])
            y = int(record[1])
            width = int(record[2])
            height = int(record[3])
            return x, y, width, height


    def circle_read_data_from_file(path: str):
        """
        Читает данные о круге из файла
        :param path(str): путь к файлу

        :return:
            tuple: кортеж с данными
        """

        with open(path, 'r', encoding='UTF-8') as file:
            record = file.readline().rstrip('\n').split(',')
            x = int(record[0])
            y = int(record[1])
            radius = int(record[2])
            return x, y, radius


    def ellipse_read_data_from_file(path: str):
        """
        Читает данные об элипсе из файла
        :param path(str): путь к файлу

        :return:
            tuple: кортеж с данными о фигуре
        """

        with open(path, 'r', encoding='UTF-8') as file:
            record = file.readline().rstrip('\n').split(',')
            x = int(record[0])
            y = int(record[1])
            width = int(record[2])
            height = int(record[3])
            return x, y, width, height


class Shape:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        self.__y = y

    def info(self):
        print(f"Класс: {self.__class__.__name__} \n"
              f"Координата Х: {self.__x} \n"
              f"Координата Y: {self.__y}")


class Square(Shape, ShapeRead, ShapeWriteline):
    def __init__(self, x: int, y: int, width: int):
        super().__init__(x, y)
        self.__width = width

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        self.__width = width

    def info(self):
        super().info()
        print(f"Длина стороны: {self.__width}\n")

class Rectangle(Shape, ShapeRead, ShapeWriteline):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        self.__height = height

    def info(self):
        super().info()
        print(f"Длина прямоугольника: {self.__width}\n"
              f"Высота прямоугольника: {self.__height}\n")


class Circle(Shape, ShapeRead, ShapeWriteline):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y)
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    def info(self):
        super().info()
        print(f"Радиус круга: {self.__radius}\n")

class Ellipse(Shape, ShapeRead, ShapeWriteline):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        self.__height = height

    def info(self):
        super().info()
        print(f"Длина элипса: {self.__width}\n"
              f"Высота элипса: {self.__height}")


def execute_application():

    path = 'file_to_write.txt'                                # путь к файлу для записи информации о фигурах

    data = Square.square_read_data_from_file("data_Square.txt")
    square = Square(*data)
    square.writelines_in_file(path)

    data = Rectangle.rectangle_read_data_from_file("data_Rectangle.txt")
    rectangle = Rectangle(*data)
    rectangle.writelines_in_file(path)


    data = Circle.circle_read_data_from_file("data_Circle.txt")
    circle = Circle(*data)
    circle.writelines_in_file(path)

    data = Ellipse.ellipse_read_data_from_file("data_Ellipse.txt")
    ellipse = Ellipse(*data)
    ellipse.writelines_in_file(path)

    # Выводим информацию о фигурах на консоль
    ListFigures = []
    ListFigures.append(square)
    ListFigures.append(rectangle)
    ListFigures.append(circle)
    ListFigures.append(ellipse)
    for figures in ListFigures:
        figures.info()



if __name__ == "__main__":
    execute_application()