# (1)
#

list_of_fruits = {'blueberry', 'banana', 'mango'}
list_of_numbers = [1,2,2,3,4,4,5,6,6,6,7]

no_duplicate_set = set(list_of_numbers)
no_duplicate_list = list(no_duplicate_set)

list_of_numbers = no_duplicate_set

print(list_of_numbers)

# (2)

library1 = {'Harry Potter', 'End Game', 'Thor', 'Batman'}
library2 = {'Naruto', 'GodHand', 'End Game'}

#town_library = library1.union(library2) #Return a set containing the union of sets
#town_library = library1.intersection(library2) #Returns a set, that is the intersection of two other sets
town_library = library1.difference(library2) #Returns a set containing the difference between two or more sets

print(town_library)