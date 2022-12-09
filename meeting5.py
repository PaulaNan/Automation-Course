def say_hi():
    print('hi')


say_hi()
# name = parameter = variabila neinitializata
def say_hi_user(name, surname):
    print(f'hello {name} {surname}')

# Ioana = argument
say_hi_user('Ioana', 'M')

# input 3 numbers
# output = set
def make_set(n1, n2, n3):
    r = set()
    r.add(n1)
    r.add(n2)
    r.add(n3)
    return r

print(make_set(1, 2, 3))
print(make_set(1, 2, 2))
set1 = make_set(1, 2, 3)
set2 = make_set(1, 2, 2)
print(set1.intersection(set2))
print(make_set(1, 2, 3).intersection(make_set(2, 3, 3)))

# return without param
def pi_value():
    return 3.14

x = pi_value() + 4
print(x)


# how to use functions from other file
from folder.helpers import sums # import only sums
print(sums(3, 4)) # * import all

# practice
# tax calculator as cmc
cc = int(input('choose cmc '))
tax = None


def tax_calculator(cc_input, hybrid_input):
    if hybrid_input == True:
        return 10
    else:
        if cc_input < 1000:
            return 70
        elif cc_input < 2000:
            return 160
        else:
            return 900

tax = tax_calculator(cc, False)
print(tax) # cc = 49 - 70
tax = tax_calculator(2400, False)
print(tax) # 900
tax = tax_calculator(2400, True)
print(tax) # 10


# gas under 15% warning return % gas remaining
CANISTER = 50
gas = int(input('remaining gas '))
remaining_gas = None


def remaining_gaz(gas_input):
    if gas_input >= CANISTER:
        print('nu can not have more than canister')
        return 'N/A'
    if gas_input < 0:
        print('you can not have negative values')
        return 'N/A'
    percentage = gas / CANISTER * 100
    if percentage < 15:
        print('low gas')
        return percentage


remaining_gas = remaining_gaz(gas)
print(f'you have {remaining_gas} % gas')

# input name girl or boy return boy or girl
name = str(input('choose a name '))
name.capitalize()
except_girls = ['Carmen', 'Beatrice']
except_boys = ['Mihnea', 'Mircea', 'Horia']


def name_type(name_input):
        if name_input[len(name_input)-1] != 'a' and name_input in except_boys:
            return 'it is a boy'
        else:
            return 'it is a girl'


print(name_type(name))