
number_of_names = int(input("Enter The Amount of names You Want to Enter: "))

names , no_duplicate_names , i = list() , list() , 0

for i in range(number_of_names):
    name_input = input("Enter You're Desired Name: ")
    names.append(name_input)

for name in names:
    if name not in no_duplicate_names:
        no_duplicate_names.append(name)
    
    else:
        continue

print("\n" + 2 * " " + "Names: " + 5 * " " + "Amount of That Name: \n")
for name in no_duplicate_names:
    count_name = names.count(name)
    length = 18 - len(name)
    print(2 * " " + "\'" + str(name) + "\'" , length * " " , str(count_name) + "\n")