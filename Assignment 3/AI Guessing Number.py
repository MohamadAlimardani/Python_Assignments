
import random as ran

def Print_Smaller_Greater_Menu():
    print("Is This " + str(AI_guess) + " The Desired Number? \n" 
    + " " + 23 * "_" + "\n" + "| -Choose an Option: " + 3 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 1.Is it Smaller?" + 6 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 2.Is it Greater?" + 6 * " " + "|" + "\n" + "|" + 23 * "_" + "|\n")

def End_Print():
    print("\nOnly " + str(len(numbers)) + " Tries Took AI To Guess The Desired Number." 
    + "\n\n" + "List of Numbers That AI Has Guessed: \n" + str(numbers) + "\n")

first_interval = 0
end_interval = 99
expected_number = ran.randint(first_interval , end_interval)
numbers =[]

while True:
    Try:
        print("\nExpected Number: " + str(expected_number) + "\n")
        while True:
            AI_guess = ran.randint(first_interval , end_interval)

            if AI_guess in numbers:
                continue

            elif AI_guess not in numbers:
                numbers.append(AI_guess)
                break

        if AI_guess == expected_number:
            End_Print()
            break

        Print_Smaller_Greater_Menu()
        small_great_meanu = input("-Waiting For You're Desire: ")

        if small_great_meanu == "1":
            end_interval = AI_guess
            continue

        elif small_great_meanu == "2":
            first_interval = AI_guess
            continue
    except:
        print("Unfortunately!! We Ran into Some Errors.\n\nRepeat The Guessing Process Again.")
        numbers.clear()
        continue
