
number = int(input("Enter your Desired number: "))

def digit_extractor(number):
    digit_list = []
    while number > 0:
        remainder = number % 10
        number = number // 10
        digit_list.append(remainder)
    print(digit_list[-2])

digit_extractor(number)
