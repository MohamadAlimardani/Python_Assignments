
import re as r

print("\n " + 4 * "*" + " Time Conversion " + 4 * "*" + "\n " + 23 * "_" + "\n" 
+ "| -Choose an Option: " + 3 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
+ "\n| 1.Sec To Hour." + 8 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
+ "\n| 2.Hour To Sec." + 8 * " " + "|" + "\n" + "|" + 23 * "_" + "|\n\n")

time_menu = int(input("-Waiting For You're Desire: "))
flag = False

if time_menu == 1:
    seconds = int(input("Enter The Amount of Seconds You Desire: "))
    minutes = seconds
    hour = seconds
    days = seconds

    seconds %= 60

    minutes //= 60
    minutes %= 60

    hour //= 3600
    hour %= 24

    days //= 86400
    
    if days != 0:
        if 0 <= seconds < 10 or 0 <= minutes < 10 or 0 <= hour < 10 or 0 <= days < 10:
            if 0 <= seconds < 10:
                seconds = "0" + str(seconds)

            if 0 <= minutes < 10:
                minutes = "0" + str(minutes)
            
            if 0 <= hour < 10:
                hour = "0" + str(hour)
            
            if 0 <= days < 10:
                days = "0" + str(days)
            
            print(str(days) + " Days & " + str(hour) + " : " + str(minutes) + " : " + str(seconds))
        
        else:
            print(str(days) + " Days & " + str(hour) + " : " + str(minutes) + " : " + str(seconds))

    else:
        if 0 <= seconds < 10 or 0 <= minutes < 10 or 0 <= hour < 10 or 0 <= days < 10:
            if 0 <= seconds < 10:
                seconds = "0" + str(seconds)

            if 0 <= minutes < 10:
                minutes = "0" + str(minutes)
            
            if 0 <= hour < 10:
                hour = "0" + str(hour)
            
            print(str(hour) + " : " + str(minutes) + " : " + str(seconds))
        
        else:
            print(str(hour) + " : " + str(minutes) + " : " + str(seconds))
            
elif time_menu == 2:
    while True:
        if flag is True:
            break
        
        else:
            print("\n")
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
                    print("\nYou're Conversion Into Seconds is equal to " + str(total_seconds) + " Seconds.\n")
                    flag = True
                    break
