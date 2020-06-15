#List Comprehension
names = ['Faith', 'Rebecca', 'Lilian', 'Roseline']

l = []

for people in names:
    l.append(people) #we can add something much interesting down there, lol..
print(l)

print([people + ' dumped me.' for people in names])

movies_and_ratings = {
    'Avengers: End Game': 10,
    'Thor: Ragnarok': 8,
    'Spider Man: Far from home': 6,
    'Hell Boy: Gods Hand': 4,
}

l = []

for movies in movies_and_ratings:
    if movies_and_ratings[movies] > 6:
        l.append(movies)
print(l)
print([movies for movies in movies_and_ratings if movies_and_ratings[movies] > 6])