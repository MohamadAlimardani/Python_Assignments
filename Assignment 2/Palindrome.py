
print("\n\nNote:If a Number is equal to It's reverse It's called a Palindrome Number. ")
number = int(input("Enter you're Desired Number: "))

original_number = number

reverse_number = 0

while number > 0:
    remainder = number % 10
    reverse_number = (reverse_number * 10) + remainder
    number = number // 10
    
if original_number == reverse_number:

    print("The number is palindrome.\n\n\n")

else:
    print("The number is not palindrome.\n\n\n")
