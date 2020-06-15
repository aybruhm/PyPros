'''
Write a python class to reverse a string word by word.
'''

class Word:
    word = input('Input string: ')

    @classmethod
    def reverse(cls):
        string = cls.word
        print('Reverse string: ', string[6::1])

_word = Word()
print(_word.reverse())