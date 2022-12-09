# ex.1 class circle, radius and color are attributes, methods: description, area, diameter, circumference
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


circle_info = Circle()
circle_info.description()
print(circle_info.circle_area())
circle_info.diameter()
circle_info.circumference()


# ex.2 class right angle, attributes: length, width, color, methods: description, area, perimeter, change color
class RightAngle:
    length = 10
    width = 5
    color = 'red'

    def _init_(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

    def description(self):
        print(f'the length is {self.length}, the color is {self.color}, and the width is {self.width}')

    def angle_area(self):
        area = self.width * self.length
        print(f'area is {area}')

    def perimeter(self):
        angle_perimeter = self.width * 2 + self.length * 2
        print(f'the perimeter is {angle_perimeter}')

    def change_color(self):
        new_color = 'green'
        self.color = new_color


angle = RightAngle()
angle.description()
angle.angle_area()
angle.perimeter()
angle.change_color()
angle.description()


# ex.3 class employee, attributes: name, last name, salary, methods: description, full name, monthly salary,
# annual salary, raise salary %
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

    def annual_salary(self):
        print(f'annual salary is {self.salary * 12}')

    def raise_salary(self, percent):
        self.percent = percent
        print(f'your annual salary is {self.percent / 100 * self.salary} + {self.salary}')


employee1 = Employee('Popescu', 'Maria', 1500)
employee1.describe()
employee1.full_name()
employee1.salary()
employee1.annual_salary()
employee1.raise_salary(10)


# ex.4 class account, attribute:iban, owner, balance, methods show balance, debit account, credit account
class Account:
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
#       print(f'Insufficient founds, you have {self.balance} ')
#     else:
#       self.balance = new_balance - debit
#     print(f'You withdrawal {debit}, you now have {self.balance}')

# bank = Account('ro12345', 'Popescu Ion', 0)
# bank.show_balance()
# bank.credit_account()
# bank.debit_account()

# ex.1 class Bill, attributes: SERIES, number, name product, quantity, price/buc, methods: change quantity,
# change price, change name product, generate bill

from datetime import date

today = date.today()


class Bill:
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
        print(f'Quantity is {self.quantity}')

    # def change_price(self):

    # def change_name(self):

    # def generate_bill(bill):


bill_generator = Bill(1, ' ball', 2, 55)
bill_generator.change_quantity()
print(f'date: ', today)


# ex.2 class car, attributes: brand, model, max_speed, current_speed, color, available_colors, enrolled, constructor:
# model, max_speed, methods: description, enrolled, paint, accelerate, brake
class Car:
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


# ex.3 class todolist, atributes: todo (dict, key=name of task, value=description), methods add task(name, descrition), end task(name), show to do list(keys), show info(name task)
# class ToDoList():
#     todo = {}
#
#     def add_task(self, name, description):
#         print(f'you added a new task: {name}, {description}')
#
#     def end_task(self, name):
#
#         print(f'you remove {name} from list')
#
#     def show_todo_list(self):
#         print('keys')
#
#     def information(self, name):
#         if name != todo:
#             input('do you want to safe in to do list? ')
#             if True:
#
#     else:
#         name == todo:
#         input(f'give me more details')
#
#
# list = ToDoList()
# list.add_task('learn', 'english')