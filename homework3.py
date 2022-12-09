# ex1 declare a list with musicals, show it, reverse it, overwrith it
music = [ 'do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(music)
music2 = music[::-1]
print(music2)
print(music2[::-1])

# ex2 how many times do appears
print(music.count('do'))

# ex3 given the lists find 2 ways to put them in one
list1 = [ 3, 1, 0, 2]
list2 = [6, 5, 4]
list3 = list1 + list2
print(list3)
print(list1 + list2)

# # ex4 sort and show the list, sort number 0, show the list
print(sorted(list3))

# using a if print list is emty or not
if len(list3) > 0:
  print('lista nu este goala')
else:
  print('lista e goala')

# use a function to delete the list
print(list3.clear())

# check again
if len(list3) > 0:
  print('lista nu este goala')
else:
  print('lista e goala')

# use the dict to show the students
dictionary = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dictionary)
print(dictionary['Ana'], dictionary['Gigel'], dictionary['Dorel'])
for i in dictionary:
  print(dictionary[i])
  print(i)

# ex.9 print the grades for each student
print(f'Ana took the grade ', {dictionary['Ana']})
print(f'Gigel took the grade ', {dictionary['Gigel']})
print(f'Dorel took the grade ', {dictionary['Dorel']})

# ex.10 Dorel get a new grade
dictionary['Dorel'] = 6
print(dictionary)

# ex.11 Gigel is getting out, and Ionica is comming in
dictionary.pop('Gigel')
print(dictionary)
dictionary['Ionel'] = 9
print(dictionary)

# ex. 12 given the set, add day 'monday'
days_of_week = {'monday', 'thursday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}
print(days_of_week)
days_of_week.add('monday')
print(days_of_week)

# ex.13 use if to verify i weekend is a subset of days of week
week_end = {'saturday', 'sunday'}
if week_end.issubset(days_of_week):
  print('week-end days is a subset of days of week')
else:
  print('week-end days is not a subset of days of week')

# ex. 14 print the difference between them
print(days_of_week.difference(week_end))

# ex.15 print the intersection between them
print(days_of_week.intersection(week_end))

# ex. 16 football team on field
football_players = {'Messi', 'Hagi', 'Ronaldo', 'Mutu', 'Chivu'}
ALL_CHANGES = 3
change_made = 2
remain_changes = ALL_CHANGES - change_made
footbal_player_in = 'Marcel'
football_player_out = 'Hagi'

if football_player_out in football_players and remain_changes > 0:
  if footbal_player_in in football_players:
    print('you can\'t make the change, the player is allready on field')
    print(football_players)
  else:
    football_players.remove(football_player_out)
    remain_changes = remain_changes - 1
    football_players.add(footbal_player_in)
    print(f'change made')
    print(f'it got out {football_player_out} and get in {footbal_player_in}, you have {remain_changes} changes left')
    print(f'curent team is {football_players}')
else:
  if change_made <= 0:
    print('you can\'t made the change, you don\'have changes left')
  else:
    print(f'you can\'made the change because the player {football_player_out} is not on nthe field')



