# lists
name = 'Andy'
name_in_a_list = ['A', 'n', 'd', 'y']
print(name_in_a_list[0])
print(len(name_in_a_list))
print(name_in_a_list[0:2])  # slicing
name_in_a_list.remove('d')  # remove by value
print(name_in_a_list)
letter = name_in_a_list.pop()  # remove by index
print(letter)
print(name_in_a_list)
name_in_a_list[0] = 'a'  # overwrite
print(name_in_a_list)
name_in_a_list.insert(0, 'M')  # add in a specific place
print(name_in_a_list)
name_in_a_list.append('S')  # add at the end
print(name_in_a_list)

# list in a list []
list_in_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
row3 = list_in_list[2]
print(row3[0])
print(list_in_list[2][0])

import random

list2 = ['tel', 'tel2', 'tel3']
random_nr = random.randint(0, len(list2) - 1)
print(list2[random_nr])

# sets - unique values {}
vowel = {'a', 'e', 'i', 'o', 'u'}
vowel.add('a')
print(vowel)
abc = {'a', 'b', 'c'}
print(abc.issubset(vowel))
print(abc.union(vowel))
print(abc.intersection(vowel))

letter = 'a'
if letter in vowel:
    print('letter is a vowel')

# tuple - can't be changed = like constant ()
room = (1, 2, 3, 4, 5, 6, 7)
print(room[2])
print(room.count(7))
print(room.index(7))
print(len(room))

# dict key(unique) : value
city = {
    'Hungary': 'Budapest',
    'Bulgaria': 'Sofia',
    'Romania': 'Bucharest',
    'Italy': 'Roma'
}
print(city.get('Romania'))
city['Romania'] = 'Cluj'  # add/ over right
city['Ungary'] = 'Kiev'
print(city)
city.pop('Romania')  # delete
city.update({'Romania': 'Buc', 'Rusia': 'Moscow'})  # update/ add {}
city2 = {'Spain': 'Madrid'}  # another method
city.update(city2)
print(city)
print(city.values())
