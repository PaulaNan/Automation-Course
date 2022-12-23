# # ex.1 abstract class GeometricShape, fied PI=3.14, 1 abstractmethod (area), a class method print
# from abc import ABC, abstractmethod
#
from abc import ABC, abstractmethod


class GeometricShape(ABC):
    PI = 3.14

    @abstractmethod
    def area(self, radius):
        self.radius = radius
        return self.area

    @classmethod
    def describe(self):
        print('I probably have shapes')


class Circle(GeometricShape):
    def area(self, radius):
        area = self.radius * self.radius * self.PI
        return area
        print(f'Circle area is {self.radius + self.radius * self.PI}')


class Square(GeometricShape):
    def area(self, square_side):
        area = square_side * 4
        return area


form = GeometricShape()
form.area(3)
form.describe()

forms = GeometricShape()
forms.describe()
forms.area(5)


# ex.2 inheritance - class Square, inherits the GeometricShape, def init - side
class GeometricShape:
    PI = 3.14

    def area(self):
        print('circle')

    def perimeter(self):
        print('square')


class Circle(GeometricShape):
    def __init__(self):
        self.radius = None

    def area(self, radius):
        self.radius = radius

        print(f'The circle area is {self.radius * self.radius * self.PI}')


class Square(GeometricShape):

    def __init__(self):
        self.square_area = None

    def area(self, square_side):
        self.square_area = square_side
        square_area = self.square_area * self.square_area
        self.square_area = square_area
        print(f'the square area is {self.square_area}')

    def perimeter(self):
        print(f'The square perimeter is {self.square_area * 4}')


class Rectangle(GeometricShape):
    def _init_(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def area(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        print(f'The rectangle area is {self.side1 * self.side2}')

    def perimeter(self, side1, side2):
        print(f'The rectangle perimeter is {self.side1 * 2 + self.side2 * 2}')


circle = Circle()
circle.area(5)

square = Square()
square.area(2)
square.perimeter()

rectangle = Rectangle()
rectangle.area(2, 4)
rectangle.perimeter(2, 4)


# ex.3 encapsulation. side is private property, implement get, set, del for side
class GeometricShape:
    __side = 3

    def get_side(self):
        return self.__side

    def set_side(self, new_side):
        self.__side = new_side
        return self.__side

    def delete_side(self):
        self.__side = None
        return self.__side


class Circle(GeometricShape):
    def _init_(self, radius):
        self.radius = radius

    @property
    def side(self):
        return self.__side

    @side.getter
    def side(self):
        print(f'The area or circle si {self.radius * self.radius * self.PI}')

    @side.setter
    def side(self, new_side):
        print(f'New side is set for {new_side}')

    @side.deleter
    def side(self):
        print(f'The side is now {self.__side}')
        return self.__side


circle = Circle()
circle.get_side()
circle.set_side(6)
circle.delete_side()


# ex.4 polymorphism - define a new method describe - print: I don't have shape (and circle) , create an object square
# and play with his methods
class Circle:
    def area(self):
        print('Circle')

    def describe(self):
        print('I have no shapes')


class Square:
    def area(self):
        print('Square')


obj_circle = Circle()
obj_square = Square()
for side in (obj_circle, obj_square):
    side.area()
