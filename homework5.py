# ex.1 function that return sum of 2 numbers
import pytz


def print_numbers(number1, number2):
    result = number1 + number2
    return result


print(f'sum is {print_numbers(2, 2)}')


# ex.2 function that return True if a number is even, false for odd


def type_numbers(number1):
    if number1 % 2 == 0:
        return f'The number {number1} is even'

    else:
        return f'The number {number1} is odd'


print(type_numbers(3))


# ex.3 function that return total number of characters of your name


def name(name):
    return len(name)


print(f'The length of name is', name('paula'))


# ex.4 function that returns rectangle area


def rectangle_area(number1, number2):
    area = number1 * 2 + number2 * 2
    return area


print(f'the rectangle area is', rectangle_area(2, 4))
# ex.5 function that returns circle area
PI = 3.14


def circle_area(radius, PI):
    the_area = PI * radius * radius
    return the_area


print(f'the circle area is', circle_area(4, PI))


# ex.6 function that return True if a character is in a str
# def notes(string):
#   if note['a'] in notes:
#     return True
#   else:
#     return False
# notes('We go to the mountains tomorrow')
# ex.7 function without return. receive a string and print nr of characters lower case is, and upper case is

# ex.8 function that receive a list of numbers and returns  a list with positive numbers------------


def positive_numbers(num1, num2, num3, num4):
    if num1 > 0 or num2 > 0 or num3 > 0 or num4 > 0:
        num_ok = num1 + num2 + num3 + num4
        return num_ok


print(f'positive numbers are', positive_numbers(4, 5, -1, 2))


# ex.9 function that returns nothing. Receive 2 numbers and print: first is larger than second, the second is larger than first, numbers are equals
def comparison(num1, num2):
    if num1 > num2:
        print(f'the number {num1} is larger than number {num2}')
    elif num1 < num2:
        print(f'the number {num2} is larger than number {num1}')
    else:
        print(f'the number {num1} is equal to {num2}')


comparison(4, 6)


# ex.10 function that receive a number and a set of numbers. Print i added the number in set + return True, Print i didn't added the number, it is already there + return false
# -------------------------------------------

def set_numbers(number, sets):
    sets = {}
    if number in sets:
        print(f'the number {number} is already there')
        return False
    else:
        return True
        print(f'i added the number {number} to the set {sets}')


set_numbers(2, {2, 3, 5, 6})

# optionals
# ex.1 function that receive a month and return how many days is in it-------------------
year = {
    'january': 31,
    'february': 28,
    'march': 31,
    'april': 30,
    'may': 31,
    'june': 30,
    'july': 31,
    'august': 31,
    'september': 30,
    'october': 31,
    'november': 30,
    'december': 31
}


def days_of_month(key):
    return days_of_month


print(days_of_month)


# ex.2 calculator function that returns 4 values: sum, divided, multiplication, difference of 2 numbers


def calculator(a, b):
    sum_num = a + b
    the_dif = a - b
    multiplication = a * b
    division = a / b
    return sum_num
    return the_dif
    print(f'the difference is {a - b}')
    return multiplication
    print(f'result of multiplication is {a * b}')
    return division
    print(f'the division is {a / b}')


print('The sum is')
print(calculator(10, 2))
calculator(10, 2)


# ex.3 function that receive a list 0-9, return dict - how many times appears every number

def list_dict(dictionary):
    dictionary = {
        0: 0,
        1: 2,
        2: 0,
        3: 1,
        4: 0,
        5: 3,
        6: 0,
        7: 2,
        8: 0,
        9: 1
    }
    return list_dict()


# ex.4 function that receive 3 numbers and returns max value between them


def max_value(num1, num2, num3):
    sum_max = num1 + num2 + num3
    return sum_max


print(' max value is')
print(max_value(3, 5, 9))

# ex.5 function that receive a number and returns the sum of all numbers between 0 and that number---------------------
# def sum_all_numbers(num):
#     if num == 0:
#         return 0
#     else:
#         return sum(0, num)
#
# sum_all_numbers(5)
# bonus
# ex. 1function that receive 2 lists of numbers, return common numbers-----------------------------
list1 = [1, 5, -6, 0, 4]
list2 = [2, 5, 6, -7, 4]


# def common_numbers(list1, list2):


# ex.2 function that takes a discount. If product is 100 - 10% discount = 90. invalid discount 110%
def discount(price):
    disc = price * 10 / 100
    new_price = price - disc
    return new_price


print(f'The price after the discount is')
print(discount(100))

# ex.3 function that shows date and time for ro and china
import pytz


def current_time():
    current_time_ro = current_time.datetime.now()
    print(f'current time in Romania is {current_time_ro}')
    return current_time_ro
    current_time_china = datetime.datetime.now(pytz.timezone('China/Beijing'))
    return current_time_china
    print("The current time in China is :", current_time_china)


print('The time in Romania is', current_time.datetime.now())

# ex.4 function that shows how many day until your birthday/ christmas..
from datetime import date, datetime

christmas_day = date(year=2022, month=12, day=25)
days_til_christmas = (christmas_day - date.today()).days
print('Days until christmas', days_til_christmas)
