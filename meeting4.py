# while/ else
i = 0
while i <= 3:
    print(i)
    i += 1
else:  # optional, only one time at the end of the loop
    print(' out of the loop, i >3')

# for/ else - takes the index
for j in range(20, 41, 2):  # from where, until where, last character is not shown
    print(j)
else:
    print(f'at the end j is {j}')

for j in range(40, 21, -2):  # from where, until where, last character is not shown
    print(j)
else:
    print(f'at the end j is {j}')

colors = ['blue', 'red', 'pink', 'green', 'white', 'red']
for c in range(len(colors)):
    print(f'my favorite colo is {colors[c]}')
    if colors[c] == 'white':
        colors[c] = 'purple'
print(colors)

# for each - all elements - takes the element
for color in colors:
    if color == 'purple':
        print(color)
        index = colors.index('purple')
        colors[index] = 'magenta'  # over wright
print(f'colors are {colors}')

grades = [3, 5, 8, 10]
the_sum = 0
for grade in grades:
    print(type(grade))
    the_sum = the_sum + grade
else:
    average = the_sum / len(grades)
    print(f'the average is {average}')

# break - getting out of for
for i in range(100):
    if i == 7:
        break  # when we look a value on a list
    print(i)
print('continue with the folder')

# continue - skip the current iteration, getting the cod at the starting point of cod
i = 0
for i in range(0, 20):
    if i == 7:
        continue
    print(f'i is {i}')

# practice
# speed up until gas is out
gas = 9
used = 1
while gas > 0:
    gas = gas - used
    print(f'accelerate! you have {gas} l')
    if gas <= 3:
        print('red light')
else:
    print('go to a gas station')

# print positive numbers
numbers = [-2, 4, 6, -5, 0, 12]
numbers1 = []
for number in numbers:  # each
    if number > 0:
        print(number)
        numbers1.append(number)
print(numbers1)

for number in numbers:
    if number <= 0:
        continue  # skip
    print(number)

# for each in dict
grades = {
    'andi': 10,
    'mara': 7,
    'ana s': 7,
    'ana d': 8
}
counter = 0
for student, grade in grades.items():
    # print(student)
    # print(grade)
    if grade >= 9:
        print(f'{student} get grade {grade}')
    if grade == 7:
        counter += 1
print(counter)
# holypython.com
# list python exercises
