
str_input = input("\nEnter You're Desired Set of Numbers: ")

for chr in str_input:
    if chr == ",":
        str_input = str_input.replace("," , " ")

print("\n\nList:\t", list(map(int, str_input.split())), "\n")
print("Tuple:\t", tuple(map(int, str_input.split())), "\n")
print("Set:\t", set(map(int, str_input.split())), 2 * "\n")