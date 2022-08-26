
counter = ["1st" , "2nd" , "3rd" , "4th" , "5th" , "6th" , "7th" , "8th" , "9th" , "10th"]

flag_ascending , flag_descending , flag_sorted , i , j , numbers = False , False , True , 1 , 1 , list()

for count in counter:
    print("Enter You're " + str(count) + " Desired Number: " , end = "")
    number = int(input())
    numbers.append(number)

element = numbers[0]

while i < len(numbers):
    if numbers[i] < numbers[i-1]:
        flag_ascending = True
    i += 1

while j < len(numbers):
    if numbers[j] > numbers[j-1]:
        flag_descending = True
    j += 1

for num in numbers:
    if element != num:
        flag_sorted = False

if flag_sorted:
    print("The Given List is Already Sorted.\n" + str(numbers))

else:
    if not flag_ascending:
        print("The Given List is Sorted Ascending.\n" + str(numbers))
        
    if not flag_descending:
        print("The Given List is Sorted Descending.\n" + str(numbers))

    if flag_ascending and flag_descending:
        print("The Given List is Not Sorted in Any Orders.\n" + str(numbers))