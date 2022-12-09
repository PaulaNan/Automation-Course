# # exceptions
# try: # put the code that might generate exception
#   number = 0
#   print(number)
#   number2 = 10/number
# except Exception as e: # Exception = any exception (e= keeps the message)
#   print(f'Error: {e}')
# print('code is passing')

# try:
#   list = [1, 2, 3]
#   list[6]
# except IndexError as e:
#   print(f'Error: {e}')

# # force an exception (if....raise)
# raise IndexError('the limit of students in classroom is 30')

# inheritance
class Chef:  # parent class
    knife = 1

    def make_salad(self):
        print('salad')

    def make_fries(self):
        print('fries')


class Chef2:
    short = 2


class JapaneseChef(Chef):  # child class
    def make_sushi(self):
        print('sushi')


class ItalianChef(Chef, Chef2):
    plate = 1

    def make_pizza(self):
        print('pizza')


nakamoto = JapaneseChef()  # initialize objects type japanese chef
newbe = Chef()
newbe.make_fries
nakamoto.make_salad
nakamoto.make_fries
nakamoto.make_sushi
mario = ItalianChef()
mario.make_fries
mario.make_pizza
mario.make_salad
mario.knife
mario.plate
mario.short


# polymorphism - 2 function with the same name, but different behavior depending on input
# polymorphism este situatia cand exista mai multe functii cu aceleasi nume si in functie de input va sti care sa se apeleze
# polymorphism with class method
class Romania:
    def language(self):
        print('romanian')


class USA:
    def language(self):
        print('english')


obj_ro = Romania()
obj_usa = USA()
for country in (obj_ro, obj_usa):
    country.language()


# polymorphism with inheritance
class Bird:
    def description(self):
        print('i am a bird')

    def fly(self):
        print('i am flying')


class Parrot(Bird):
    def talk(self):
        print('i also talk')


class Penguin(Bird):
    def fly(self):  # in poly when are 2 function with same name it is uses the right one
        print('i actually can not fly, but it is ok, i am dressed stylish')


random_bird = Bird()
random_bird.description()
random_bird.fly
print('------------')

polly = Parrot()
polly.description()
polly.talk()
polly.fly()
print('---------------')

pingu = Penguin()
pingu.description()
pingu.fly()
# metoda abstracta = definita la niv clasei abstracte care nu are logica/ corp care trebuie implementata de toti copiii care mostenesc clasa abstracta
# abstraction - contains methods without body but also with specific logic
# interfata e o clasa care contine metode abstracte care pot fi mostenite ulterior
# interfata(contine numai metode abstracte) dog implements animal (dog class implementeaza interfata animal)
# nimimul pe care trebuie sa il stii
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        raise NotImplementedError

    @abstractmethod
    def sleep(self):
        raise NotImplementedError


class Dog(Animal):
    def sound(self):
        print('ham ham')

    def sleep(self):
        print('zzzzzzzzzz')


class Cat(Animal):
    def sound(self):
        print('miau, miau')

    def sleep(self):
        print('rrrrrrr')

    def describe(self):  # new method in abstractmethod
        print('i am human')


azorel = Dog()
tom = Cat()
azorel.sleep()
azorel.sound()

tom.sound()
tom.sleep()
tom.describe()


class Car(ABC):

    @abstractmethod  # decorator
    def accelerate(self):  # abstract method
        pass
        # or raise NotImplementedError (force an exception)

    # interfata are toate metodele abstracte clasa abstracta are si metode abstracte si metode clasice
    @classmethod  # metoda ce tine de clasa asta metoda clasica
    def stop(self):
        print('STOP')


class Ferrari(Car):
    def accelerate(self):
        print('i am accelerating from 0 to 100 in 3 sec')

    def stop(self):  # overwrite
        print('i am a ferrari, i can not stop')


class Lastun(Car):
    def accelerate(self):
        print('i amm accelerating from 0 to 100 in 15 sec')


f = Ferrari()
f.accelerate()
f.stop()

l = Lastun()
l.accelerate()
l.stop()


# interfata are toate metodele abstracte obliga toate clasele mostenitoare sa foloseasca metodele

# encapsulation - attributes will be hidden by __ : get, set, delete, hide
class Car:
    __color = 'grey'

    # we can hide methods

    def get_color(self):  # to get the color
        return self.__color

    def set_color(self, wished_color):  # to set new color
        self.__color = wished_color

    def delete_color(self):
        self.__color = None

    def __hidden(self):
        pass


volvo = Car()
print(volvo.get_color())
volvo.set_color('red')
print(volvo.get_color())
volvo.delete_color()
print(volvo.get_color())


# property - label - obliga sa se conporte ca o propietate
# tema


# property - label - obliga sa se conporte ca o propietate. daca atributul e color, metodele sunt tot color. pe getter trebuie return
class CarPy:
    def _init_(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.getter
    def color(self):
        print
        {f'getter: color is {self.__color}'}
        return self.__color

    @color.setter
    def color(self, color):
        if color == 'black':
            print(f'setter: new color is {color}')
            self.__color = color

    @color.deleter
    def color(self):
        print(f'deleter: i delete the color')
        self.__color = None


car2 = CarPy('grey')
car2.color = 'red'  # set color
car2.color  # get color
del car2.color  # del color
car2.color  # get color
print('-------------------')
car3 = CarPy('white')
car3.color  # getter
car3.color = 'black'  # set color
car3.color
del car3.color
car3.color
# propietatea e ca decorator/field si avem acces la decoratorii de getter, setter, deleter care trebuie implementate
# metode care fac exact asta: get, set, delete
