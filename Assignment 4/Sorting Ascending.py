
counter = ["1st" , "2nd" , "3rd" , "4th" , "5th" , "6th" , "7th" , "8th" , "9th" , "10th"]

flag_ascending , i , temp , numbers = False , 1 , 0 , list()

for count in counter:
    print("Enter You're " + str(count) + " Desired Number: ")
    number = int(input())
    numbers.append(number)

element = numbers[0]

while i < len(numbers):
    if numbers[i] < numbers[i-1]:
        flag_ascending = True
    i += 1

if not flag_ascending:
    print("The Given List is Already Sorted Ascending.\n" + str(numbers) + "\n")

else:
    for k in range(len(numbers)):
        for j in range(k + 1 , len(numbers)):
            if not numbers[k] < numbers[j]:
                temp = numbers[k]
                numbers[k] = numbers[j]
                numbers[j] = temp

    print("The List Has been Sorted in Ascending Order: \n" + str(numbers))