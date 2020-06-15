l = [1,2,3,4,5]
l2 = [1, 'String', 'Israel', 3.45, True]

# Indexing through a list
print(l2[0])
print(l2[1])
print(l2[2])
print(l2[3])
print(l2[4])

names = ["Joe", "John", "James"]
print(names)

# Append literally means adding something(could be a name or something) to a list,
# usually at the end of the list.
names.append("Gary")
print(names)

# Insert means inserting anything you want to a specific order or place
names.insert(1, "Israel")
print(names)

# Reverse literally reverse the whole list
names.reverse()
print(names)

numbers = [5, 6, 7, 3, 8, 12]
print(numbers)

# Sort(sorting) runs from the least number to the highest number
numbers.sort()
print(numbers)

for number in numbers:
	print(numbers)