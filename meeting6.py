class Car:
    # fields/ attribute
    make = 'Dacia'
    model = None
    year = 2022
    color = None

    # constructor
    def __init__(self, model, color):
        self.color = color
        self.model = model

    # methods
    def accelerate(self):
        print('Vrum, vrum')

    def paint(self, color):
        self.color = color


car1 = Car('Logan', 'red')
car2 = Car('Duster', 'orange')
print(car1.color)
print(car2.color)
car1.accelerate()
car2.paint('blue')
print(car2.color)


# nerfgun exercise
class Nerfgun:
    # attribute/ fields
    model = None
    bullets = 0
    safety_on = True
    color = None
    possible_colors = {'red', 'orange', 'black'}

    # constructor
    def __init__(self, model, color):
        self.model = model
        if color in self.possible_colors:
            self.color = color
        else:
            print(f'when call the method of object {model}, the color is invalid')

    # methods
    def description(self):
        print(f'the model is {self.model}')
        print(f'the color is {self.color}')
        print(f'no of bullets are {self.bullets}')
        print(f'safety on is {self.safety_on}')

    def remove_safety(self):
        self.safety_on = False
        print('you remove safety')

    def shoot(self):
        if self.safety_on == False and self.bullets > 0:
            self.bullets -= 1
            print('boom, boom')
        else:
            print('you can not shoot, verify safety and bullets')

    def load(self, bullets):
        if bullets >= 10:
            self.bullets = 10
        elif bullets <= 0:
            print('invalid no of bullets')
        else:
            self.bullets = bullets

    def safety_off(self):
        self.safety_on = True
        print('the safety is on')


# objects/ call the methods
nerf1 = Nerfgun('glock', 'red')
nerf2 = Nerfgun('glock3', 'pink')
nerf1.description()
nerf2.description()
nerf2.color = 'blue'
nerf2.description()
nerf1.remove_safety()
nerf1.description()
nerf1.load(5)
nerf1.shoot()
nerf1.shoot()
nerf1.safety_off()
nerf1.description()
nerf2.remove_safety()
nerf2.load(2)
nerf2.shoot()
nerf2.shoot()
nerf2.description()

import random


class Dog:
    def __init__(self, name, breed, color):  # all are none
        self.name = name
        self.breed = breed
        self.color = color
        self.age = 1

    def description(self):
        print(f'name {self.name}')
        print(f'color {self.color}')
        print(f'breed {self.breed}')
        print(f'dog age {self.dog_age()}')

    def dog_age(self):
        return self.age * 7

    def happy_birthday(self):
        self.age += 1

    def bark(self):
        n = random.randint(1, 3)
        print(self.name + ':')
        print('ham ' * n)


grivei = Dog('Grivei', 'golden', 'black')
azorel = Dog('Azorel', 'x', 'brown')
grivei.description()
azorel.description()
azorel.name = 'Zdreanta'
azorel.happy_birthday()
zdreanta = azorel
zdreanta.happy_birthday()
zdreanta.bark()
zdreanta.bark()
zdreanta.description()
azorel.happy_birthday()
azorel.description()
