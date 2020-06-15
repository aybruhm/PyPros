
credit_card1 = (1234567890986, 'Israel Abraham', '09/22', 553)
credit_card2 = (2374748576889, 'John Adam', '08/22', 223)

credit_cards = [credit_card1, credit_card2]
print(credit_cards)

#Unpacking Tuples

# (1)

person = ("Israel Abraham", 18, 'Jellof Rice')
name, age, favfood = person

print(name)
print(age)
print(favfood)
print(person)

# (2)

people1 = ("Israel Abraham", 18, 'Jellof Rice')
people2 = ("Kafur Ahmed", 22, 'Fried Rice')

people = (people1, people2)

for name, age, favfood in people:
    print(name)
    print(age)
    print(favfood)
    print()
