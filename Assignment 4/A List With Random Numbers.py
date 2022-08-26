
import random as rnd

while True:
    first_interval , end_interval , random_numbers , period_of_numbers = -10**300 , 10**300 , list() , list()
    print("\n")
    length_of_list = int(input("Enter The Amount of Numbers You Desire: "))

    while True:
        random_period = rnd.randint(first_interval , end_interval)

        if random_period in period_of_numbers:
            continue
        
        else:
            period_of_numbers.append(random_period)

        if len(period_of_numbers) == 2:
            if period_of_numbers[0] > period_of_numbers[1]:
                period_of_numbers.clear()
                continue
            
            else:
                break

    while True:
        random_number = rnd.randint(period_of_numbers[0] , period_of_numbers[1])

        if random_number in random_numbers:
            continue
        
        else:
            random_numbers.append(random_number)

        if len(random_numbers) == length_of_list:
            break

    print("\nYou're " + str(length_of_list) + " Random Numbers Is Ready:\n\n" + str(random_numbers) + "\n")