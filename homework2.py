x = int(input('choose a number '))

# verify if x is a negativ, positive or neutral number
if x == 0:
    print(f'{x} is a neutral number')
elif x > 0:
    print(f'{x} is a positive number')
else:
    print(f'{x} is a negative number')

# verify if x is between -2 and 13
if -2 <= x <= 13:
    print(f'{x} is between -2 and 13')
else:
    print(f'{x} is not between -2 and 13')

#verify if the difference between x and y is less than 5
y = int(input('choose another number '))
z = x - y
if z < 5:
    print(f'the difference between {x} and {y} is less than 5')
else:
    print(f'the difference between {x} and {y} is grater than 5')

# verify if x is not between 5 and 27
if not(5 > x < 27):
    print(f'x is between 5 and 27')
else:
    print(f'x is not between 5 and 27')

# verify if x = y and print witch is bigger
if x == y:
    print(f'{x} and {y} are equal')
elif x > y:
    print(f'{x} is bigger than {type}')
else:
    print(f'{x} is less than {y}')

# add another number and find out what type of triangle it is
z = int(input('choose the third number '))
if x == y != z or x == z != y or y == z != x:
    print('the triangle is isoscel')
elif x == y == z:
    print('the triangle is equilateral')
else:
    print('the triangle is some triangle')

# verify if the letter is a vowel - funct casefold()
letter = str(input('choose a letter '))
if letter.upper() in ('a', 'e', 'i', 'o', 'u'):
    print(f'{letter} is a vowel')
elif letter.lower() in ('a', 'e', 'i', 'o', 'u'):
    print(f'{letter} is a vowel')
else:
    print(f'{letter} is a consonant')

# transform grades rto romanian sistem
nota = float(input('enter your grade: '))
if nota > 10 or nota <1:
  print('the grade is invalid, try again')
if nota >= 9:
    print('you took an A')
elif nota >= 8:
    print('you took an B')
elif nota >= 7:
    print('you took an C')
elif nota >= 6:
    print('you took an D')
elif nota >= 5:
    print('you took an E')
else:
    print('you took an F')

# verify if x has minim 4 characters-------
# if x >= -1000 or x >= 1000: # if x /100 >1:
# number = int(input('write a number '))
# m = len(str(number))
# if m == 4:
#     print(f'the number {number} has 4 digits')
# else:
#     print(f'the number {number} does not have 4 digits')

# verify if x is even number or odd number
if x % 2 == 0:
    print(f'the number {x} is even number')
else:
    print(f'the number {x} is an odd number')

# read from keyboard a int and show the string without last x characters
x_string = int(input('Choose a number '))
string = 'Coral is either the stupidest animal or the smartest rock'
print(string[0:-x])

# print first and last 5 characters
print(string[:5], string[-5:])

# type a str and check if fist and last characters are the same
string2 = str(input('write something ')).lower()
assert string2[0] == string2[-1]
print('primul si ultimul sunt la fel')

# given the str, show the even and odd numbers-------------------
# number_str = '0123456789'
# slice2 = slice(1)
# par = slice2 % 2
# if par == 0:
#   print(f"the number {number_str[]} is even")
# else:
#   print(f'the number {number_str[]} is odd')

# generate a random number to play roll dice
import random
choose = int(input('choose a number '))
dice_roll = random.randint(1, 6)
if choose == dice_roll:
  print(f'you win. you choose {choose}, and it was {dice_roll}')
else:
  print(f'you loose. you choose {choose}, but it was {dice_roll}')


# verify if the angles of triables are valid sum between them = 180--------
x = int(input('choose first angle= '))
y = int(input('choose second anglei= '))
z = int(input('choose third angle= '))
if 0<x<179 and 0<y<179 and 0<z<179:
  print('the triangle is valid')
else:
  print('the triangle is not valid')