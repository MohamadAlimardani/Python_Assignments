
speed_mph = float(input("Enter The Speed in MPH: "))

speed_kph = speed_mph * 1.609
format_speed_kph = "{:.2f}".format(speed_kph)

print("The Speed in KPH is: " , format_speed_kph)