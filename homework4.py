# # ex.1 use a for to iterate through the list to show mercedes my favorite car.
# cars = ['audi', 'volvo', 'bMW', 'mercedes', 'aston martin', 'lastun', 'fiat', 'trabant', 'opel']
# for i in cars:
#     if i == 'mercedes':
#         print(f'my favorite car is {i}')
#
# for car in cars:
#     if car == 'trabant':
#         print(car)
#
# # while
# i = 0
# while i < len(cars):
#     i = i + 1
#     print(cars)
#
# # ex.2 use for / else
# for i in range(1, len(cars) - 1):
#     cars[i] = cars[i].capitalize()
# else:
#     print(cars)
#
# # ex.3 buyer want a Mercedes
# for car in cars:
#     if car == 'Mercedes':
#         print('we found the car you want')
#         break
#     else:
#         print(f'we found the car {car}. Still searching...')
#
# # ex.4 the buyer is rinch and indecise. We show him without Trabant and Lastun
# for car in cars:
#     if car == 'Trabant' or car == 'Lastun':
#         continue
#     print(f'you may like car {car}')
#
# # ex.5 create an empty list to upgrade the list
# used_cars = []
# for car in cars:
#     if car == 'Lastun' or car == 'Trabant':
#         used_cars.append(car)
#         cars.remove(car)
#         cars.append('Tesla')
# print(f'used cars: {used_cars}')
# print(f'new list {cars}')
#
# ex.6 create dict. A buyer has 15000 euro
# car_price = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# for model, price in car_price.items():
#     if price >= 15000:
#         print(f'i found {model} with price {price}')
#     else:
#         print(f'for budget under 15000, you may choose {model} with {price}')
#
# # ex.7 find out how many time 3 apears without using count method
# numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# count = 0
# for number in numbers:
#     print(number)
#     if number == 3:
#         count = count + 1
# print(f'the numer 3 in {count} times in the list')
#
# # ex.8 find out the sum without using sum method
# sum = 0
# for number in numbers:
#     sum = sum + number
# print(f'the sum is {sum}')
#
# # ex.9 find out the larger number without using max method-------
# max_number = 0
# for number in numbers:
#     if number > max_number:
#         max_number = number
# print(f'the largest number is {max_number}')
#
# # ex.10 if number>0 replace with his negative value
# for number in numbers:
#     if numbers[number] >= 0:
#         numbers[number] = numbers[number] * -1
#     else:
#         numbers[number] = numbers[number] * -1
# print(f'the numbers are now {numbers}')

# another list

another_list = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
positive_numbers = []
negative_numbers = []
even_numbers = []
odd_numbers = []
for number in another_list:
    if number > 0:
        positive_numbers.append(number)
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    else:
        negative_numbers.append(number)
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
print(f'positive numbers are {positive_numbers}')
print(f'negative numbers are {negative_numbers}')
print(f'even numbers are {even_numbers}')
print(f'odd numbers are {odd_numbers}')

# ex.2 sort the list without using sort method
new_list = []
while another_list:
    minim = another_list[0]
    for number in another_list:
        if number < minim:
            minim = number
    new_list.append(minim)
    another_list.remove(minim)

print(f'the sorted list is {new_list}')

# ex.3 random number to guess
import random

secret_number = int(input('choose a number '))
guest_number = random.randint(1, 100)
while guest_number != secret_number:
    if guest_number > secret_number:
        print(f'secret number {secret_number} is less than the number {guest_number}')
        break
    else:
        print(f'secret number {secret_number} is grater than the number {guest_number}')
        break
else:
    print(f'secret number {secret_number} is equal with the number {guest_number}')

# ex.4 choose a number and make a pyramid
pyramid = int(input('choose a number '))
i = 1
j = 0
while i < pyramid:
    while j <= i - 1:
        print(pyramid, end="")
        j += 1
        print("\r")
        j = 0
        i += 1
        break
# ex.5 phone keyboard print 2d
phone_keyboard = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    [0]
]
row2 = phone_keyboard[0]
print(phone_keyboard[0][1])
