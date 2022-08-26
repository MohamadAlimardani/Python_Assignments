
number = int(input("Enter You're Desired Number: "))

i , fact , number_stages= 1 , 1 , list()

while True:
    i += 1
    fact = fact * i
    
    if fact < number:
        continue
    
    elif fact == number:
        print("The Given Number is a Factorial of Another's Number.\n")
        break
    
    else:
        print("The Given Number is Not a Factorial of Another's Number.\n")
        break