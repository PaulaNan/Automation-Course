# importam librarie externa
import math


marca_masina = 'Volvo'  # snake case
modelMasina = 'XC60'  # camel case
# one line initialization
x, y, z = 'apple', 'banana', 'cherry'
a = b = c = 'orange'
print(x, y, z)
print(a)


# tipuri de date
marca = 'Dacia'  # string
an_fabricatie = 2112  # integer
pret = 12599.52  # float
inamtriculat = True  # boolean


# sintaxa care limiteaza nr de zecimale
a = 3.12345
print('{:.2f}'.format(a))
print(round(a))
# fortam rotunjire in jos
print(math.floor(a))
# fortam rotunjire in sus
print(math.ceil(a))

cifra = '3'
cifra2 = int(cifra) # type casting - transformi un tip de date
print(type(cifra2))

nume = 'Matei'
prenume = 'Paula'
varsta = 33
print('Numele meu este', nume, prenume)
print('Numele meu este ' + nume + ' ' + prenume)
print(f'Numele meu este {nume} si prenumele {prenume}, varsta {varsta}')

# assertul e o modalitate de a face verificari daca nu e true opreste tot
m = 1
print(m == 1)
assert m == 1
print('trec pe aici')
assert m != 2
print('nu trec pe aici')

# default la split este spatiu intre cuvinte
name, age, sex = input('Enter name, age and sex ').split()
print(f'the name is {name}, the age is {age}, and sex is {sex}')

# metodele stringului
print(name.count('a'))
print(name.replace('i', 'y'))
print(name.upper())

# string slicing www.stackoverflow.com/questions/509211/understanding-slice-natation
# my_str[de unde ince*em:pana unde mergem:din cat in cat]
myStr = 'azi e miercuri'
last_index = len(myStr)-1
print(last_index)
print(myStr[13])
print(myStr[0:last_index:2])

# parcurgere inversa
print(myStr[::-1])

