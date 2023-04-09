from abc import ABC

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


class Square(Shape):
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
        print(f"Длина стороны: {self.__width}")


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
              f"Высота прямоугольника: {self.__height}")

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
        super(Ellipse, self).info()
        print(f"Длина элипса: {self.__width}\n"
              f"Высота элипса: {self.__height}")



def execute_application():

    square = Square(0, 0, 5)
    square.info()
    print()

    rectangle = Rectangle(1, 1, 2, 8)
    rectangle.info()
    print()

    circle = Circle(2, 2, 4)
    circle.info()
    print()

    ellipse = Ellipse(3, 3, 3, 8)
    ellipse.info()
    print()




if __name__ == "__main__":
    execute_application()