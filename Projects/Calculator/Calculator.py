
import os
import sys
import math
import numpy as np
from math import radians
from mpmath import cot

def Print_Main_Menu():
    print("\n\n\nWELCOME! To the Ultimate Calculator. (^_^)\n\n" 
    + " " + 4 * "*" + " Main Menu " + 4 * "*" + "\n " 
    + 23 * "_" + "\n" + "| -Choose an Option: " + 3 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 1.Basic Calculator." + 3 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 2.Advanced Calculator." + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| Q.Exit." + 15 * " " + "|" + "\n" + "|" + 23 * "_" + "|\n")

def Print_Basic_Menu():
    print(" " + 4 * "*" + " Basic Menu " + 4 * "*" + "\n " 
            + 23 * "_" + "\n" + "| -Choose an Option: " + 3 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
            + "\n| 1.Expression." + 9 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
            + "\n| 2.Sum." + 16 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
            + "\n| 3.Subtraction." + 8 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
            + "\n| 4.Multiplication." + 5 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
            + "\n| 5.Division." + 11 * " " + "|" + "\n" + "|" + 23 * "-" + "|" 
            + "\n| 6.Remainder." + 10 * " " + "|" + "\n" + "|" + 23 * "-" + "|" 
            + "\n| 7.Percentage." + 9 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
            + "\n| - Back." + 15 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
            + "\n| Q.Exit." + 15 * " " + "|" + "\n" + "|" + 23 * "_" + "|\n")

def Print_Advanced_Menu():
    print(" " + 4 * "*" + " Advanced Menu " + 4 * "*" + "\n " + 23 * "_" + "\n" + "| -Choose an Option: " + 3 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 1.Trigonometry." + 7 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 2.Other Operations." + 3 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 3.Conversions." + 8 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| - Back" + 16 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| Q.Exit." + 15 * " " + "|" + "\n" + "|" + 23 * "_" + "|\n")

def Print_Trigonometry_Menu():
    print(" " + 4 * "*" + " Trigonometry " + 4 * "*" + "\n " + 23 * "_" + "\n" + "| -Choose an Option: " + 3 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 1.Sin." + 16 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 2.Cos." + 16 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 3.Tan." + 16 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 4.Cot." + 16 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 5.ArcSin." + 13 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 6.ArcCos." + 13 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 7.ArcTan." + 13 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| - Back." + 15 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| Q.Exit." + 15 * " " + "|" + "\n" + "|" + 23 * "_" + "|\n")

def Print_Other_Operations():
    print(" " + 4 * "*" + " Trigonometry " + 4 * "*" + "\n " + 23 * "_" + "\n" + "| -Choose an Option: " + 3 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 1.Square Root." + 8 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 2.Power." + 14 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 3.Factorial." + 10 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 4.Logarithm." + 10 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| - Back." + 15 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| Q.Exit." + 15 * " " + "|" + "\n" + "|" + 23 * "_" + "|\n")

def Print_Log():
    print(" " + 23 * "_" + "\n" + "| -Choose an Option: " + 3 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 1.Base 10." + 12 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 2.Base 2." + 13 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| - Back." + 15 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| Q.Exit." + 15 * " " + "|" + "\n" + "|" + 23 * "_" + "|\n")

def Print_Area_Conversions_Menu():
    print(" " + 4 * "*" + " Area Conversion " + 4 * "*" + "\n " + 23 * "_" + "\n" 
    + "| -Choose an Option: " + 3 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 1.Mile." + 15 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 2.Acre." + 15 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 3.Yard." + 15 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 4.Foot." + 15 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 5.Inch." + 15 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 6.Kilometer." + 10 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 7.Meter." + 14 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 8.Centimeter." + 9 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 9.Milimeter." + 10 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 10.Hectare." + 11 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 11.Are." + 15 * " " + "|" + "\n" + "|" + 23 * "_" + "|\n\n")

def Print_Conversions_Menu():
    print(" " + 4 * "*" + " Area Conversion " + 4 * "*" + "\n " + 23 * "_" + "\n" 
    + "| -Choose an Option: " + 3 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 1.Area." + 15 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 2.BMI." + 16 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 3.Data." + 15 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 4.Length." + 13 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 5.Mass." + 15 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 6.Numeral System." + 5 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 7.Speed." + 14 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 8.Temperature." + 8 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 9.Time." + 15 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 10.Volume." + 12 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| - Back." + 15 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| Q.Exit." + 15 * " " + "|" + "\n" + "|" + 23 * "_" + "|\n\n")

def Inner_Print():
    print(" " + 23 * "_" + "\n" + "| -Choose an Option: " + 3 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
        + "\n| 1.Continue." + 11 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
        + "\n| - Back." + 15 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
        + "\n| Q.Exit." + 15 * " " + "|" + "\n" + "|" + 23 * "_" + "|\n")

def Expression():
    print("Note: Only Use Parentheses for Power Calculations.\n**For the best experience Please Do Not Use Parantheses for Other Calculations.**\n\n")
    input_str = input("Enter You're Desired Expression: ")
    print("The Result of Given Expression is " + str(eval(input_str)) + ".")

def Sum():
    input_string = input("Enter the Numbers you Desire: ")
    input_list = input_string.split()

    for i in range(len(input_list)):
        input_list[i] = int(input_list[i])
    
    print("The Sum of Given Numbers is: " + str(sum(input_list)))

def Subtract():
    input_string = input("Enter the Numbers you Desire: ")
    input_list = input_string.split()

    for i in range(len(input_list)):
        input_list[i] = int(input_list[i])

    subtract = input_list[0] - input_list[1]
    del input_list[0]
    del input_list[0]    
    size = len(input_list)
    i = 0
    for i in range(size):
        subtract = subtract - input_list[i]
        i += 1
    print("The Multiplication of Given Numbers is: " + str(subtract))   

def Multiplication():
    input_string = input("Enter the Numbers you Desire: ")
    input_list = input_string.split()

    for i in range(len(input_list)):
        input_list[i] = int(input_list[i])

    multiply = 1
    for num in input_list:
        multiply = multiply * num

    print("The Multiplication of Given Numbers is: " + str(multiply))

def Division():
        input_string = input("Enter the Numbers you Desire: ")
        input_list = input_string.split()

        for i in range(len(input_list)):
            input_list[i] = int(input_list[i])

        division = input_list[0] / input_list[1]
        del input_list[0]
        del input_list[0]    

        i = 0
        size = len(input_list)
        for i in range(size):
            if input_list[i] != 0:
                division = division / input_list[i]
            
            else:
                print("Division by \'0\' !!" + "\nInvalid Division!" + "\nPlease ReEnter another set of numbers: ")
                Division()
            i += 1
        print("The Multiplication of Given Numbers is: " + str(division))

def Remainder():
    divided = int(input("Enter You're Divided Number: "))
    divisor = int(input("Enter You're Divisor Number: "))

    remainder = divided % divisor

    print("Remainder of " + str(divided) + " to " + str(divisor) + " is " + str(remainder) + ".")

def Percentage():
    number = int(input("Enter You're Desired Number: "))

    percentage = number * 0.1
    foramt_percentage = "{:.2f}".format(percentage)

    print("Percentage of " + str(number) + " is: " + foramt_percentage + "%")

def Sin():
    angle = float(input("Enter You're Desired Angle: "))
    sin_angle = math.sin(angle)
    format_sin_angle = "{:.4f}".format(sin_angle)

    print("Sin(" + str(angle) + ")= " + str(format_sin_angle))

def Cos():
    angle = float(input("Enter You're Desired Angle: "))
    cos_angle = math.sin(angle)
    format_cos_angle = "{:.4f}".format(cos_angle)

    print("Cos(" + str(angle) + ")= " + str(format_cos_angle))

def Tan():
    angle = float(input("Enter You're Desired Angle: "))
    tan_angle = math.tan(angle)
    format_tan_angle = "{:.4f}".format(tan_angle)

    print("Tan(" + str(int(angle)) + ")= " + str(format_tan_angle))

def Cot():
    angle = float(input("Enter You're Desired Angle: "))
    radian_angle = math.radians(angle)
    cot_angle = cot(radian_angle)

    print("Cot(" + str(angle) + ")= " + str(cot_angle))

def ArcSin():
    angle = float(input("Enter You're Desired Angle: "))
    arcsin_angle = math.asin(angle)
    final_arcsin_angle = math.degrees(arcsin_angle)
    format_final_arcsin_angle = "{:.4f}".format(final_arcsin_angle)
    print("ArcSin(" + str(angle) + ")= " + str(format_final_arcsin_angle))

def ArcCos():
    angle = float(input("Enter You're Desired Angle: "))
    arccos_angle = math.acos(angle)
    final_arccos_angle = math.degrees(arccos_angle)
    format_final_arccos_angle = "{:.4f}".format(final_arccos_angle)
    print("ArcCos(" + str(angle) + ")= " + str(format_final_arccos_angle))

def ArcTan():
    angle = float(input("Enter You're Desired Angle: "))
    arctan_angle = math.acos(angle)
    final_arctan_angle = math.degrees(arctan_angle)
    format_final_arctan_angle = "{:.4f}".format(final_arctan_angle)
    print("ArcTan(" + str(angle) + ")= " + str(format_final_arctan_angle))

def Square_Root():
    root = int(input("Enter You're Desired Root: "))
    number = int(input("Enter You're Desired Number: "))

    sqrt = math.pow(number , 1/root)
    format_sqrt = "{:.2f}".format(sqrt)
    print(str(int(root)) + "√" + str(number) + " = " + format_sqrt)

def Power():
    base = int(input("Enter the base: "))
    exp = int(input("Enter the exponent: "))
    temp = exp
    power = pow(base , exp)

    print(str(base) + " raises to the power of " + str(exp) + " : " + str(power) + "\n" , end = "")

    for i in range(exp):
        print(str(base) , end ="")
        temp -= 1
        if 0 < temp < exp:
            for j in range(1):
                print(end = " * ") 

    print(" = " + str(power))

def Factorial():
    number = int(input("Enter You're Desired Number: "))
    temp = number
    fact = math.factorial(number)

    print("\n" + str(number) + "! = " , end = "")

    for i in range(number):
        i += 1
        print(str(temp) , end ="")
        temp -= 1
        if 0 < temp < number:
            for j in range(1):
                print(end = " x ") 
        if i%10 == 0:
            print("\n")

    print(" = " + str(fact) + "\n")

def Log():
    Print_Log()
    log_menu = input("-Waiting for You're Desire: ")
    print("\n")

    if log_menu == "1":
        number = float(input("Enter You're Desired Number: "))

        log_10 = math.log10(number)
        format_log_10 = "{:.2f}".format(log_10)

        print("Log " + str(number) + " in Base 10 is: " + format_log_10)
    
    elif log_menu == "2":
        number = float(input("Enter You're Desired Number: "))

        log_2 = math.log2(number)
        format_log_2 = "{:.2f}".format(log_2)

        print("Log " + str(number) + " in Base 2 is: " + format_log_2)

def Area_Conversion():
    Print_Area_Conversions_Menu()
    first_area_measurement = int(input("-Which Area Measurement You Desire to Convert From: "))
    print("\n")
    second_area_measurement = int(input("-Which Area Measurement You Desire to Convert From: "))
    print("\n")

    if first_area_measurement == 1 and second_area_measurement == 1: #Mile to Mile
        print("Invalid Conversion!!")

    elif first_area_measurement == 1 and second_area_measurement == 2: #Mile to Acre
        acre = int(input("Enter You're Desired Number: "))
        mile_to_acre = 640 * acre

        print("1 Square Mile is equal to " + str(mile_to_acre) + " Acre.")
            
    elif first_area_measurement == 1 and second_area_measurement == 3: #Mile to Yard
        yard = int(input("Enter You're Desired Number: "))
        mile_to_yard = 3097600 * yard

        print("1 Square Mile is equal to " + str(mile_to_yard) + " Yard.")

    elif first_area_measurement == 1 and second_area_measurement == 4: #Mile to Foot
        foot = int(input("Enter You're Desired Number: "))
        mile_to_foot = 27878400 * foot

        print("1 Square Mile is equal to " + str(mile_to_foot) + " Foot.")
            
    elif first_area_measurement == 1 and second_area_measurement == 5: #Mile to Inch
        inch = int(input("Enter You're Desired Number: "))
        mile_to_inch = 4014489599 * inch

        print("1 Square Mile is equal to " + str(mile_to_inch) + " Inch.")
            
    elif first_area_measurement == 1 and second_area_measurement == 6: #Mile to Kilometer
        kilometer = int(input("Enter You're Desired Number: "))
        mile_to_kilometer = 2.589988 * kilometer

        print("1 Square Mile is equal to " + str(mile_to_kilometer) + " Kilometer.")   

    elif first_area_measurement == 1 and second_area_measurement == 7: #Mile to Meter
        meter = int(input("Enter You're Desired Number: "))
        mile_to_meter = 2589988 * meter

        print("1 Square Mile is equal to " + str(mile_to_meter) + " Meter.")
            
    elif first_area_measurement == 1 and second_area_measurement == 8: #Mile to Centimeter
        centimeter = int(input("Enter You're Desired Number: "))
        mile_to_centimeter = 25899881100 * centimeter

        print("1 Square Mile is equal to " + str(mile_to_centimeter) + " Centimeter.")

    elif first_area_measurement == 1 and second_area_measurement == 9: #Mile to Milimeter
        milimeter = int(input("Enter You're Desired Number: "))
        mile_to_milimeter = 2589988110000 * milimeter

        print("1 Square Mile is equal to " + str(mile_to_milimeter) + " Milimeter.")

    elif first_area_measurement == 1 and second_area_measurement == 10: #Mile to Hectare
        hectare = int(input("Enter You're Desired Number: "))
        mile_to_hectare = 258.998811 * hectare

        print("1 Square Mile is equal to " + str(mile_to_hectare) + " Hectare.")

    elif first_area_measurement == 1 and second_area_measurement == 11: #Mile to Are
        are = int(input("Enter You're Desired Number: "))
        mile_to_are = 25900 * are

        print("1 Square Mile is equal to " + str(mile_to_are) + " Are.")

    elif first_area_measurement == 2 and second_area_measurement == 1: #Acre to Mile
        mile = int(input("Enter You're Desired Number: "))
        acre_to_mile = 0.001563 * mile

        print("1 Square Acre is equal to " + str(acre_to_mile) + " Mile.")

    elif first_area_measurement == 2 and second_area_measurement == 2: #Acre to Acre
        print("Invalid Conversion!!")

    elif first_area_measurement == 2 and second_area_measurement == 3: #Acre to Yard
        yard = int(input("Enter You're Desired Number: "))
        acre_to_yard = 4840 * yard

        print("1 Square Acre is equal to " + str(acre_to_yard) + " Yard.")

    elif first_area_measurement == 2 and second_area_measurement == 4: #Acre to Foot
        foot = int(input("Enter You're Desired Number: "))
        acre_to_foot = 43560 * foot

        print("1 Square Acre is equal to " + str(acre_to_foot) + " Foot.")

    elif first_area_measurement == 2 and second_area_measurement == 5: #Acre to Inch
        inch = int(input("Enter You're Desired Number: "))
        acre_to_inch = 6272640 * inch

        print("1 Square Acre is equal to " + str(acre_to_inch) + " Inch.")

    elif first_area_measurement == 2 and second_area_measurement == 6: #Acre to Kilometer
        kilometer = int(input("Enter You're Desired Number: "))
        acre_to_kilometer = 0.004047 * kilometer

        print("1 Square Acre is equal to " + str(acre_to_kilometer) + " Kilometer.")

    elif first_area_measurement == 2 and second_area_measurement == 7: #Acre to Meter
        meter = int(input("Enter You're Desired Number: "))
        acre_to_meter = 4047 * meter

        print("1 Square Acre is equal to " + str(acre_to_meter) + " Meter.")

    elif first_area_measurement == 2 and second_area_measurement == 8: #Acre to Centimeter
        centimeter = int(input("Enter You're Desired Number: "))
        acre_to_centimeter = 40468564 * centimeter

        print("1 Square Acre is equal to " + str(acre_to_centimeter) + " Centimeter.")

    elif first_area_measurement == 2 and second_area_measurement == 9: #Acre to Milimeter
        milimeter = int(input("Enter You're Desired Number: "))
        acre_to_milimeter = 4046856422 * milimeter

        print("1 Square Acre is equal to " + str(acre_to_milimeter) + " Milimeter.")

    elif first_area_measurement == 2 and second_area_measurement == 10: #Acre to Hectare
        hectare = int(input("Enter You're Desired Number: "))
        acre_to_hectare = 0.404686 * hectare

        print("1 Square Acre is equal to " + str(acre_to_hectare) + " Hectare.")

    elif first_area_measurement == 2 and second_area_measurement == 11: #Acre to Are
        are = int(input("Enter You're Desired Number: "))
        acre_to_are = 40.468564 * are

        print("1 Square Acre is equal to " + str(acre_to_are) + " Are.")

    elif first_area_measurement == 3 and second_area_measurement == 1: #Yard to Mile
        mile = int(input("Enter You're Desired Number: "))
        yard_to_mile = 0.00000032283 * mile

        print("1 Square Yard is equal to " + str(yard_to_mile) + " Mile.")

    elif first_area_measurement == 3 and second_area_measurement == 2: #Yard to Acre
        acre = int(input("Enter You're Desired Number: "))
        yard_to_acre = 0.000207 * acre

        print("1 Square Yard is equal to " + str(yard_to_acre) + " Acre.")

    elif first_area_measurement == 3 and second_area_measurement == 3: #Yard to Yard
        print("Invalid Conversion!!")

    elif first_area_measurement == 3 and second_area_measurement == 4: #Yard to Foot
        Foot = int(input("Enter You're Desired Number: "))
        yard_to_Foot = 9 * Foot

        print("1 Square Yard is equal to " + str(yard_to_Foot) + " Foot.")

    elif first_area_measurement == 3 and second_area_measurement == 5: #Yard to Inch
        Inch = int(input("Enter You're Desired Number: "))
        yard_to_Inch = 1296 * Inch

        print("1 Square Yard is equal to " + str(yard_to_Inch) + " Inch.")

    elif first_area_measurement == 3 and second_area_measurement == 6: #Yard to Kilometer
        Kilometer = int(input("Enter You're Desired Number: "))
        yard_to_Kilometer = 0.00000083613 * Kilometer

        print("1 Square Yard is equal to " + str(yard_to_Kilometer) + " Kilometer.")

    elif first_area_measurement == 3 and second_area_measurement == 7: #Yard to Meter
        Meter = int(input("Enter You're Desired Number: "))
        yard_to_Meter = 0.836127 * Meter

        print("1 Square Yard is equal to " + str(yard_to_Meter) + " Meter.")

    elif first_area_measurement == 3 and second_area_measurement == 8: #Yard to Centimeter
        Centimeter = int(input("Enter You're Desired Number: "))
        yard_to_Centimeter = 8361 * Centimeter

        print("1 Square Yard is equal to " + str(yard_to_Centimeter) + " Centimeter.")

    elif first_area_measurement == 3 and second_area_measurement == 9: #Yard to Milimeter
        Milimeter = int(input("Enter You're Desired Number: "))
        yard_to_Milimeter = 836127 * Milimeter

        print("1 Square Yard is equal to " + str(yard_to_Milimeter) + " Milimeter.")

    elif first_area_measurement == 3 and second_area_measurement == 10: #Yard to Hectare
        Hectare = int(input("Enter You're Desired Number: "))
        yard_to_Hectare = 0.000083613 * Hectare

        print("1 Square Yard is equal to " + str(yard_to_Hectare) + " Hectare.")

    elif first_area_measurement == 3 and second_area_measurement == 11: #Yard to Are
        Are = int(input("Enter You're Desired Number: "))
        yard_to_Are = 0.008361 * Are

        print("1 Square Yard is equal to " + str(yard_to_Are) + " Are.")

    elif first_area_measurement == 4 and second_area_measurement == 1: #Foot to Mile
        Mile = int(input("Enter You're Desired Number: "))
        Foot_to_Mile = 0.00000003587 * Mile

        print("1 Square Foot is equal to " + str(Foot_to_Mile) + " Mile.")

    elif first_area_measurement == 4 and second_area_measurement == 2: #Foot to Acre
        Acre = int(input("Enter You're Desired Number: "))
        Foot_to_Acre = 0.000022957 * Acre

        print("1 Square Foot is equal to " + str(Foot_to_Acre) + " Acre.")

    elif first_area_measurement == 4 and second_area_measurement == 3: #Foot to Yard
        Yard = int(input("Enter You're Desired Number: "))
        Foot_to_Yard = 0.111111 * Yard

        print("1 Square Foot is equal to " + str(Foot_to_Yard) + " Yard.")

    elif first_area_measurement == 4 and second_area_measurement == 4: #Foot to Foot
        print("Invalid Conversion!!")

    elif first_area_measurement == 4 and second_area_measurement == 5: #Foot to Inch
        Inch = int(input("Enter You're Desired Number: "))
        Foot_to_Inch = 144 * Inch

        print("1 Square Foot is equal to " + str(Foot_to_Inch) + " Inch.")

    elif first_area_measurement == 4 and second_area_measurement == 6: #Foot to Kilometer
        Kilometer = int(input("Enter You're Desired Number: "))
        Foot_to_Kilometer = 0.000000092903 * Kilometer

        print("1 Square Foot is equal to " + str(Foot_to_Kilometer) + " Kilometer.")

    elif first_area_measurement == 4 and second_area_measurement == 7: #Foot to Meter
        Meter = int(input("Enter You're Desired Number: "))
        Foot_to_Meter = 0.092903 * Meter

        print("1 Square Foot is equal to " + str(Foot_to_Meter) + " Meter.")

    elif first_area_measurement == 4 and second_area_measurement == 8: #Foot to Centimeter
        Centimeter = int(input("Enter You're Desired Number: "))
        Foot_to_Centimeter = 929.0304 * Centimeter

        print("1 Square Foot is equal to " + str(Foot_to_Centimeter) + " Centimeter.")

    elif first_area_measurement == 4 and second_area_measurement == 9: #Foot to Milimeter
        Milimeter = int(input("Enter You're Desired Number: "))
        Foot_to_Milimeter = 92903 * Milimeter

        print("1 Square Foot is equal to " + str(Foot_to_Milimeter) + " Milimeter.")

    elif first_area_measurement == 4 and second_area_measurement == 10: #Foot to Hectare
        Hectare = int(input("Enter You're Desired Number: "))
        Foot_to_Hectare = 0.0000092903 * Hectare

        print("1 Square Foot is equal to " + str(Foot_to_Hectare) + " Hectare.")

    elif first_area_measurement == 4 and second_area_measurement == 11: #Foot to Are
        Are = int(input("Enter You're Desired Number: "))
        Foot_to_Are = 0.000929 * Are

        print("1 Square Foot is equal to " + str(Foot_to_Are) + " Are.")

    elif first_area_measurement == 5 and second_area_measurement == 1: #Inch to Mile
        Mile = int(input("Enter You're Desired Number: "))
        Inch_to_Mile = 0.0000000002491 * Mile

        print("1 Square Inch is equal to " + str(Inch_to_Mile) + " Mile.")

    elif first_area_measurement == 5 and second_area_measurement == 2: #Inch to Acre
        Acre = int(input("Enter You're Desired Number: "))
        Inch_to_Acre = 0.00000015942 * Acre

        print("1 Square Inch is equal to " + str(Inch_to_Acre) + " Acre.")

    elif first_area_measurement == 5 and second_area_measurement == 3: #Inch to Yard
        Yard = int(input("Enter You're Desired Number: "))
        Inch_to_Yard = 0.000772 * Yard

        print("1 Square Inch is equal to " + str(Inch_to_Yard) + " Yard.")

    elif first_area_measurement == 5 and second_area_measurement == 4: #Inch to Foot
        Foot = int(input("Enter You're Desired Number: "))
        Inch_to_Foot = 0.006944 * Foot

        print("1 Square Inch is equal to " + str(Inch_to_Foot) + " Foot.")

    elif first_area_measurement == 5 and second_area_measurement == 5: #Inch to Inch
        print("Invalid Conversion!!")

    elif first_area_measurement == 5 and second_area_measurement == 6: #Inch to Kilometer
        Kilometer = int(input("Enter You're Desired Number: "))
        Inch_to_Kilometer = 0.00000000064516 * Kilometer

        print("1 Square Inch is equal to " + str(Inch_to_Kilometer) + " Kilometer.")

    elif first_area_measurement == 5 and second_area_measurement == 7: #Inch to Meter
        Meter = int(input("Enter You're Desired Number: "))
        Inch_to_Meter = 0.000645 * Meter

        print("1 Square Inch is equal to " + str(Inch_to_Meter) + " Meter.")

    elif first_area_measurement == 5 and second_area_measurement == 8: #Inch to Centimeter
        Centimeter = int(input("Enter You're Desired Number: "))
        Inch_to_Centimeter = 6.4516 * Centimeter

        print("1 Square Inch is equal to " + str(Inch_to_Centimeter) + " Centimeter.")

    elif first_area_measurement == 5 and second_area_measurement == 9: #Inch to Milimeter
        Milimeter = int(input("Enter You're Desired Number: "))
        Inch_to_Milimeter = 645.16 * Milimeter

        print("1 Square Inch is equal to " + str(Inch_to_Milimeter) + " Milimeter.")

    elif first_area_measurement == 5 and second_area_measurement == 10: #Inch to Hectare
        Hectare = int(input("Enter You're Desired Number: "))
        Inch_to_Hectare = 0.000000064516 * Hectare

        print("1 Square Inch is equal to " + str(Inch_to_Hectare) + " Hectare.")

    elif first_area_measurement == 5 and second_area_measurement == 11: #Inch to Are
        Are = int(input("Enter You're Desired Number: "))
        Inch_to_Are = 0.0000064516 * Are

        print("1 Square Inch is equal to " + str(Inch_to_Are) + " Are.")

    elif first_area_measurement == 6 and second_area_measurement == 1: #Kilometer to Mile
        Mile = int(input("Enter You're Desired Number: "))
        Kilometer_to_Mile = 0.386102 * Mile

        print("1 Square Kilometer is equal to " + str(Kilometer_to_Mile) + " Mile.")

    elif first_area_measurement == 6 and second_area_measurement == 2: #Kilometer to Acre
        Acre = int(input("Enter You're Desired Number: "))
        Kilometer_to_Acre = 247.105381 * Acre

        print("1 Square Kilometer is equal to " + str(Kilometer_to_Acre) + " Acre.")

    elif first_area_measurement == 6 and second_area_measurement == 3: #Kilometer to Yard
        Yard = int(input("Enter You're Desired Number: "))
        Kilometer_to_Yard = 1195990 * Yard

        print("1 Square Kilometer is equal to " + str(Kilometer_to_Yard) + " Yard.")

    elif first_area_measurement == 6 and second_area_measurement == 4: #Kilometer to Foot
        Foot = int(input("Enter You're Desired Number: "))
        Kilometer_to_Foot = 10763910 * Foot

        print("1 Square Kilometer is equal to " + str(Kilometer_to_Foot) + " Foot.")

    elif first_area_measurement == 6 and second_area_measurement == 5: #Kilometer to Inch
        Inch = int(input("Enter You're Desired Number: "))
        Kilometer_to_Inch = 1550003 * Inch

        print("1 Square Kilometer is equal to " + str(Kilometer_to_Inch) + " Inch.")

    elif first_area_measurement == 6 and second_area_measurement == 6: #Kilometer to Kilometer
        print("Invalid Conversion!!")

    elif first_area_measurement == 6 and second_area_measurement == 7: #Kilometer to Meter
        Meter = int(input("Enter You're Desired Number: "))
        Kilometer_to_Meter = 1000000 * Meter

        print("1 Square Kilometer is equal to " + str(Kilometer_to_Meter) + " Meter.")

    elif first_area_measurement == 6 and second_area_measurement == 8: #Kilometer to Centimeter
        Centimeter = int(input("Enter You're Desired Number: "))
        Kilometer_to_Centimeter = 10000000000 * Centimeter

        print("1 Square Kilometer is equal to " + str(Kilometer_to_Centimeter) + " Centimeter.")

    elif first_area_measurement == 6 and second_area_measurement == 9: #Kilometer to Milimeter
        Milimeter = int(input("Enter You're Desired Number: "))
        Kilometer_to_Milimeter = 1000000000000 * Milimeter

        print("1 Square Kilometer is equal to " + str(Kilometer_to_Milimeter) + " Milimeter.")

    elif first_area_measurement == 6 and second_area_measurement == 10: #Kilometer to Hectare
        Hectare = int(input("Enter You're Desired Number: "))
        Kilometer_to_Hectare = 100 * Hectare

        print("1 Square Kilometer is equal to " + str(Kilometer_to_Hectare) + " Hectare.")

    elif first_area_measurement == 6 and second_area_measurement == 11: #Kilometer to Are
        Are = int(input("Enter You're Desired Number: "))
        Kilometer_to_Are = 10000 * Are

        print("1 Square Kilometer is equal to " + str(Kilometer_to_Are) + " Are.")

    elif first_area_measurement == 7 and second_area_measurement == 1: #Meter to Mile
        Mile = int(input("Enter You're Desired Number: "))
        Meter_to_Mile = 0.0000003861 * Mile

        print("1 Square Meter is equal to " + str(Meter_to_Mile) + " Mile.")

    elif first_area_measurement == 7 and second_area_measurement == 2: #Meter to Acre
        Acre = int(input("Enter You're Desired Number: "))
        Meter_to_Acre = 0.000247 * Acre

        print("1 Square Meter is equal to " + str(Meter_to_Acre) + " Acre.")

    elif first_area_measurement == 7 and second_area_measurement == 3: #Meter to Yard
        Yard = int(input("Enter You're Desired Number: "))
        Meter_to_Yard = 1.19599 * Yard

        print("1 Square Meter is equal to " + str(Meter_to_Yard) + " Yard.")

    elif first_area_measurement == 7 and second_area_measurement == 4: #Meter to Foot
        Foot = int(input("Enter You're Desired Number: "))
        Meter_to_Foot = 10.74391 * Foot

        print("1 Square Meter is equal to " + str(Meter_to_Foot) + " Foot.")

    elif first_area_measurement == 7 and second_area_measurement == 5: #Meter to Inch
        Inch = int(input("Enter You're Desired Number: "))
        Meter_to_Inch = 1550 * Inch

        print("1 Square Meter is equal to " + str(Meter_to_Inch) + " Inch.")

    elif first_area_measurement == 7 and second_area_measurement == 6: #Meter to Kilometer
        Kilometer = int(input("Enter You're Desired Number: "))
        Meter_to_Kilometer = 0.000001 * Kilometer

        print("1 Square Meter is equal to " + str(Meter_to_Kilometer) + " Kilometer.")

    elif first_area_measurement == 7 and second_area_measurement == 7: #Meter to Meter
        print("Invalid Conversion!!")

    elif first_area_measurement == 7 and second_area_measurement == 8: #Meter to Centimeter
        Centimeter = int(input("Enter You're Desired Number: "))
        Meter_to_Centimeter = 10000 * Centimeter

        print("1 Square Meter is equal to " + str(Meter_to_Centimeter) + " Centimeter.")

    elif first_area_measurement == 7 and second_area_measurement == 9: #Meter to Milimeter
        Milimeter = int(input("Enter You're Desired Number: "))
        Meter_to_Milimeter = 1000000 * Milimeter

        print("1 Square Meter is equal to " + str(Meter_to_Milimeter) + " Milimeter.")

    elif first_area_measurement == 7 and second_area_measurement == 10: #Meter to Hectare
        Hectare = int(input("Enter You're Desired Number: "))
        Meter_to_Hectare = 0.0001 * Hectare

        print("1 Square Meter is equal to " + str(Meter_to_Hectare) + " Hectare.")

    elif first_area_measurement == 7 and second_area_measurement == 11: #Meter to Are
        Are = int(input("Enter You're Desired Number: "))
        Meter_to_Are = 0.01 * Are

        print("1 Square Meter is equal to " + str(Meter_to_Are) + " Are.")

    elif first_area_measurement == 8 and second_area_measurement == 1: #Centimeter to Mile
        Mile = int(input("Enter You're Desired Number: "))
        Centimeter_to_Mile = 0.00000000003861 * Mile

        print("1 Square Centimeter is equal to " + str(Centimeter_to_Mile) + " Mile.")

    elif first_area_measurement == 8 and second_area_measurement == 2: #Centimeter to Acre
        Acre = int(input("Enter You're Desired Number: "))
        Centimeter_to_Acre = 0.000000024711 * Acre

        print("1 Square Centimeter is equal to " + str(Centimeter_to_Acre) + " Acre.")

    elif first_area_measurement == 8 and second_area_measurement == 3: #Centimeter to Yard
        Yard = int(input("Enter You're Desired Number: "))
        Centimeter_to_Yard = 0.00012 * Yard

        print("1 Square Centimeter is equal to " + str(Centimeter_to_Yard) + " Yard.")

    elif first_area_measurement == 8 and second_area_measurement == 4: #Centimeter to Foot
        Foot = int(input("Enter You're Desired Number: "))
        Centimeter_to_Foot = 0.001076 * Foot

        print("1 Square Centimeter is equal to " + str(Centimeter_to_Foot) + " Foot.")

    elif first_area_measurement == 8 and second_area_measurement == 5: #Centimeter to Inch
        Inch = int(input("Enter You're Desired Number: "))
        Centimeter_to_Inch = 0.155 * Inch

        print("1 Square Centimeter is equal to " + str(Centimeter_to_Inch) + " Inch.")

    elif first_area_measurement == 8 and second_area_measurement == 6: #Centimeter to Kilometer
        Kilometer = int(input("Enter You're Desired Number: "))
        Centimeter_to_Kilometer = 0.0000000001 * Kilometer

        print("1 Square Centimeter is equal to " + str(Centimeter_to_Kilometer) + " Kilometer.")

    elif first_area_measurement == 8 and second_area_measurement == 7: #Centimeter to Meter
        Meter = int(input("Enter You're Desired Number: "))
        Centimeter_to_Meter = 0.0001 * Meter

        print("1 Square Centimeter is equal to " + str(Centimeter_to_Meter) + " Meter.")

    elif first_area_measurement == 8 and second_area_measurement == 8: #Centimeter to Centimeter
        print("Invalid Conversion!!")

    elif first_area_measurement == 8 and second_area_measurement == 9: #Centimeter to Milimeter
        Milimeter = int(input("Enter You're Desired Number: "))
        Centimeter_to_Milimeter = 100 * Milimeter

        print("1 Square Centimeter is equal to " + str(Centimeter_to_Milimeter) + " Milimeter.")

    elif first_area_measurement == 8 and second_area_measurement == 10: #Centimeter to Hectare
        Hectare = int(input("Enter You're Desired Number: "))
        Centimeter_to_Hectare = 0.00000001 * Hectare

        print("1 Square Centimeter is equal to " + str(Centimeter_to_Hectare) + " Hectare.")

    elif first_area_measurement == 8 and second_area_measurement == 11: #Centimeter to Are
        Are = int(input("Enter You're Desired Number: "))
        Centimeter_to_Are = 0.000001 * Are

        print("1 Square Centimeter is equal to " + str(Centimeter_to_Are) + " Are.")

    elif first_area_measurement == 9 and second_area_measurement == 1: #Milimeter to Mile
        Mile = int(input("Enter You're Desired Number: "))
        Milimeter_to_Mile = 0.0000000000003861 * Mile

        print("1 Square Milimeter is equal to " + str(Milimeter_to_Mile) + " Mile.")

    elif first_area_measurement == 9 and second_area_measurement == 2: #Milimeter to Acre
        Acre = int(input("Enter You're Desired Number: "))
        Milimeter_to_Acre = 0.00000000024711 * Acre

        print("1 Square Milimeter is equal to " + str(Milimeter_to_Acre) + " Acre.")

    elif first_area_measurement == 9 and second_area_measurement == 3: #Milimeter to Yard
        Yard = int(input("Enter You're Desired Number: "))
        Milimeter_to_Yard = 0.000001196 * Yard

        print("1 Square Milimeter is equal to " + str(Milimeter_to_Yard) + " Yard.")

    elif first_area_measurement == 9 and second_area_measurement == 4: #Milimeter to Foot
        Foot = int(input("Enter You're Desired Number: "))
        Milimeter_to_Foot = 0.000010764 * Foot

        print("1 Square Milimeter is equal to " + str(Milimeter_to_Foot) + " Foot.")

    elif first_area_measurement == 9 and second_area_measurement == 5: #Milimeter to Inch
        Inch = int(input("Enter You're Desired Number: "))
        Milimeter_to_Inch = 0.00155 * Inch

        print("1 Square Milimeter is equal to " + str(Milimeter_to_Inch) + " Inch.")

    elif first_area_measurement == 9 and second_area_measurement == 6: #Milimeter to Kilometer
        Kilometer = int(input("Enter You're Desired Number: "))
        Milimeter_to_Kilometer = 0.000000000001 * Kilometer

        print("1 Square Milimeter is equal to " + str(Milimeter_to_Kilometer) + " Kilometer.")

    elif first_area_measurement == 9 and second_area_measurement == 7: #Milimeter to Meter
        Meter = int(input("Enter You're Desired Number: "))
        Milimeter_to_Meter = 0.000001 * Meter

        print("1 Square Milimeter is equal to " + str(Milimeter_to_Meter) + " Meter.")

    elif first_area_measurement == 9 and second_area_measurement == 8: #Milimeter to Centimeter
        Centimeter = int(input("Enter You're Desired Number: "))
        Milimeter_to_Centimeter = 0.01 * Centimeter

        print("1 Square Milimeter is equal to " + str(Milimeter_to_Centimeter) + " Centimeter.")

    elif first_area_measurement == 9 and second_area_measurement == 9: #Milimeter to Milimeter
        print("Invalid Conversion!!")

    elif first_area_measurement == 9 and second_area_measurement == 10: #Milimeter to Hectare
        Hectare = int(input("Enter You're Desired Number: "))
        Milimeter_to_Hectare = 0.0000000001 * Hectare

        print("1 Square Milimeter is equal to " + str(Milimeter_to_Hectare) + " Hectare.")

    elif first_area_measurement == 9 and second_area_measurement == 11: #Milimeter to Are
        Are = int(input("Enter You're Desired Number: "))
        Milimeter_to_Are = 0.00000001 * Are

        print("1 Square Milimeter is equal to " + str(Milimeter_to_Are) + " Are.")

    elif first_area_measurement == 10 and second_area_measurement == 1: #Hectare to Mile
        Mile = int(input("Enter You're Desired Number: "))
        Hectare_to_Mile = 0.003861 * Mile

        print("1 Square Hectare is equal to " + str(Hectare_to_Mile) + " Mile.")

    elif first_area_measurement == 10 and second_area_measurement == 2: #Hectare to Acre
        Acre = int(input("Enter You're Desired Number: "))
        Hectare_to_Acre = 2.471054 * Acre

        print("1 Square Hectare is equal to " + str(Hectare_to_Acre) + " Acre.")

    elif first_area_measurement == 10 and second_area_measurement == 3: #Hectare to Yard
        Yard = int(input("Enter You're Desired Number: "))
        Hectare_to_Yard = 11960 * Yard

        print("1 Square Hectare is equal to " + str(Hectare_to_Yard) + " Yard.")

    elif first_area_measurement == 10 and second_area_measurement == 4: #Hectare to Foot
        Foot = int(input("Enter You're Desired Number: "))
        Hectare_to_Foot = 107639 * Foot

        print("1 Square Hectare is equal to " + str(Hectare_to_Foot) + " Foot.")

    elif first_area_measurement == 10 and second_area_measurement == 5: #Hectare to Inch
        Inch = int(input("Enter You're Desired Number: "))
        Hectare_to_Inch = 15500031 * Inch

        print("1 Square Hectare is equal to " + str(Hectare_to_Inch) + " Inch.")

    elif first_area_measurement == 10 and second_area_measurement == 6: #Hectare to Kilometer
        Kilometer = int(input("Enter You're Desired Number: "))
        Hectare_to_Kilometer = 0.01 * Kilometer

        print("1 Square Hectare is equal to " + str(Hectare_to_Kilometer) + " Kilometer.")

    elif first_area_measurement == 10 and second_area_measurement == 7: #Hectare to Meter
        Meter = int(input("Enter You're Desired Number: "))
        Hectare_to_Meter = 10000 * Meter

        print("1 Square Hectare is equal to " + str(Hectare_to_Meter) + " Meter.")

    elif first_area_measurement == 10 and second_area_measurement == 8: #Hectare to Centimeter
        Centimeter = int(input("Enter You're Desired Number: "))
        Hectare_to_Centimeter = 100000000 * Centimeter

        print("1 Square Hectare is equal to " + str(Hectare_to_Centimeter) + " Centimeter.")

    elif first_area_measurement == 10 and second_area_measurement == 9: #Hectare to Milimeter
        Milimeter = int(input("Enter You're Desired Number: "))
        Hectare_to_Milimeter = 10000000000 * Milimeter

        print("1 Square Hectare is equal to " + str(Hectare_to_Milimeter) + " Milimeter.")

    elif first_area_measurement == 10 and second_area_measurement == 10: #Hectare to Hectare
        print("Invalid Conversion!!")

    elif first_area_measurement == 10 and second_area_measurement == 11: #Hectare to Are
        Are = int(input("Enter You're Desired Number: "))
        Hectare_to_Are = 100 * Are

        print("1 Square Hectare is equal to " + str(Hectare_to_Are) + " Are.")

    elif first_area_measurement == 11 and second_area_measurement == 1: #Are to Mile
        Mile = int(input("Enter You're Desired Number: "))
        Are_to_Mile = 0.00003861 * Mile

        print("1 Square Are is equal to " + str(Are_to_Mile) + " Mile.")

    elif first_area_measurement == 11 and second_area_measurement == 2: #Are to Acre
        Acre = int(input("Enter You're Desired Number: "))
        Are_to_Acre = 0.024711 * Acre

        print("1 Square Are is equal to " + str(Are_to_Acre) + " Acre.")

    elif first_area_measurement == 11 and second_area_measurement == 3: #Are to Yard
        Yard = int(input("Enter You're Desired Number: "))
        Are_to_Yard = 119.599005 * Yard

        print("1 Square Are is equal to " + str(Are_to_Yard) + " Yard.")

    elif first_area_measurement == 11 and second_area_measurement == 4: #Are to Foot
        Foot = int(input("Enter You're Desired Number: "))
        Are_to_Foot = 1076 * Foot

        print("1 Square Are is equal to " + str(Are_to_Foot) + " Foot.")

    elif first_area_measurement == 11 and second_area_measurement == 5: #Are to Inch
        Inch = int(input("Enter You're Desired Number: "))
        Are_to_Inch = 155000 * Inch

        print("1 Square Are is equal to " + str(Are_to_Inch) + " Inch.")

    elif first_area_measurement == 11 and second_area_measurement == 6: #Are to Kilometer
        Kilometer = int(input("Enter You're Desired Number: "))
        Are_to_Kilometer = 0.0001 * Kilometer

        print("1 Square Are is equal to " + str(Are_to_Kilometer) + " Kilometer.")

    elif first_area_measurement == 11 and second_area_measurement == 7: #Are to Meter
        Meter = int(input("Enter You're Desired Number: "))
        Are_to_Meter = 100 * Meter

        print("1 Square Are is equal to " + str(Are_to_Meter) + " Meter.")

    elif first_area_measurement == 11 and second_area_measurement == 8: #Are to Centimeter
        Centimeter = int(input("Enter You're Desired Number: "))
        Are_to_Centimeter = 1000000 * Centimeter

        print("1 Square Are is equal to " + str(Are_to_Centimeter) + " Centimeter.")

    elif first_area_measurement == 11 and second_area_measurement == 9: #Are to Milimeter
        Milimeter = int(input("Enter You're Desired Number: "))
        Are_to_Milimeter = 100000000 * Milimeter

        print("1 Square Are is equal to " + str(Are_to_Milimeter) + " Milimeter.")

    elif first_area_measurement == 11 and second_area_measurement == 10: #Are to Hectare
        Hectare = int(input("Enter You're Desired Number: "))
        Are_to_Hectare = 0.01 * Hectare

        print("1 Square Are is equal to " + str(Are_to_Hectare) + " Hectare.")

    elif first_area_measurement == 11 and second_area_measurement == 11: #Are to Hectare
        print("Invalid Conversion!!")

while True: #Main Menu
    Print_Main_Menu()
    menu = input("-Waiting for You're Desire: ")
    print("\n\n")

    if menu == "1": #Basic Menu
        while True: #Basic Menu
            Print_Basic_Menu()
            basic_menu = input("-Waiting for You're Desire: ")
            print("\n\n")

            if basic_menu == "1": #Numerical Expression             
                Expression()
                while True:
                    Inner_Print()
                    exp_menu = input("-Waiting for You're Desire: ")
                    
                    if exp_menu == "1": #Continue
                        Expression()
                    
                    elif exp_menu == "-": #Back
                        break

                    elif exp_menu == "q" or exp_menu == "Q": #Exit
                        sys.exit(1)
                    
                    else:
                        print("Invalid option!\nEnter again: ")
                        continue
            
            elif basic_menu == "2": #Sum             
                Sum()
                while True:
                    Inner_Print()
                    sum_menu = input("-Waiting for You're Desire: ")
                    
                    if sum_menu == "1": #Continue
                        Sum()
                    
                    elif sum_menu == "-": #Back
                        break

                    elif sum_menu == "q" or sum_menu == "Q": #Exit
                        sys.exit(1)
                    
                    else:
                        print("Invalid option!\nEnter again: ")
                        continue

            elif basic_menu == "3": #Subtraction
                Subtract()
                while True:
                    Inner_Print()
                    sub_menu = input("-Waiting for You're Desire: ")
                    
                    if sub_menu == "1": #Continue
                        Subtract()
                    
                    elif sub_menu == "-": #Back
                        break

                    elif sub_menu == "q" or sub_menu == "Q": #Exit
                        sys.exit(1)
                    
                    else:
                        print("Invalid option!\nEnter again: ")
                        continue
                
            elif basic_menu == "4": #Multiplication             
                Multiplication()
                while True:
                    Inner_Print()
                    Multiply_menu = input("-Waiting for You're Desire: ")
                        
                    if Multiply_menu == "1": #Continue
                        Multiplication()
                        
                    elif Multiply_menu == "-": #Back
                        break

                    elif Multiply_menu == "q" or Multiply_menu == "Q": #Exit
                        sys.exit(1)
                        
                    else:
                        print("Invalid option!\nEnter again: ")
                        continue
                
            elif basic_menu == "5": #Division             
                    Division()
                    while True:
                        Inner_Print()
                        div_menu = input("-Waiting for You're Desire: ")
                        
                        if div_menu == "1": #Continue
                            Division()
                        
                        elif div_menu == "-": #Back
                            break

                        elif div_menu == "q" or div_menu == "Q": #Exit
                            sys.exit(1)
                        
                        else:
                            print("Invalid option!\nEnter again: ")
                        continue
            
            elif basic_menu == "6": #Remainder             
                    Remainder()
                    while True:
                        Inner_Print()
                        remain_menu = input("-Waiting for You're Desire: ")
                        
                        if remain_menu == "1": #Continue
                            Remainder()
                        
                        elif remain_menu == "-": #Back
                            break

                        elif remain_menu == "q" or remain_menu == "Q": #Exit
                            sys.exit(1)
                        
                        else:
                            print("Invalid option!\nEnter again: ")
                        continue

            elif basic_menu == "7": #Percentage             
                    Percentage()
                    while True:
                        Inner_Print()
                        percent_menu = input("-Waiting for You're Desire: ")
                        
                        if percent_menu == "1": #Continue
                            Percentage()
                        
                        elif percent_menu == "-": #Back
                            break

                        elif percent_menu == "q" or percent_menu == "Q": #Exit
                            sys.exit(1)
                        
                        else:
                            print("Invalid option!\nEnter again: ")
                        continue

            elif basic_menu == "-": #Back
                break

            elif basic_menu == "q" or basic_menu == "Q": #Exit
                sys.exit(1)

            else: #Invalid
                print("Invalid option!\nEnter again: ")
                continue

    elif menu == "2": #Advanced Menu
        while True:
            Print_Advanced_Menu()
            advanced_menu = input("-Waiting for You're Desire: ")
            print("\n\n")

            if advanced_menu == "1": #Trigonometry Menu
                while True:
                    Print_Trigonometry_Menu()
                    trigonometry_menu = input("-Waiting for You're Desire: ")
                        
                    if trigonometry_menu == "1": #Sin
                        Sin()
                        while True:
                            Inner_Print()
                            sin_menu = input("-Waiting for You're Desire: ")
                            
                            if sin_menu == "1": #Continue
                                Sin()
                            
                            elif sin_menu == "-": #Back
                                break

                            elif sin_menu == "q" or sin_menu == "Q": #Exit
                                sys.exit(1)
                            
                            else:
                                print("Invalid option!\nEnter again: ")
                                continue

                    elif trigonometry_menu == "2": #Cos
                        Cos()
                        while True:
                            Inner_Print()
                            cos_menu = input("-Waiting for You're Desire: ")
                            
                            if cos_menu == "1": #Continue
                                Cos()
                            
                            elif cos_menu == "-": #Back
                                break

                            elif cos_menu == "q" or cos_menu == "Q": #Exit
                                sys.exit(1)
                            
                            else:
                                print("Invalid option!\nEnter again: ")
                                continue
                        
                    elif trigonometry_menu == "3": #Tan
                        Tan()
                        while True:
                            Inner_Print()
                            tan_menu = input("-Waiting for You're Desire: ")
                            
                            if tan_menu == "1": #Continue
                                Tan()
                            
                            elif tan_menu == "-": #Back
                                break

                            elif tan_menu == "q" or tan_menu == "Q": #Exit
                                sys.exit(1)
                            
                            else:
                                print("Invalid option!\nEnter again: ")
                                continue

                    elif trigonometry_menu == "4": #Cot
                        Cot()
                        while True:
                            Inner_Print()
                            cot_menu = input("-Waiting for You're Desire: ")
                            
                            if cot_menu == "1": #Continue
                                Cot()
                            
                            elif cot_menu == "-": #Back
                                break

                            elif cot_menu == "q" or cot_menu == "Q": #Exit
                                sys.exit(1)
                            
                            else:
                                print("Invalid option!\nEnter again: ")
                                continue
                    
                    elif trigonometry_menu == "5": #ArcSin
                        ArcSin()
                        while True:
                            Inner_Print()
                            arcsin_menu = input("-Waiting for You're Desire: ")
                            
                            if arcsin_menu == "1": #Continue
                                ArcSin()
                            
                            elif arcsin_menu == "-": #Back
                                break

                            elif arcsin_menu == "q" or arcsin_menu == "Q": #Exit
                                sys.exit(1)
                            
                            else:
                                print("Invalid option!\nEnter again: ")
                                continue
                    
                    elif trigonometry_menu == "6": #ArcCos
                        ArcCos()
                        while True:
                            Inner_Print()
                            arccos_menu = input("-Waiting for You're Desire: ")
                            
                            if arccos_menu == "1": #Continue
                                ArcCos()
                            
                            elif arccos_menu == "-": #Back
                                break

                            elif arccos_menu == "q" or arccos_menu == "Q": #Exit
                                sys.exit(1)
                            
                            else:
                                print("Invalid option!\nEnter again: ")
                                continue
                    
                    elif trigonometry_menu == "7": #ArcTan
                        ArcTan()
                        while True:
                            Inner_Print()
                            arctan_menu = input("-Waiting for You're Desire: ")
                            
                            if arctan_menu == "1": #Continue
                                ArcTan()
                            
                            elif arctan_menu == "-": #Back
                                break

                            elif arctan_menu == "q" or arctan_menu == "Q": #Exit
                                sys.exit(1)
                            
                            else:
                                print("Invalid option!\nEnter again: ")
                                continue

                    elif trigonometry_menu == "-": #Back
                        break
                    
                    elif trigonometry_menu == "q" or trigonometry_menu == "Q": #Exit
                        sys.exit(1)

                    else:
                        print("Invalid Option!\nPlease Choose Again.")
                        continue
            
            elif advanced_menu == "2": #Other Operations Menu
                while True:
                    Print_Other_Operations()
                    other_menu = input("-Waiting for You're Desire: ")
                        
                    if other_menu == "1": #Sqrt
                        Square_Root()
                        while True:
                            Inner_Print()
                            sqrt_menu = input("-Waiting for You're Desire: ")
                            
                            if sqrt_menu == "1": #Continue
                                Square_Root()
                            
                            elif sqrt_menu == "-": #Back
                                break

                            elif sqrt_menu == "q" or sqrt_menu == "Q": #Exit
                                sys.exit(1)
                            
                            else:
                                print("Invalid option!\nEnter again: ")
                                continue

                    elif other_menu == "2": #Power
                        Power()
                        while True:
                            Inner_Print()
                            power_menu = input("-Waiting for You're Desire: ")
                            
                            if power_menu == "1": #Continue
                                Power()
                            
                            elif power_menu == "-": #Back
                                break

                            elif power_menu == "q" or power_menu == "Q": #Exit
                                sys.exit(1)
                            
                            else:
                                print("Invalid option!\nEnter again: ")
                                continue

                    elif other_menu == "3": #Factorial
                        Factorial()
                        while True:
                            Inner_Print()
                            fact_menu = input("-Waiting for You're Desire: ")
                            
                            if fact_menu == "1": #Continue
                                Factorial()
                            
                            elif fact_menu == "-": #Back
                                break

                            elif fact_menu == "q" or fact_menu == "Q": #Exit
                                sys.exit(1)
                            
                            else:
                                print("Invalid option!\nEnter again: ")
                                continue

                    elif other_menu == "4": #Log
                        Log()
                        while True:
                            Inner_Print()
                            log_menu = input("-Waiting for You're Desire: ")
                            
                            if log_menu == "1": #Continue
                                Log()
                            
                            elif log_menu == "-": #Back
                                break

                            elif log_menu == "q" or log_menu == "Q": #Exit
                                sys.exit(1)
                            
                            else:
                                print("Invalid option!\nEnter again: ")
                                continue

                    elif other_menu == "-": #Back
                                break

                    elif other_menu == "q" or other_menu == "Q": #Exit
                        sys.exit(1)
                    
                    else: #Invalid
                        print("Invalid option!\nEnter again: ")
                        continue
            
            elif advanced_menu == "3": #Conversions Menu
                while True:
                    Print_Conversions_Menu()
                    conversion_menu = input("-Waiting for You're Desire: ")
                    print("\n\n")
                        
                    if conversion_menu == "1": #Area
                        Area_Conversion()
                        while True:
                            Inner_Print()
                            area_menu = input("-Waiting for You're Desire: ")
                            
                            if area_menu == "1": #Continue
                                Area_Conversion()
                            
                            elif area_menu == "-": #Back
                                break

                            elif area_menu == "q" or area_menu == "Q": #Exit
                                sys.exit(1)
                            
                            else:
                                print("Invalid option!\nEnter again: ")
                                continue
                            
                    elif conversion_menu == "-": #Back
                        break

                    elif conversion_menu == "q" or conversion_menu == "Q": #Exit
                        sys.exit(1)
                    
                    else: #Invalid
                        print("Invalid Option!\nPlease Choose Again.")
                        continue
                    
            elif advanced_menu == "-": #Back
                break

            elif advanced_menu == "q" or advanced_menu == "Q": #Exit
                sys.exit(1)

            else: #Invalid
                print("Invalid Option!\nPlease Choose Again.")
                continue

    elif menu == "q" or menu == "Q": #Exit
        sys.exit(1)
