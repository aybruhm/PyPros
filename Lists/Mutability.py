#Immutable/Immutate
#tuples
#integers, floats, boolean


#Mutable
#lists
#Dictionaries
#OrderedDict
t = (1, 2, 3, [4,6,7]) #you can't change a tuple, because it's immutable,
# however, you can change a list in a tuple.
print(t)
t[3][1] = 8 
print(t)