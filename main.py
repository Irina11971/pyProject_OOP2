from abc import ABC, abstractmethod

# 9.6 Объектно-ориентированное программирование
# Абстрактные классы

# Создайте базовый класс Shape для хранения плоских фигур.
# Определите производные классы:
# Square — квадрат, который характеризуется координатами левого
# верхнего угла и длиной стороны;
# Rectangle — прямоугольник с заданными координатами верхнего
# левого угла и размерами;
# Circle — окружность с заданными координатами цен-тра и радиусом;
# Ellipse — эллипс с заданными координатами верхнего угла описанного
# вокруг него прямоугольника со сторонами, параллельными осям координат,
# и размерами этого прямоугольника.
# Создайте список фигур. Определите класс, который сохраняет фигуры
# в файлы, загружает из файла и отобразите информацию о каждой из фигур.


class ShapeWriteline(ABC): # абстрактный класс для записи информации о формах в файл
    @abstractmethod
    def writeline_in_file(self):
        pass
class ShapeRead(ABC): # абстрактный класс для чтения информации о формах из файла
    @abstractmethod
    def read_data_from_file(self):
        pass

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


class Square(Shape, ShapeWriteline, ShapeRead):
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



class Rectangle(Shape):
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

class Circle(Shape):
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

class Ellipse(Shape):
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

    ListFigures = []

    square = Square(0, 0, 5)
    ListFigures.append(square)

    rectangle = Rectangle(1, 1, 2, 8)
    ListFigures.append(rectangle)

    circle = Circle(2, 2, 4)
    ListFigures.append(circle)

    ellipse = Ellipse(3, 3, 3, 8)
    ListFigures.append(ellipse)

    for figures in ListFigures:
        figures.info()
        print()




if __name__ == "__main__":
    execute_application()