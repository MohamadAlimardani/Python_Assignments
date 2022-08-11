
number = int(input("Enter you're Desired Number: "))
const = (0 , 7)

if number % const[1] == const[0]:
    print("The Given number is a multiple of 7. ")

else:
    next_number = number + (const[1] - number % const[1])
    print("The Given number is not a multiple of 7. " , "\nThe Next Number that is a multiple of 7 is " + str(next_number) + ".")