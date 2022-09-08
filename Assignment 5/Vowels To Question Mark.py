
from tabulate import tabulate

word_input = input("Enter You're Desired Word: ")

vowels = ["a", "e", "i", "o", "u"]

word_input_v2 = word_input.lower()

for vw in vowels:
    word_input_v2 = word_input_v2.replace(vw, "?")

print(word_input + " Converted To " + word_input_v2 + ".\n")