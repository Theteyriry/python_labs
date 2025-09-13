#добавляем модуль для работы с абстрактными классами (декоратор и базовый класс)
from abc import ABC, abstractmethod

#добавляем модуль для математических операций
import math

#создаем родительский класс
class Shape(ABC):
    #добавляем абстрактные (обязательные для реализации при наследовании) методы
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetr(self):
        pass

#создаем дочерний класс прямоугольников
class Rectangle(Shape):
    #добавляем атрибуты длина, высота
    def __init__(self, length, width):
        self.length = length
        self.width = width
    #реализуем обязательные функции
    def area(self):
        return self.width*self.length
    def perimetr(self):
        return (self.length + self.width)*2
    
class Circle(Shape):
    def __init__(self, radius):
            self.radius = radius
    def area(self):
            #для вычислений используем pi из модуля math
            return math.pi*self.radius*self.radius
    def perimetr(self):
            return 2*math.pi*self.radius
    
class Triangle(Shape):
    def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c
    def area(self):
            p = self.perimetr()/2
            return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    def perimetr(self):
            return self.a + self.b + self.c
    
#создаем функцию вывода информации о фигурах
def print_shape_info(shape):
    #округляем до двух знаков после запятой
    print(f"Площадь: {shape.area():.2f}")
    #добавляем \n перенос на новую строку для визуального отделения информации о фигурах
    print(f"Периметр: {shape.perimetr():.2f}\n")

#защищаем проверочный код от импортирования
if __name__ == '__main__':

    #создаем экземпляры разных классов
    rectangle = Rectangle(10, 1)
    circle = Circle(4)
    triangle = Triangle(3, 5, 7)

    #выводим сообщение о типе фигуры и используем функцию вывода
    print("Rectangle Info:")
    print_shape_info(rectangle)

    print("Circle Info:")
    print_shape_info(circle)

    print("Triangle Info:")
    print_shape_info(triangle)



        
