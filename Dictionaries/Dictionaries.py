from collections import OrderedDict



#INDEXING DICTS: you index dicts.., by using its key
grocery = {
    'banana': 234,
    'apple': 321
} #where banana is the key and 234 is the value and so forth

print(grocery['banana'])
#.get() is a built-in function for dict. It basically get a value for us.
print(grocery.get('apple'))

for key in grocery:
    print(key, grocery[key])

#ADDING TO DICTS
grocery['strawberry'] = 454
print(grocery)

#The four most used methods in Dicts are:
# (1) dict.items()
print(grocery.items()) #you can cast these into a list by printing: # print(list(grocery.items()))
# (2) dict.keys()
print(grocery.keys())
# (3) dict.values()
print(grocery.values())
# (4) dict.pop(key)
print(grocery.pop('strawberry'))
print(grocery)


#NESTED DICTS
contacts = {
    'Israel': {
    'phone': '09060008209',
    'course': 'Software Engineering',
    'programming language': 'Python',
    },
    'Duncan': {
    'phone': '09060008209',
    'course': 'Cyber Security',
    'programming language': 'JavaScript',
    },
}

print(contacts)
