
print("\n\nNote:If a Number is equal to It's reverse It's called a Palindrome Number. ")
number = int(input("Enter you're Desired Number: "))

const = (0 , 10)

original_number = number

reverse_number = const[0]

while number > const[0]:
    remainder = number % const[1]
    reverse_number = (reverse_number * const[1]) + remainder
    number = number // const[1]
    
if original_number == reverse_number:

    print("The number is palindrome.\n\n\n")

else:
    print("The number is not palindrome.\n\n\n")