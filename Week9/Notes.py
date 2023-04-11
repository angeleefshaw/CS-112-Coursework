# Python Dictionaries

siblings = {
    "Angelee": 7,
    "Justine": 9,
    "John": 3
}

print(siblings.keys())
print('')
print(siblings.values())
print('')
print(siblings.items())


# print(siblings.get('Angelee'))

# for person in siblings:
#     print(person, siblings[person])

# #boolean operator
# if 'Angelee' in siblings:
#     print('Angelee is in the dictionary!')

# print(len(siblings))

# total = 0
# for name in siblings:
#     total += siblings.get(name)

# print(total)

siblings['Markus'] = 8
siblings['Markus'] = 10

movies = {}

print(movies['Casablanca']['year'])

#print(movies)
for key in movies: 
    print(key)