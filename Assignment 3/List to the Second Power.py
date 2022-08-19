
import random as ran

numbers = []
random_numbers = []
second_power = []

while True:
    random_number = ran.randint(1 , 100)

    if random_number in numbers:
        continue
    
    else:
        numbers.append(random_number)

    if len(numbers) == 20:
        break

print("\nList of Numbers: \n" + str(numbers) + "\n")

for num in numbers:
    second_power.append(num ** 2)

print("List of Numbers That Raised To The Second Power: \n" + str(second_power) + "\n")
