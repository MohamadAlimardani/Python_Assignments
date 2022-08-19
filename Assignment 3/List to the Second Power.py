
import random as ran

random_numbers = []
second_power = []
while True:
    random_numbers.append(ran.randint(1 , 100))
    if len(random_numbers) is 20:
        break
    else:
        continue

print("\nList of Numbers: \n" + str(random_numbers) + "\n")

for num in random_numbers:
    second_power.append(num ** 2)

print("List of Numbers That Raised To The Second Power: \n" + str(second_power) + "\n")