
print("\n")
str_input = input("Enter Ypu're Desired Sentence: ")
print("\n")
split_element = input("Enter You're Desired Splition Element: ")
print("\n")
join_element = input("Enter You're Desired Concatenate Element: ")

result = join_element.join(str_input.split(split_element))

print("\n\nResult is: " + result + "\n\n")