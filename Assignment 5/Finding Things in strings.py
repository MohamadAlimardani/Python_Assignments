
from tabulate import tabulate
import colorama

colorama.init()
start_red = "\033[1;91m"
end_red = "\033[0;0m"

start_cyan = "\033[1;96m"
end_cyan = "\033[0;0m"

str_input = input("Enter You're Desired String: ")

str_input_v1 = str_input
str_input_v2 = str_input

number_of_letters = 0
alphabets = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" ,
             "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z"] 

elements_list = ["." , "," , "/" , "\\" , "[" , "]" , "{" , "}" , "!" , "#" , "&" , "(" , 
                 ")" , "*" , "^" , ":" , ";" , "\'" , "\"" , "<" , ">" , "|" , "$" , "%" ,
                 "~" , "`" , "@" , "?" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0"]
space_enter_list = [" " , "\n"]

#Counting Characters
for se in space_enter_list:
    str_input_v2 = str_input_v2.replace(se , "")

number_of_chars = len(str_input_v2)

# Counting Words
for el in elements_list:
    str_input_v1 = str_input_v1.replace(el , " ")

words_list = str_input_v1.split()
number_of_words = len(words_list)

# Counting Spaces
number_of_spaces = str_input.count(" ")

# Counting Enters
number_of_enters = str_input.count("\n")

# Counting Dots 
number_of_periods = str_input.count(".")

# Counting Commas
number_of_comma = str_input.count(",")

# Counting Letters
for chr in str_input:
    if chr.lower() in alphabets:
        number_of_letters += 1
    else:
        continue

headers_PvP = [start_cyan + "Words" + end_cyan , start_cyan + "Letters" + end_cyan , 
               start_cyan + "Characters" + end_cyan , start_cyan + "Dots" + end_cyan , 
               start_cyan + "Commas" + end_cyan , start_cyan + "Spaces" + end_cyan , 
               start_cyan + "Enters" + end_cyan]

table_PvP = [[start_red + str(number_of_words) + end_red , start_red + str(number_of_letters) + end_red ,
              start_red + str(number_of_chars) + end_red , start_red + str(number_of_periods) + end_red ,
              start_red + str(number_of_comma) + end_red , start_red +  str(number_of_spaces) + end_red ,
              start_red + str(number_of_enters) + end_red]]

print(tabulate(table_PvP , headers_PvP , tablefmt="fancy_grid") , "\n")