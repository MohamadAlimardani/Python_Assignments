
import os

def set_of_colors():
    colors_list = list()
    print("Enter You're Desired Set of Colors: ")
    while True:
        color_input = input()

        if color_input == "-1":
            return tuple(colors_list)

        colors_list.append(color_input)

def valid_colors():
    for clr in colors_1:
        if clr not in colors_2:
            print(clr, end = "\t")

os.system("cls")
colors_1 = set_of_colors()
os.system("cls")
colors_2 = set_of_colors()
os.system("cls")
valid_colors()
