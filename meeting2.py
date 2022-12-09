# operatori de atribuire =
x = 3
x += 3 # x = x+3
print(x)
# operatori aritmetici + - / *
print(4 +5)
# operatori de comparare == != > < >= <=
print(x >= 5) # true
print(3 == 3) # true
print(3 != 3) # false
# operatori logici and or not
print(3 > 1 and 5 > 1) # true and true - true
print(-3 > 1 and 5 > 1) # false and true - false
print(3 > 1 or 5 > 1) # true or true - true
print(3 > 1 or -5 > 1) # true or false - true
print(-3 > 1 or -5 > 1) # false or false - false
print(not(-3 > 1 or -5 > 1)) # false or false - false - not false = true
print(-3 > 1 or 3 > 1 and 5 > 1) # false or true(true and true) - true

# if else
NOTA_DE_TRECERE_EXAMEN = 5 # scrisa cu litera mare e constanta, nu trebuie schimbata niciodata
NOTA_DE_TRECERE_PURTARE = 7
nota_examen = 10
nota_purtare = 10
if nota_purtare >= NOTA_DE_TRECERE_PURTARE and nota_examen >= NOTA_DE_TRECERE_EXAMEN:
    print('am trecut')
    if nota_purtare ==10 and nota_examen == 10:
        print('esti pe primul loc')
else: # nu are conditie, deoarece e ce a mai ramas
    print('nu am trecut')

# il elif else
optiune = int(input('alege o optiune: 1 romana, 2 engleza, 0 meniu anterior'))
if optiune == 0:
    print('meniul anterior')
elif optiune == 1:
    print('ai ales romana')
    optiune2 = int(input('persoana fizica 1, persoana juridica 2'))
    if optiune2 == 1:
        print('ai ales persoana fizica')
    elif optiune2 == 2:
        print('ai ales persoana juridica')
    else:
        print('nu ai ales corect, mai incearca')
elif optiune == 2:
    print('you choose english')
    optiune3 = int(input('individual 1, company 2'))
    if optiune3 == 1:
        print('you choose individual')
    elif optiune3 == 2:
        print('you choose company')
    else:
        print('is not correct, try again')
else:
    print('nu ai ales corect, mai incearca')


# boarding
mother = True
father = True
age = 17
mother_accord = True
father_accord = False
passport = False

if passport == False:
    print('you can\t go')
else:
    if age >= 18:
        print('you can go on board')
    else:
        if mother == True and father == True:
            print('you can go on board')
        elif mother == True and father == False and father_accord == True:
            print('you can go on board')
        elif mother == False and father == True and mother_accord == True:
            print('you can go on board')
        else:
            print('you need a parent')
