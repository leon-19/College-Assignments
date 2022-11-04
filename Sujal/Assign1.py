cricket = []
badminton = []
football = []
universalSet = []

# Cricket Players
a = int(input('Enter number of cricket players : '))
for i in range(a):
    b = input(f'Enter player {i+1} name : ')
    cricket.append(b)


# Badminton Players
a = int(input('Enter number of Badminton players : '))
for i in range(a):
    b = input(f'Enter player {i+1} name : ')
    badminton.append(b)


# Football Players
a = int(input('Enter number of Football players : '))
for i in range(a):
    b = input(f'Enter player {i+1} name : ')
    football.append(b)

for player in cricket:
    universalSet.append(player)
for player in badminton:
    if player not in universalSet:
        universalSet.append(player)
for player in football:
    if player not in universalSet:
        universalSet.append(player)

print('Universal Set : ')
print(universalSet)

print('\n***Cricket  Players***')
print(cricket)
print()
print('***Badminton Players***')
print(badminton)
print()
print('***Football Players***')
print(football)


# Cricket and Badminton
cricket_badminton = []
for player in universalSet:
    if player in cricket and badminton:
        cricket_badminton.append(player)
print('\nPlayers who play both cricket and badminton are : ')
print(cricket_badminton)


# Either Cricket or Badminton
cricketOrBadminton = []
for player in cricket:
    if player not in badminton:
        cricketOrBadminton.append(player)
for player in badminton:
    if player not in cricket:
        cricketOrBadminton.append(player)

print('\nPlayers who play either cricket or badminton are : ')
print(cricketOrBadminton)

# Neither cricket nor badminton
noCricketNoBadminton = []
cricketBadmintonUnion = []

for player in cricket:
    cricketBadmintonUnion.append(player)
for player in badminton:
    if player not in cricketBadmintonUnion:
        cricketBadmintonUnion.append(player)

for player in universalSet:
    if player not in cricketBadmintonUnion:
        noCricketNoBadminton.append(player)

print('\nPlayers who play neither cricket nor badminton are : ')
print(noCricketNoBadminton)

# Cricket and Football but not Badminton
cricket_Football = []
for player in universalSet:
    if player not in badminton:
        cricket_Football.append(player)

print('\nPlayers who play cricket and football but not badminton are : ')
print(cricket_Football)
