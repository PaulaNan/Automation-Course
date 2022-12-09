# ex.1 class circle, radius and color are atributes, methods: description, area, diameter, circumference
class Circle:
    radius = 10
    color = 'blue'

    def _init_(self, radius, color):
        self.radius = radius
        self.color = color

    def description(self):
        print(f'the color is {self.color}, and the radius is {self.radius}')

    def circle_area(self):
        area = self.radius * self.radius * 3.14
        return area

    def diameter(self):
        circle_diameter = 2 * self.radius
        print(f'diameter is {circle_diameter}')

    def circumference(self):
        circum = 2 * 3.14 * self.radius
        print(f'the circumference is {circum}')


cercle_info = Circle(10, 'blue')
cercle_info.description()
print(cercle_info.circle_area())
cercle_info.diameter()
cercle_info.circumference()


# ex.2 class right angle, atributes: lenght, width, color, methods: description, area, petrimeter, change color
class RightAngle():
    lenght = 10
    width = 5
    color = 'red'

    def _init_(self, lenght, width, color):
        self.lenght = lenght
        self.width = width
        self.color = color

    def description(self):
        print(f'the lenght is {self.lenght}, the color is {self.color}, and the widht is {self.width}')

    def angle_area(self):
        area = self.width * self.lenght
        print(f'area is {area}')

    def perimeter(self):
        angle_perimeter = self.width * 2 + self.lenght * 2
        print(f'the perimeter is {angle_perimeter}')

    def change_color(self):
        new_color = 'green'
        self.color = new_color


angle = RightAngle(10, 5, 'red')
angle.description()
angle.angle_area()
angle.perimeter()
angle.change_color()
angle.description()


# ex.3 class employee, atributes:name, surname, salary, methods: description, full name, monthly salary, anual salary, raise salary %
class Employee:
    def _init_(self, name, last_name, salary):
        self.name = name
        self.last_name = last_name
        self.salary = salary

    def describe(self):
        print(f'my name is {self.name} {self.full_name} and my salary is {self.salary}')

    def full_name(self):
        full_name = f'full name is {self.name} {self.last_name}'
        return full_name

    def salary(self):
        print(f'monthly salary is {self.salary}')

    def anual_salary(self):
        print(f'anual salary is {self.salary * 12}')

    def raise_salary(self, percent):
        self.percent = percent
        print(f'your annual salary is {self.percent / 100 * self.salary} + {self.salary}')


employee1 = Employee('Popescu', 'Maria', 1500)
employee1.describe()
employee1.full_name()
employee1.salary()
employee1.anual_salary()
employee1.raise_salary(10)
#
#
# class Employee():
#     name = None
#     surname = None
#     salary = None
#
#     def _init_(self, name, surname, salary):
#         self.name = name
#         self.surname = surname
#         self.salary = salary
#
#     def description(self):
#         print(f'the name is {self.name}, surname {self.surname}, and salary is {self.salary}')
#
#     def full_name(self):
#         print(f'full name is {self.name} {self.surname}')
#
#     def monthly_salary(self):
#         print(f'salary is {self.salary}')
#
#     def anual_salary(self):
#         year_salary = self.salary * 12
#         print(f'anual salary is {year_salary}')
#
#     def raise_salary(self):
#         percent = self.salary * 10 / 100
#         new_salary = self.salary + percent
#         print(f'the raise is {percent}')
#         print(f'new salary is {new_salary}')
#
#
# empl = Employee('Popescu', 'Marcel', 1500)
# empl.description()
# empl.full_name()
# empl.monthly_salary()
# empl.anual_salary()
# empl.raise_salary()


# ex.4 class account, atribute:iban, owner, balance, methods show balance, debit account, credit account
class Account():
    iban = None
    owner = None
    balance = 0
    credit = None
    debit = None

    def _init_(self, iban, owner, balance):
        self.iban = iban
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f'owner {self.owner} has in account {self.iban} the amount of {self.balance}')

    def credit_account(self):
        credit = int(input('how much money do you want to credit your account '))
        new_balance = self.balance + credit
        print(f'you credit your account with {credit}, and the balance is {new_balance}')


#   def debit_account(self):
#     debit = int(input('how much do you want to withdrawal? '))
#     if debit < self.balance:
#       print(f'insuficinet founds, you have {self.balance} ')
#     else:
#       self.balance = new_balance - debit
#     print(f'you withdrawal {debit}, you now have {self.balance}')

# bank = Account('ro12345', 'Popescu Ion', 0)
# bank.show_balance()
# bank.credit_account()
# bank.debit_account()

# ex.1 class Bill, atributes: SERIES, number, name product, quantity, price/buc, methods: change quantity, change price, change name product, generate bill
from datetime import date

today = date.today()


class Bill():
    SERIES = 'ABC'
    number = 1
    product_name = None
    quantity = None
    price = None

    def _init_(self, number, product_name, quantity, price):
        self.number = number
        self.product_name = product_name
        self.quantity = quantity
        self.price = price

    def change_quantity(self):
        print(f' quantity is {self.quantity}')

    # def change_price(self):

    # def change_name(self):

    # def generate_bill(bill):


bill_generator = Bill(1, ' ball', 2, 55 )
bill_generator.change_quantity()
print(f'date: ', today)


# ex.2 class car, atributes: brand, model, max_speed, current_speed, color, available_colors, enrolled, constructor: model, max_speed, methods: description, enrolled, paint, accelerate, brake
class Car():
    color = 'grey'
    current_speed = 0
    available_colors = {'red', 'blue', 'white', 'orange', 'green', 'black'}
    brand = 'Audi'
    enrolled = False

    def _init_(self, model, max_speed):
        self.model = model
        self.max_speed = max_speed

    def description(self):
        print(f' information about your car: brand {self.brand}, model {self.model}, color {self.color}, enrolled {self.enrolled}')

    def enrolled_car(self):
        self.enrolled = True

    def paint(self, color):
        if color in self.available_colors:
            print(f'your car is now {color}')
            self.color = color
        else:
            print('choose a color')

    def accelerate(self, current_speed):
        if current_speed < 0:
            print('eror')
        elif current_speed < 220:
            print(f'accelerate with {current_speed}')
        else:
            print(f'car will accelerate until {self.max_speed}')

    def brake(self):
        self.current_speed == 0
        print('car is braking, your speed is 0')


new_car = Car('a6', 220)
new_car.description()
new_car.enrolled_car()
new_car.paint('blue')
new_car.accelerate(130)
new_car.description()
new_car.brake()

