
number = int(input("Enter your Desired number: "))

const = (0 , 1 , 2 , 10)
even_counter = const[0]
odd_counter = const[0]

while number > const[0]:
    remainder = number % const[3]
    number = number // const[3]

    if remainder % const[2] == const[0]:
        even_counter += const[1]

    else:
        odd_counter += const[1]

if even_counter > odd_counter:
    print("\nEven = " , even_counter , "\nODD = " , odd_counter , "\nThere is more Even Digits than ODD Digits in the given number. ")

elif even_counter == odd_counter:
    print("\nEven = " , even_counter , "\nODD = " , odd_counter , "\nThere is an equal number of ODD and Even Digits in the given number. ")

else:
    print("\nEven = " , even_counter , "\nODD = " , odd_counter , "\nThere is more ODD Digits than Even Digits in the given number. ")
