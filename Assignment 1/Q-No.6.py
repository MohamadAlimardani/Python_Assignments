
number = int(input("Enter your Desired number: "))

second_digit = (number % 100) // 10

fifth_digit = (number % 100000) // 10000

sum = second_digit + fifth_digit

print("Sum of Specified Digits is:" , sum)