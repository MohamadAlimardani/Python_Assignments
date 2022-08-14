
number = int(input("Enter your Desired number: "))

even_counter = 0
odd_counter = 0

while number > 0:
    remainder = number % 10
    number = number // 10

    if remainder % 2 == 0:
        even_counter += 1

    else:
        odd_counter += 1

if even_counter > odd_counter:
    print("\nEven = " , even_counter , "\nODD = " , odd_counter , "\nThere is more Even Digits than ODD Digits in the given number. ")

elif even_counter == odd_counter:
    print("\nEven = " , even_counter , "\nODD = " , odd_counter , "\nThere is an equal number of ODD and Even Digits in the given number. ")

else:
    print("\nEven = " , even_counter , "\nODD = " , odd_counter , "\nThere is more ODD Digits than Even Digits in the given number. ")
