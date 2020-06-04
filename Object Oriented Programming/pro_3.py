'''
Write a Python program to get the class name of an instance in Python.
'''

class Animal:
    def __init__(self, name):
        self.name = name


animal = Animal("Goat")
print(animal.name)
print(type(animal.name))