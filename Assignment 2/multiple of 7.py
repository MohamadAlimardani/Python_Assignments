
number = int(input("Enter you're Desired Number: "))

if number % 7 == 0:
    print("The Given number is a multiple of 7. ")

else:
    next_number = number + (7 - number % 7)
    print("The Given number is not a multiple of 7. " , "\nThe Next Number that is a multiple of 7 is " + str(next_number) + ".")
