
from tabulate import tabulate

standard_words = list()

str_input = input("Enter All You're Words and Seperate Them With Space: ")

words_list = str_input.split()

for word in words_list:
    standard_words.append(word[:1].upper() + word[1:].lower())

print("\nThe Given Words: \n" + str(words_list) + "\n\nStandardazied Words: \n" + str(standard_words) + "\n")
