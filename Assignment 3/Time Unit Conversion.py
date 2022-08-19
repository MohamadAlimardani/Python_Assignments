
import datetime as dt
import re as r


print("\n " + 4 * "*" + " Time Conversion " + 4 * "*" + "\n " + 23 * "_" + "\n" 
+ "| -Choose an Option: " + 3 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
+ "\n| 1.Sec To Hour." + 8 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
+ "\n| 2.Hour To Sec." + 8 * " " + "|" + "\n" + "|" + 23 * "_" + "|\n\n")

time_menu = int(input("-Waiting For You're Desire: "))
flag = False

if time_menu == 1:
    seconds = int(input("Enter The Amount of Seconds You Desire: "))
    converted_sec = str(dt.timedelta(seconds = seconds))
    print(converted_sec)

elif time_menu == 2:
    while True:
        if flag is True:
            break
        
        else:
            h_m_s = input("Enter You're Desired Time: ")
            numbers = r.findall('[0-9]+' , h_m_s)
            for i in range(len(numbers)):
                numbers[i] = int(numbers[i])
                
            for i , time_unit in enumerate(numbers):
                if not 0 <= numbers[i] <= 23:
                    print("Invalid Input!")
                    break
                
                elif not 0 <= numbers[i+1] <= 59:
                    print("Invalid Input!")
                    break
                
                elif not 0 <= numbers[i+2] <= 59:
                    print("Invalid Input!")
                    break
                
                else:
                    hour_to_second = numbers[i] * 3600
                    minute_to_second = numbers[i+1] * 60
                    total_seconds = hour_to_second + minute_to_second + numbers[i+2]
                    print("You're Conversion Into Seconds is equal to " + str(total_seconds) + " Seconds.")
                    flag = True
                    break