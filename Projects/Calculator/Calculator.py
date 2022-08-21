
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
    + "\n| 4.Numeral System." + 5 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 5.Temperature." + 8 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| - Back." + 15 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| Q.Exit." + 15 * " " + "|" + "\n" + "|" + 23 * "_" + "|\n\n")

def Print_Data_Menu():
    print(" " + 4 * "*" + " Area Conversion " + 4 * "*" + "\n " + 23 * "_" + "\n" 
    + "| -Choose an Option: " + 3 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 1.Bits." + 15 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 2.Bytes." + 14 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 3.KiloBytes." + 10 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 4.MegaBytes." + 10 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 5.GigaBytes." + 10 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 6.TeraBytes." + 10 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 7.PetaBytes." + 10 * " " + "|" + "\n" + "|" + 23 * "_" + "|\n\n")

def Print_Numeral_System():
    print("\n " + 4 * "*" + " Numeral System " + 4 * "*" + "\n " + 23 * "_" + "\n" 
    + "| -Choose an Option: " + 3 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 1.Decimal." + 12 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 2.Binary." + 13 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 3.Octal." + 14 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 4.HexaDecimal." + 8 * " " + "|" + "\n" + "|" + 23 * "_" + "|\n\n")

def Print_Temperature_Conversion():
    print("\n " + 3 * "*" + " Temperature Unit " + 3 * "*" + "\n " + 23 * "_" + "\n" 
    + "| -Choose an Option: " + 3 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 1.Celsius." + 12 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 2.Fahrenheit." + 9 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
    + "\n| 3.Kelvin." + 13 * " " + "|" + "\n" + "|" + 23 * "_" + "|\n\n")

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
    number = float(input("Enter You're Desired Number: "))

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
        Mile = float(input("Enter You're Desired Number: "))
        mile_to_acre = 640 * Mile

        print(str(Mile) + " Mile is equal to " + str(mile_to_acre) + " Acre.")
            
    elif first_area_measurement == 1 and second_area_measurement == 3: #Mile to Yard
        Mile = float(input("Enter You're Desired Number: "))
        mile_to_yard = 3097600 * Mile

        print(str(Mile) + " Mile is is equal to " + str(mile_to_yard) + " Yard.")

    elif first_area_measurement == 1 and second_area_measurement == 4: #Mile to Foot
        Mile = float(input("Enter You're Desired Number: "))
        mile_to_foot = 27878400 * Mile

        print(str(Mile) + " Mile is equal to " + str(mile_to_foot) + " Foot.")
            
    elif first_area_measurement == 1 and second_area_measurement == 5: #Mile to Inch
        Mile = float(input("Enter You're Desired Number: "))
        mile_to_inch = 4014489599 * Mile

        print(str(Mile) + " Mile is equal to " + str(mile_to_inch) + " Inch.")
            
    elif first_area_measurement == 1 and second_area_measurement == 6: #Mile to Kilometer
        Mile = float(input("Enter You're Desired Number: "))
        mile_to_kilometer = 2.589988 * Mile

        print(str(Mile) + " Mile is equal to " + str(mile_to_kilometer) + " Kilometer.")   

    elif first_area_measurement == 1 and second_area_measurement == 7: #Mile to Meter
        Mile = float(input("Enter You're Desired Number: "))
        mile_to_meter = 2589988 * Mile

        print(str(Mile) + " Mile is equal to " + str(mile_to_meter) + " Meter.")
            
    elif first_area_measurement == 1 and second_area_measurement == 8: #Mile to Centimeter
        Mile = float(input("Enter You're Desired Number: "))
        mile_to_centimeter = 25899881100 * Mile

        print(str(Mile) + " Mile is equal to " + str(mile_to_centimeter) + " Centimeter.")

    elif first_area_measurement == 1 and second_area_measurement == 9: #Mile to Milimeter
        Mile = float(input("Enter You're Desired Number: "))
        mile_to_milimeter = 2589988110000 * Mile

        print(str(Mile) + " Mile is equal to " + str(mile_to_milimeter) + " Milimeter.")

    elif first_area_measurement == 1 and second_area_measurement == 10: #Mile to Hectare
        Mile = float(input("Enter You're Desired Number: "))
        mile_to_hectare = 258.998811 * Mile

        print(str(Mile) + " Mile is equal to " + str(mile_to_hectare) + " Hectare.")

    elif first_area_measurement == 1 and second_area_measurement == 11: #Mile to Are
        Mile = float(input("Enter You're Desired Number: "))
        mile_to_are = 25900 * Mile

        print(str(Mile) + " Mile is equal to " + str(mile_to_are) + " Are.")

    elif first_area_measurement == 2 and second_area_measurement == 1: #Acre to Mile
        Acre = float(input("Enter You're Desired Number: "))
        acre_to_mile = 0.001563 * Acre

        print(str(Acre) + " Acre is equal to " + str(acre_to_mile) + " Mile.")

    elif first_area_measurement == 2 and second_area_measurement == 2: #Acre to Acre
        print("Invalid Conversion!!")

    elif first_area_measurement == 2 and second_area_measurement == 3: #Acre to Yard
        Acre = float(input("Enter You're Desired Number: "))
        acre_to_yard = 4840 * Acre

        print(str(Acre) + " Acre is equal to " + str(acre_to_yard) + " Yard.")

    elif first_area_measurement == 2 and second_area_measurement == 4: #Acre to Foot
        Acre = float(input("Enter You're Desired Number: "))
        acre_to_foot = 43560 * Acre

        print(str(Acre) + " Acre is equal to " + str(acre_to_foot) + " Foot.")

    elif first_area_measurement == 2 and second_area_measurement == 5: #Acre to Inch
        Acre = float(input("Enter You're Desired Number: "))
        acre_to_inch = 6272640 * Acre

        print(str(Acre) + " Acre is equal to " + str(acre_to_inch) + " Inch.")

    elif first_area_measurement == 2 and second_area_measurement == 6: #Acre to Kilometer
        Acre = float(input("Enter You're Desired Number: "))
        acre_to_kilometer = 0.004047 * Acre

        print(str(Acre) + " Acre is equal to " + str(acre_to_kilometer) + " Kilometer.")

    elif first_area_measurement == 2 and second_area_measurement == 7: #Acre to Meter
        Acre = float(input("Enter You're Desired Number: "))
        acre_to_meter = 4047 * Acre

        print(str(Acre) + " Acre is equal to " + str(acre_to_meter) + " Meter.")

    elif first_area_measurement == 2 and second_area_measurement == 8: #Acre to Centimeter
        Acre = float(input("Enter You're Desired Number: "))
        acre_to_centimeter = 40468564 * Acre

        print(str(Acre) + " Acre is equal to " + str(acre_to_centimeter) + " Centimeter.")

    elif first_area_measurement == 2 and second_area_measurement == 9: #Acre to Milimeter
        Acre = float(input("Enter You're Desired Number: "))
        acre_to_milimeter = 4046856422 * Acre

        print(str(Acre) + " Acre is equal to " + str(acre_to_milimeter) + " Milimeter.")

    elif first_area_measurement == 2 and second_area_measurement == 10: #Acre to Hectare
        Acre = float(input("Enter You're Desired Number: "))
        acre_to_hectare = 0.404686 * Acre

        print(str(Acre) + " Acre is equal to " + str(acre_to_hectare) + " Hectare.")

    elif first_area_measurement == 2 and second_area_measurement == 11: #Acre to Are
        Acre = float(input("Enter You're Desired Number: "))
        acre_to_are = 40.468564 * Acre

        print(str(Acre) + " Acre is equal to " + str(acre_to_are) + " Are.")

    elif first_area_measurement == 3 and second_area_measurement == 1: #Yard to Mile
        Yard = float(input("Enter You're Desired Number: "))
        yard_to_mile = 0.00000032283 * Yard

        print(str(Yard) + " Yard is equal to " + str(yard_to_mile) + " Mile.")

    elif first_area_measurement == 3 and second_area_measurement == 2: #Yard to Acre
        Yard = float(input("Enter You're Desired Number: "))
        yard_to_acre = 0.000207 * Yard

        print(str(Yard) + " Yard is equal to " + str(yard_to_acre) + " Acre.")

    elif first_area_measurement == 3 and second_area_measurement == 3: #Yard to Yard
        print("Invalid Conversion!!")

    elif first_area_measurement == 3 and second_area_measurement == 4: #Yard to Foot
        Yard = float(input("Enter You're Desired Number: "))
        yard_to_Foot = 9 * Yard

        print(str(Yard) + " Yard is equal to " + str(yard_to_Foot) + " Foot.")

    elif first_area_measurement == 3 and second_area_measurement == 5: #Yard to Inch
        Yard = float(input("Enter You're Desired Number: "))
        yard_to_Inch = 1296 * Yard

        print(str(Yard) + " Yard is equal to " + str(yard_to_Inch) + " Inch.")

    elif first_area_measurement == 3 and second_area_measurement == 6: #Yard to Kilometer
        Yard = float(input("Enter You're Desired Number: "))
        yard_to_Kilometer = 0.00000083613 * Yard

        print(str(Yard) + " Yard is equal to " + str(yard_to_Kilometer) + " Kilometer.")

    elif first_area_measurement == 3 and second_area_measurement == 7: #Yard to Meter
        Yard = float(input("Enter You're Desired Number: "))
        yard_to_Meter = 0.836127 * Yard

        print(str(Yard) + " Yard is equal to " + str(yard_to_Meter) + " Meter.")

    elif first_area_measurement == 3 and second_area_measurement == 8: #Yard to Centimeter
        Yard = float(input("Enter You're Desired Number: "))
        yard_to_Centimeter = 8361 * Yard

        print(str(Yard) + " Yard is equal to " + str(yard_to_Centimeter) + " Centimeter.")

    elif first_area_measurement == 3 and second_area_measurement == 9: #Yard to Milimeter
        Yard = float(input("Enter You're Desired Number: "))
        yard_to_Milimeter = 836127 * Yard

        print(str(Yard) + " Yard is equal to " + str(yard_to_Milimeter) + " Milimeter.")

    elif first_area_measurement == 3 and second_area_measurement == 10: #Yard to Hectare
        Yard = float(input("Enter You're Desired Number: "))
        yard_to_Hectare = 0.000083613 * Yard

        print(str(Yard) + " Yard is equal to " + str(yard_to_Hectare) + " Hectare.")

    elif first_area_measurement == 3 and second_area_measurement == 11: #Yard to Are
        Yard = float(input("Enter You're Desired Number: "))
        yard_to_Are = 0.008361 * Yard

        print(str(Yard) + " Yard is equal to " + str(yard_to_Are) + " Are.")

    elif first_area_measurement == 4 and second_area_measurement == 1: #Foot to Mile
        Foot = float(input("Enter You're Desired Number: "))
        Foot_to_Mile = 0.00000003587 * Foot

        print(str(Foot) + " Foot is equal to " + str(Foot_to_Mile) + " Mile.")

    elif first_area_measurement == 4 and second_area_measurement == 2: #Foot to Acre
        Foot = float(input("Enter You're Desired Number: "))
        Foot_to_Acre = 0.000022957 * Foot

        print(str(Foot) + " Foot is equal to " + str(Foot_to_Acre) + " Acre.")

    elif first_area_measurement == 4 and second_area_measurement == 3: #Foot to Yard
        Foot = float(input("Enter You're Desired Number: "))
        Foot_to_Yard = 0.111111 * Foot

        print(str(Foot) + " Foot is equal to " + str(Foot_to_Yard) + " Yard.")

    elif first_area_measurement == 4 and second_area_measurement == 4: #Foot to Foot
        print("Invalid Conversion!!")

    elif first_area_measurement == 4 and second_area_measurement == 5: #Foot to Inch
        Foot = float(input("Enter You're Desired Number: "))
        Foot_to_Inch = 144 * Foot

        print(str(Foot) + " Foot is equal to " + str(Foot_to_Inch) + " Inch.")

    elif first_area_measurement == 4 and second_area_measurement == 6: #Foot to Kilometer
        Foot = float(input("Enter You're Desired Number: "))
        Foot_to_Kilometer = 0.000000092903 * Foot

        print(str(Foot) + " Foot is equal to " + str(Foot_to_Kilometer) + " Kilometer.")

    elif first_area_measurement == 4 and second_area_measurement == 7: #Foot to Meter
        Foot = float(input("Enter You're Desired Number: "))
        Foot_to_Meter = 0.092903 * Foot

        print(str(Foot) + " Foot is equal to " + str(Foot_to_Meter) + " Meter.")

    elif first_area_measurement == 4 and second_area_measurement == 8: #Foot to Centimeter
        Foot = float(input("Enter You're Desired Number: "))
        Foot_to_Centimeter = 929.0304 * Foot

        print(str(Foot) + " Foot is equal to " + str(Foot_to_Centimeter) + " Centimeter.")

    elif first_area_measurement == 4 and second_area_measurement == 9: #Foot to Milimeter
        Foot = float(input("Enter You're Desired Number: "))
        Foot_to_Milimeter = 92903 * Foot

        print(str(Foot) + " Foot is equal to " + str(Foot_to_Milimeter) + " Milimeter.")

    elif first_area_measurement == 4 and second_area_measurement == 10: #Foot to Hectare
        Foot = float(input("Enter You're Desired Number: "))
        Foot_to_Hectare = 0.0000092903 * Foot

        print(str(Foot) + " Foot is equal to " + str(Foot_to_Hectare) + " Hectare.")

    elif first_area_measurement == 4 and second_area_measurement == 11: #Foot to Are
        Foot = float(input("Enter You're Desired Number: "))
        Foot_to_Are = 0.000929 * Foot

        print(str(Foot) + " Foot is equal to " + str(Foot_to_Are) + " Are.")

    elif first_area_measurement == 5 and second_area_measurement == 1: #Inch to Mile
        Inch = float(input("Enter You're Desired Number: "))
        Inch_to_Mile = 0.0000000002491 * Inch

        print(str(Inch) + " Inch is equal to " + str(Inch_to_Mile) + " Mile.")

    elif first_area_measurement == 5 and second_area_measurement == 2: #Inch to Acre
        Inch = float(input("Enter You're Desired Number: "))
        Inch_to_Acre = 0.00000015942 * Inch

        print(str(Inch) + " Inch is equal to " + str(Inch_to_Acre) + " Acre.")

    elif first_area_measurement == 5 and second_area_measurement == 3: #Inch to Yard
        Inch = float(input("Enter You're Desired Number: "))
        Inch_to_Yard = 0.000772 * Inch

        print(str(Inch) + " Inch is equal to " + str(Inch_to_Yard) + " Yard.")

    elif first_area_measurement == 5 and second_area_measurement == 4: #Inch to Foot
        Inch = float(input("Enter You're Desired Number: "))
        Inch_to_Foot = 0.006944 * Inch

        print(str(Inch) + " Inch is equal to " + str(Inch_to_Foot) + " Foot.")

    elif first_area_measurement == 5 and second_area_measurement == 5: #Inch to Inch
        print("Invalid Conversion!!")

    elif first_area_measurement == 5 and second_area_measurement == 6: #Inch to Kilometer
        Inch = float(input("Enter You're Desired Number: "))
        Inch_to_Kilometer = 0.00000000064516 * Inch

        print(str(Inch) + " Inch is equal to " + str(Inch_to_Kilometer) + " Kilometer.")

    elif first_area_measurement == 5 and second_area_measurement == 7: #Inch to Meter
        Inch = float(input("Enter You're Desired Number: "))
        Inch_to_Meter = 0.000645 * Inch

        print(str(Inch) + " Inch is equal to " + str(Inch_to_Meter) + " Meter.")

    elif first_area_measurement == 5 and second_area_measurement == 8: #Inch to Centimeter
        Inch = float(input("Enter You're Desired Number: "))
        Inch_to_Centimeter = 6.4516 * Inch

        print(str(Inch) + " Inch is equal to " + str(Inch_to_Centimeter) + " Centimeter.")

    elif first_area_measurement == 5 and second_area_measurement == 9: #Inch to Milimeter
        Inch = float(input("Enter You're Desired Number: "))
        Inch_to_Milimeter = 645.16 * Inch

        print(str(Inch) + " Inch is equal to " + str(Inch_to_Milimeter) + " Milimeter.")

    elif first_area_measurement == 5 and second_area_measurement == 10: #Inch to Hectare
        Inch = float(input("Enter You're Desired Number: "))
        Inch_to_Hectare = 0.000000064516 * Inch

        print(str(Inch) + " Inch is equal to " + str(Inch_to_Hectare) + " Hectare.")

    elif first_area_measurement == 5 and second_area_measurement == 11: #Inch to Are
        Inch = float(input("Enter You're Desired Number: "))
        Inch_to_Are = 0.0000064516 * Inch

        print(str(Inch) + " Inch is equal to " + str(Inch_to_Are) + " Are.")

    elif first_area_measurement == 6 and second_area_measurement == 1: #Kilometer to Mile
        Kilometer = float(input("Enter You're Desired Number: "))
        Kilometer_to_Mile = 0.386102 * Kilometer

        print(str(Kilometer) + " Kilometer is equal to " + str(Kilometer_to_Mile) + " Mile.")

    elif first_area_measurement == 6 and second_area_measurement == 2: #Kilometer to Acre
        Kilometer = float(input("Enter You're Desired Number: "))
        Kilometer_to_Acre = 247.105381 * Kilometer

        print(str(Kilometer) + " Kilometer is equal to " + str(Kilometer_to_Acre) + " Acre.")

    elif first_area_measurement == 6 and second_area_measurement == 3: #Kilometer to Yard
        Kilometer = float(input("Enter You're Desired Number: "))
        Kilometer_to_Yard = 1195990 * Kilometer

        print(str(Kilometer) + " Kilometer is equal to " + str(Kilometer_to_Yard) + " Yard.")

    elif first_area_measurement == 6 and second_area_measurement == 4: #Kilometer to Foot
        Kilometer = float(input("Enter You're Desired Number: "))
        Kilometer_to_Foot = 10763910 * Kilometer

        print(str(Kilometer) + " Kilometer is equal to " + str(Kilometer_to_Foot) + " Foot.")

    elif first_area_measurement == 6 and second_area_measurement == 5: #Kilometer to Inch
        Kilometer = float(input("Enter You're Desired Number: "))
        Kilometer_to_Inch = 1550003 * Kilometer

        print(str(Kilometer) + " Kilometer is equal to " + str(Kilometer_to_Inch) + " Inch.")

    elif first_area_measurement == 6 and second_area_measurement == 6: #Kilometer to Kilometer
        print("Invalid Conversion!!")

    elif first_area_measurement == 6 and second_area_measurement == 7: #Kilometer to Meter
        Kilometer = float(input("Enter You're Desired Number: "))
        Kilometer_to_Meter = 1000000 * Kilometer

        print(str(Kilometer) + " Kilometer is equal to " + str(Kilometer_to_Meter) + " Meter.")

    elif first_area_measurement == 6 and second_area_measurement == 8: #Kilometer to Centimeter
        Kilometer = float(input("Enter You're Desired Number: "))
        Kilometer_to_Centimeter = 10000000000 * Kilometer

        print(str(Kilometer) + " Kilometer is equal to " + str(Kilometer_to_Centimeter) + " Centimeter.")

    elif first_area_measurement == 6 and second_area_measurement == 9: #Kilometer to Milimeter
        Kilometer = float(input("Enter You're Desired Number: "))
        Kilometer_to_Milimeter = 1000000000000 * Kilometer

        print(str(Kilometer) + " Kilometer is equal to " + str(Kilometer_to_Milimeter) + " Milimeter.")

    elif first_area_measurement == 6 and second_area_measurement == 10: #Kilometer to Hectare
        Kilometer = float(input("Enter You're Desired Number: "))
        Kilometer_to_Hectare = 100 * Kilometer

        print(str(Kilometer) + " Kilometer is equal to " + str(Kilometer_to_Hectare) + " Hectare.")

    elif first_area_measurement == 6 and second_area_measurement == 11: #Kilometer to Are
        Kilometer = float(input("Enter You're Desired Number: "))
        Kilometer_to_Are = 10000 * Kilometer

        print(str(Kilometer) + " Kilometer is equal to " + str(Kilometer_to_Are) + " Are.")

    elif first_area_measurement == 7 and second_area_measurement == 1: #Meter to Mile
        Meter = float(input("Enter You're Desired Number: "))
        Meter_to_Mile = 0.0000003861 * Meter

        print(str(Meter) + " Meter is equal to " + str(Meter_to_Mile) + " Mile.")

    elif first_area_measurement == 7 and second_area_measurement == 2: #Meter to Acre
        Meter = float(input("Enter You're Desired Number: "))
        Meter_to_Acre = 0.000247 * Meter

        print(str(Meter) + " Meter is equal to " + str(Meter_to_Acre) + " Acre.")

    elif first_area_measurement == 7 and second_area_measurement == 3: #Meter to Yard
        Meter = float(input("Enter You're Desired Number: "))
        Meter_to_Yard = 1.19599 * Meter

        print(str(Meter) + " Meter is equal to " + str(Meter_to_Yard) + " Yard.")

    elif first_area_measurement == 7 and second_area_measurement == 4: #Meter to Foot
        Meter = float(input("Enter You're Desired Number: "))
        Meter_to_Foot = 10.74391 * Meter

        print(str(Meter) + " Meter is equal to " + str(Meter_to_Foot) + " Foot.")

    elif first_area_measurement == 7 and second_area_measurement == 5: #Meter to Inch
        Meter = float(input("Enter You're Desired Number: "))
        Meter_to_Inch = 1550 * Meter

        print(str(Meter) + " Meter is equal to " + str(Meter_to_Inch) + " Inch.")

    elif first_area_measurement == 7 and second_area_measurement == 6: #Meter to Kilometer
        Meter = float(input("Enter You're Desired Number: "))
        Meter_to_Kilometer = 0.000001 * Meter

        print(str(Meter) + " Meter is equal to " + str(Meter_to_Kilometer) + " Kilometer.")

    elif first_area_measurement == 7 and second_area_measurement == 7: #Meter to Meter
        print("Invalid Conversion!!")

    elif first_area_measurement == 7 and second_area_measurement == 8: #Meter to Centimeter
        Meter = float(input("Enter You're Desired Number: "))
        Meter_to_Centimeter = 10000 * Meter

        print(str(Meter) + " Meter is equal to " + str(Meter_to_Centimeter) + " Centimeter.")

    elif first_area_measurement == 7 and second_area_measurement == 9: #Meter to Milimeter
        Meter = float(input("Enter You're Desired Number: "))
        Meter_to_Milimeter = 1000000 * Meter

        print(str(Meter) + " Meter is equal to " + str(Meter_to_Milimeter) + " Milimeter.")

    elif first_area_measurement == 7 and second_area_measurement == 10: #Meter to Hectare
        Meter = float(input("Enter You're Desired Number: "))
        Meter_to_Hectare = 0.0001 * Meter

        print(str(Meter) + " Meter is equal to " + str(Meter_to_Hectare) + " Hectare.")

    elif first_area_measurement == 7 and second_area_measurement == 11: #Meter to Are
        Meter = float(input("Enter You're Desired Number: "))
        Meter_to_Are = 0.01 * Meter

        print(str(Meter) + " Meter is equal to " + str(Meter_to_Are) + " Are.")

    elif first_area_measurement == 8 and second_area_measurement == 1: #Centimeter to Mile
        Centimeter = float(input("Enter You're Desired Number: "))
        Centimeter_to_Mile = 0.00000000003861 * Centimeter

        print(str(Centimeter) + " Centimeter is equal to " + str(Centimeter_to_Mile) + " Mile.")

    elif first_area_measurement == 8 and second_area_measurement == 2: #Centimeter to Acre
        Centimeter = float(input("Enter You're Desired Number: "))
        Centimeter_to_Acre = 0.000000024711 * Centimeter

        print(str(Centimeter) + " Centimeter is equal to " + str(Centimeter_to_Acre) + " Acre.")

    elif first_area_measurement == 8 and second_area_measurement == 3: #Centimeter to Yard
        Centimeter = float(input("Enter You're Desired Number: "))
        Centimeter_to_Yard = 0.00012 * Centimeter

        print(str(Centimeter) + " Centimeter is equal to " + str(Centimeter_to_Yard) + " Yard.")

    elif first_area_measurement == 8 and second_area_measurement == 4: #Centimeter to Foot
        Centimeter = float(input("Enter You're Desired Number: "))
        Centimeter_to_Foot = 0.001076 * Centimeter

        print(str(Centimeter) + " Centimeter is equal to " + str(Centimeter_to_Foot) + " Foot.")

    elif first_area_measurement == 8 and second_area_measurement == 5: #Centimeter to Inch
        Centimeter = float(input("Enter You're Desired Number: "))
        Centimeter_to_Inch = 0.155 * Centimeter

        print(str(Centimeter) + " Centimeter is equal to " + str(Centimeter_to_Inch) + " Inch.")

    elif first_area_measurement == 8 and second_area_measurement == 6: #Centimeter to Kilometer
        Centimeter = float(input("Enter You're Desired Number: "))
        Centimeter_to_Kilometer = 0.0000000001 * Centimeter

        print(str(Centimeter) + " Centimeter is equal to " + str(Centimeter_to_Kilometer) + " Kilometer.")

    elif first_area_measurement == 8 and second_area_measurement == 7: #Centimeter to Meter
        Centimeter = float(input("Enter You're Desired Number: "))
        Centimeter_to_Meter = 0.0001 * Centimeter

        print(str(Centimeter) + " Centimeter is equal to " + str(Centimeter_to_Meter) + " Meter.")

    elif first_area_measurement == 8 and second_area_measurement == 8: #Centimeter to Centimeter
        print("Invalid Conversion!!")

    elif first_area_measurement == 8 and second_area_measurement == 9: #Centimeter to Milimeter
        Centimeter = float(input("Enter You're Desired Number: "))
        Centimeter_to_Milimeter = 100 * Centimeter

        print(str(Centimeter) + " Centimeter is equal to " + str(Centimeter_to_Milimeter) + " Milimeter.")

    elif first_area_measurement == 8 and second_area_measurement == 10: #Centimeter to Hectare
        Centimeter = float(input("Enter You're Desired Number: "))
        Centimeter_to_Hectare = 0.00000001 * Centimeter

        print(str(Centimeter) + " Centimeter is equal to " + str(Centimeter_to_Hectare) + " Hectare.")

    elif first_area_measurement == 8 and second_area_measurement == 11: #Centimeter to Are
        Centimeter = float(input("Enter You're Desired Number: "))
        Centimeter_to_Are = 0.000001 * Centimeter

        print(str(Centimeter) + " Centimeter is equal to " + str(Centimeter_to_Are) + " Are.")

    elif first_area_measurement == 9 and second_area_measurement == 1: #Milimeter to Mile
        Milimeter = float(input("Enter You're Desired Number: "))
        Milimeter_to_Mile = 0.0000000000003861 * Milimeter

        print(str(Milimeter) + " Milimeter is equal to " + str(Milimeter_to_Mile) + " Mile.")

    elif first_area_measurement == 9 and second_area_measurement == 2: #Milimeter to Acre
        Milimeter = float(input("Enter You're Desired Number: "))
        Milimeter_to_Acre = 0.00000000024711 * Milimeter

        print(str(Milimeter) + " Milimeter is equal to " + str(Milimeter_to_Acre) + " Acre.")

    elif first_area_measurement == 9 and second_area_measurement == 3: #Milimeter to Yard
        Milimeter = float(input("Enter You're Desired Number: "))
        Milimeter_to_Yard = 0.000001196 * Milimeter

        print(str(Milimeter) + " Milimeter is equal to " + str(Milimeter_to_Yard) + " Yard.")

    elif first_area_measurement == 9 and second_area_measurement == 4: #Milimeter to Foot
        Milimeter = float(input("Enter You're Desired Number: "))
        Milimeter_to_Foot = 0.000010764 * Milimeter

        print(str(Milimeter) + " Milimeter is equal to " + str(Milimeter_to_Foot) + " Foot.")

    elif first_area_measurement == 9 and second_area_measurement == 5: #Milimeter to Inch
        Milimeter = float(input("Enter You're Desired Number: "))
        Milimeter_to_Inch = 0.00155 * Milimeter

        print(str(Milimeter) + " Milimeter is equal to " + str(Milimeter_to_Inch) + " Inch.")

    elif first_area_measurement == 9 and second_area_measurement == 6: #Milimeter to Kilometer
        Milimeter = float(input("Enter You're Desired Number: "))
        Milimeter_to_Kilometer = 0.000000000001 * Milimeter

        print(str(Milimeter) + " Milimeter is equal to " + str(Milimeter_to_Kilometer) + " Kilometer.")

    elif first_area_measurement == 9 and second_area_measurement == 7: #Milimeter to Meter
        Milimeter = float(input("Enter You're Desired Number: "))
        Milimeter_to_Meter = 0.000001 * Milimeter

        print(str(Milimeter) + " Milimeter is equal to " + str(Milimeter_to_Meter) + " Meter.")

    elif first_area_measurement == 9 and second_area_measurement == 8: #Milimeter to Centimeter
        Milimeter = float(input("Enter You're Desired Number: "))
        Milimeter_to_Centimeter = 0.01 * Milimeter

        print(str(Milimeter) + " Milimeter is equal to " + str(Milimeter_to_Centimeter) + " Centimeter.")

    elif first_area_measurement == 9 and second_area_measurement == 9: #Milimeter to Milimeter
        print("Invalid Conversion!!")

    elif first_area_measurement == 9 and second_area_measurement == 10: #Milimeter to Hectare
        Milimeter = float(input("Enter You're Desired Number: "))
        Milimeter_to_Hectare = 0.0000000001 * Milimeter

        print(str(Milimeter) + " Milimeter is equal to " + str(Milimeter_to_Hectare) + " Hectare.")

    elif first_area_measurement == 9 and second_area_measurement == 11: #Milimeter to Are
        Milimeter = float(input("Enter You're Desired Number: "))
        Milimeter_to_Are = 0.00000001 * Milimeter

        print(str(Milimeter) + " Milimeter is equal to " + str(Milimeter_to_Are) + " Are.")

    elif first_area_measurement == 10 and second_area_measurement == 1: #Hectare to Mile
        Hectare = float(input("Enter You're Desired Number: "))
        Hectare_to_Mile = 0.003861 * Hectare

        print(str(Hectare) + " Hectare is equal to " + str(Hectare_to_Mile) + " Mile.")

    elif first_area_measurement == 10 and second_area_measurement == 2: #Hectare to Acre
        Hectare = float(input("Enter You're Desired Number: "))
        Hectare_to_Acre = 2.471054 * Hectare

        print(str(Hectare) + " Hectare is equal to " + str(Hectare_to_Acre) + " Acre.")

    elif first_area_measurement == 10 and second_area_measurement == 3: #Hectare to Yard
        Hectare = float(input("Enter You're Desired Number: "))
        Hectare_to_Yard = 11960 * Hectare

        print(str(Hectare) + " Hectare is equal to " + str(Hectare_to_Yard) + " Yard.")

    elif first_area_measurement == 10 and second_area_measurement == 4: #Hectare to Foot
        Hectare = float(input("Enter You're Desired Number: "))
        Hectare_to_Foot = 107639 * Hectare

        print(str(Hectare) + " Hectare is equal to " + str(Hectare_to_Foot) + " Foot.")

    elif first_area_measurement == 10 and second_area_measurement == 5: #Hectare to Inch
        Hectare = float(input("Enter You're Desired Number: "))
        Hectare_to_Inch = 15500031 * Hectare

        print(str(Hectare) + " Hectare is equal to " + str(Hectare_to_Inch) + " Inch.")

    elif first_area_measurement == 10 and second_area_measurement == 6: #Hectare to Kilometer
        Hectare = float(input("Enter You're Desired Number: "))
        Hectare_to_Kilometer = 0.01 * Hectare

        print(str(Hectare) + " Hectare is equal to " + str(Hectare_to_Kilometer) + " Kilometer.")

    elif first_area_measurement == 10 and second_area_measurement == 7: #Hectare to Meter
        Hectare = float(input("Enter You're Desired Number: "))
        Hectare_to_Meter = 10000 * Hectare

        print(str(Hectare) + " Hectare is equal to " + str(Hectare_to_Meter) + " Meter.")

    elif first_area_measurement == 10 and second_area_measurement == 8: #Hectare to Centimeter
        Hectare = float(input("Enter You're Desired Number: "))
        Hectare_to_Centimeter = 100000000 * Hectare

        print(str(Hectare) + " Hectare is equal to " + str(Hectare_to_Centimeter) + " Centimeter.")

    elif first_area_measurement == 10 and second_area_measurement == 9: #Hectare to Milimeter
        Hectare = float(input("Enter You're Desired Number: "))
        Hectare_to_Milimeter = 10000000000 * Hectare

        print(str(Hectare) + " Hectare is equal to " + str(Hectare_to_Milimeter) + " Milimeter.")

    elif first_area_measurement == 10 and second_area_measurement == 10: #Hectare to Hectare
        print("Invalid Conversion!!")

    elif first_area_measurement == 10 and second_area_measurement == 11: #Hectare to Are
        Hectare = float(input("Enter You're Desired Number: "))
        Hectare_to_Are = 100 * Hectare

        print(str(Hectare) + " Hectare is equal to " + str(Hectare_to_Are) + " Are.")

    elif first_area_measurement == 11 and second_area_measurement == 1: #Are to Mile
        Are = float(input("Enter You're Desired Number: "))
        Are_to_Mile = 0.00003861 * Are

        print(str(Are) + " Are is equal to " + str(Are_to_Mile) + " Mile.")

    elif first_area_measurement == 11 and second_area_measurement == 2: #Are to Acre
        Are = float(input("Enter You're Desired Number: "))
        Are_to_Acre = 0.024711 * Are

        print(str(Are) + " Are is equal to " + str(Are_to_Acre) + " Acre.")

    elif first_area_measurement == 11 and second_area_measurement == 3: #Are to Yard
        Are = float(input("Enter You're Desired Number: "))
        Are_to_Yard = 119.599005 * Are

        print(str(Are) + " Are is equal to " + str(Are_to_Yard) + " Yard.")

    elif first_area_measurement == 11 and second_area_measurement == 4: #Are to Foot
        Are = float(input("Enter You're Desired Number: "))
        Are_to_Foot = 1076 * Are

        print(str(Are) + " Are is equal to " + str(Are_to_Foot) + " Foot.")

    elif first_area_measurement == 11 and second_area_measurement == 5: #Are to Inch
        Are = float(input("Enter You're Desired Number: "))
        Are_to_Inch = 155000 * Are

        print(str(Are) + " Are is equal to " + str(Are_to_Inch) + " Inch.")

    elif first_area_measurement == 11 and second_area_measurement == 6: #Are to Kilometer
        Are = float(input("Enter You're Desired Number: "))
        Are_to_Kilometer = 0.0001 * Are

        print(str(Are) + " Are is equal to " + str(Are_to_Kilometer) + " Kilometer.")

    elif first_area_measurement == 11 and second_area_measurement == 7: #Are to Meter
        Are = float(input("Enter You're Desired Number: "))
        Are_to_Meter = 100 * Are

        print(str(Are) + " Are is equal to " + str(Are_to_Meter) + " Meter.")

    elif first_area_measurement == 11 and second_area_measurement == 8: #Are to Centimeter
        Are = float(input("Enter You're Desired Number: "))
        Are_to_Centimeter = 1000000 * Are

        print(str(Are) + " Are is equal to " + str(Are_to_Centimeter) + " Centimeter.")

    elif first_area_measurement == 11 and second_area_measurement == 9: #Are to Milimeter
        Are = float(input("Enter You're Desired Number: "))
        Are_to_Milimeter = 100000000 * Are

        print(str(Are) + " Are is equal to " + str(Are_to_Milimeter) + " Milimeter.")

    elif first_area_measurement == 11 and second_area_measurement == 10: #Are to Hectare
        Are = float(input("Enter You're Desired Number: "))
        Are_to_Hectare = 0.01 * Are

        print(str(Are) + " Are is equal to " + str(Are_to_Hectare) + " Hectare.")

    elif first_area_measurement == 11 and second_area_measurement == 11: #Are to Hectare
        print("Invalid Conversion!!")

def BMI():
    while True:
        weight_kg = float(input("Enter You're Desired Weight(Kg): "))
        height_m = float(input("Enter You're Desired Height(M): "))

        bmi = weight_kg / (height_m ** 2)
        format_bmi = "{:.2f}".format(bmi)

        if 16 <= bmi < 18.5:
            print("You're BMI is " + format_bmi + ", You should Gain some weight Asap. ")
            break

        elif 18.5 <= bmi < 24:
            print("You're BMI is " + format_bmi + ", Congrats! You're weight is Normal. ")
            break

        elif 24 <= bmi < 30:
            print("You're BMI is " + format_bmi + ", You're slightly Overweight , Watch out You're Diet. ")
            break

        elif 30 <= bmi < 35:
            print("You're BMI is " + format_bmi + ", You've got first Degree Obesity , You should go on a Diet. ")
            break

        elif 35 <= bmi < 40:
            print("You're BMI is " + format_bmi + ", You've got second Degree Obesity , You have to go on a Diet , It's almost Dangerous!")
            break

        elif bmi >= 40:
            print("You're BMI is " + format_bmi + ", You've got third Degree Obesity , You have to go on a Diet , You're Health care is in Danger! ")
            break
        else:
            print("Invalid Information due to super low BMI!\nPlease Enter again.")
            continue

def Data_Unit():
    Print_Data_Menu()

    first_data_conversion = input("-Which Data Unit You Desire to Convert From: ")
    second_data_conversion = input("-Which Data Unit You Desire to Convert To: ")

    if first_data_conversion == "1" and second_data_conversion == "1": # Bits to Bits
        print("Invalid Conversion!!")

    elif first_data_conversion == "1" and second_data_conversion == "2": # Bits to Bytes
        Bits = float(input("Enter You're Desired Number: "))
        Bits_to_Bytes = (1/8) * Bits
        
        print(str(Bits) + " Bits is equal to " + str(Bits_to_Bytes) + " Bytes.")

    elif first_data_conversion == "1" and second_data_conversion == "3": # Bits to KiloBytes
        Bits = float(input("Enter You're Desired Number: "))
        Bits_to_KiloBytes = 0.000125 * Bits
        
        print(str(Bits) + " Bits is equal to " + str(Bits_to_KiloBytes) + " KiloBytes.")

    elif first_data_conversion == "1" and second_data_conversion == "4": # Bits to MegaBytes
        Bits = float(input("Enter You're Desired Number: "))
        Bits_to_MegaBytes = 0.000000125 * Bits
        
        print(str(Bits) + " Bits is equal to " + str(Bits_to_MegaBytes) + " MegaBytes.")

    elif first_data_conversion == "1" and second_data_conversion == "5": # Bits to GigaBytes
        Bits = float(input("Enter You're Desired Number: "))
        Bits_to_GigaBytes = 0.000000000125 * Bits
        
        print(str(Bits) + " Bits is equal to " + str(Bits_to_GigaBytes) + " GigaBytes.")

    elif first_data_conversion == "1" and second_data_conversion == "6": # Bits to TeraBytes
        Bits = float(input("Enter You're Desired Number: "))
        Bits_to_TeraBytes = 0.000000000000125 * Bits
        
        print(str(Bits) + " Bits is equal to " + str(Bits_to_TeraBytes) + " TeraBytes.")

    elif first_data_conversion == "1" and second_data_conversion == "7": # Bits to PetaBytes
        Bits = float(input("Enter You're Desired Number: "))
        Bits_to_PetaBytes = 0.000000000000000125 * Bits
        
        print(str(Bits) + " Bits is equal to " + str(Bits_to_PetaBytes) + " PetaBytes.")

    elif first_data_conversion == "2" and second_data_conversion == "1": # Bytes to Bits
        Bytes = float(input("Enter You're Desired Number: "))
        Bytes_to_Bits = 8 * Bytes
        
        print(str(Bytes) + " Bytes is equal to " + str(Bytes_to_Bits) + " Bits.")

    elif first_data_conversion == "2" and second_data_conversion == "2": # Bytes to Bytes
        print("Invalid Conversion!!")

    elif first_data_conversion == "2" and second_data_conversion == "3": # Bytes to KiloBytes
        Bytes = float(input("Enter You're Desired Number: "))
        Bytes_to_KiloBytes = 0.001 * Bytes
        
        print(str(Bytes) + " Bytes is equal to " + str(Bytes_to_KiloBytes) + " KiloBytes.")

    elif first_data_conversion == "2" and second_data_conversion == "4": # Bytes to MegaBytes
        Bytes = float(input("Enter You're Desired Number: "))
        Bytes_to_MegaBytes = 0.000001 * Bytes
        
        print(str(Bytes) + " Bytes is equal to " + str(Bytes_to_MegaBytes) + " MegaBytes.")

    elif first_data_conversion == "2" and second_data_conversion == "5": # Bytes to GigaBytes
        Bytes = float(input("Enter You're Desired Number: "))
        Bytes_to_GigaBytes = 0.000000001 * Bytes
        
        print(str(Bytes) + " Bytes is equal to " + str(Bytes_to_GigaBytes) + " GigaBytes.")

    elif first_data_conversion == "2" and second_data_conversion == "6": # Bytes to TeraBytes
        Bytes = float(input("Enter You're Desired Number: "))
        Bytes_to_TeraBytes = 0.000000000001 * Bytes
        
        print(str(Bytes) + " Bytes is equal to " + str(Bytes_to_TeraBytes) + " TeraBytes.")

    elif first_data_conversion == "2" and second_data_conversion == "7": # Bytes to PetaBytes
        Bytes = float(input("Enter You're Desired Number: "))
        Bytes_to_PetaBytes = 0.000000000000001 * Bytes
        
        print(str(Bytes) + " Bytes is equal to " + str(Bytes_to_PetaBytes) + " PetaBytes.")

    elif first_data_conversion == "3" and second_data_conversion == "1": # KiloBytes to Bits
        KiloBytes = float(input("Enter You're Desired Number: "))
        KiloBytes_to_Bits = 8000 * KiloBytes
        
        print(str(KiloBytes) + " KiloBytes is equal to " + str(KiloBytes_to_Bits) + " KiloBytes.")

    elif first_data_conversion == "3" and second_data_conversion == "2": # KiloBytes to Bytes
        KiloBytes = float(input("Enter You're Desired Number: "))
        KiloBytes_to_Bytes = 1000 * KiloBytes
        
        print(str(KiloBytes) + " KiloBytes is equal to " + str(KiloBytes_to_Bytes) + " Bytes.")

    elif first_data_conversion == "3" and second_data_conversion == "3": # KiloBytes to KiloBytes
        print("Invalid Conversion!!")

    elif first_data_conversion == "3" and second_data_conversion == "4": # KiloBytes to MegaBytes
        KiloBytes = float(input("Enter You're Desired Number: "))
        KiloBytes_to_MegaBytes = 0.001 * KiloBytes
        
        print(str(KiloBytes) + " KiloBytes is equal to " + str(KiloBytes_to_MegaBytes) + " MegaBytes.")

    elif first_data_conversion == "3" and second_data_conversion == "5": # KiloBytes to GigaBytes
        KiloBytes = float(input("Enter You're Desired Number: "))
        KiloBytes_to_GigaBytes = 0.000001 * KiloBytes
        
        print(str(KiloBytes) + " KiloBytes is equal to " + str(KiloBytes_to_GigaBytes) + " GigaBytes.")

    elif first_data_conversion == "3" and second_data_conversion == "6": # KiloBytes to TeraBytes
        KiloBytes = float(input("Enter You're Desired Number: "))
        KiloBytes_to_TeraBytes = 0.000000001 * KiloBytes
        
        print(str(KiloBytes) + " KiloBytes is equal to " + str(KiloBytes_to_TeraBytes) + " TeraBytes.")

    elif first_data_conversion == "3" and second_data_conversion == "7": # KiloBytes to PetaBytes
        KiloBytes = float(input("Enter You're Desired Number: "))
        KiloBytes_to_PetaBytes = 0.000000000001 * KiloBytes
        
        print(str(KiloBytes) + " KiloBytes is equal to " + str(KiloBytes_to_PetaBytes) + " PetaBytes.")

    elif first_data_conversion == "4" and second_data_conversion == "1": # MegaBytes to Bits
        MegaBytes = float(input("Enter You're Desired Number: "))
        MegaBytes_to_Bits = 8000000 * MegaBytes
        
        print(str(MegaBytes) + " MegaBytes is equal to " + str(MegaBytes_to_Bits) + " Bits.")

    elif first_data_conversion == "4" and second_data_conversion == "2": # MegaBytes to Bytes
        MegaBytes = float(input("Enter You're Desired Number: "))
        MegaBytes_to_Bytes = 1000000 * MegaBytes
        
        print(str(MegaBytes) + " MegaBytes is equal to " + str(MegaBytes_to_Bytes) + " Bytes.")

    elif first_data_conversion == "4" and second_data_conversion == "3": # MegaBytes to KiloBytes
        MegaBytes = float(input("Enter You're Desired Number: "))
        MegaBytes_to_KiloBytes = 1000 * MegaBytes
        
        print(str(MegaBytes) + " MegaBytes is equal to " + str(MegaBytes_to_KiloBytes) + " KiloBytes.")

    elif first_data_conversion == "4" and second_data_conversion == "4": # MegaBytes to MegaBytes
        print("Invalid Conversion!!")

    elif first_data_conversion == "4" and second_data_conversion == "5": # MegaBytes to GigaBytes
        MegaBytes = float(input("Enter You're Desired Number: "))
        MegaBytes_to_GigaBytes = 0.001 * MegaBytes
        
        print(str(MegaBytes) + " MegaBytes is equal to " + str(MegaBytes_to_GigaBytes) + " GigaBytes.")

    elif first_data_conversion == "4" and second_data_conversion == "6": # MegaBytes to TeraBytes
        MegaBytes = float(input("Enter You're Desired Number: "))
        MegaBytes_to_TeraBytes = 0.000001 * MegaBytes
        
        print(str(MegaBytes) + " MegaBytes is equal to " + str(MegaBytes_to_TeraBytes) + " TeraBytes.")

    elif first_data_conversion == "4" and second_data_conversion == "7": # MegaBytes to PetaBytes
        MegaBytes = float(input("Enter You're Desired Number: "))
        MegaBytes_to_PetaBytes = 0.000000001 * MegaBytes
        
        print(str(MegaBytes) + " MegaBytes is equal to " + str(MegaBytes_to_PetaBytes) + " PetaBytes.")

    elif first_data_conversion == "5" and second_data_conversion == "1": # GigaBytes to Bits
        GigaBytes = float(input("Enter You're Desired Number: "))
        GigaBytes_to_Bits = 8000000000 * GigaBytes
        
        print(str(GigaBytes) + " GigaBytes is equal to " + str(GigaBytes_to_Bits) + " Bits.")

    elif first_data_conversion == "5" and second_data_conversion == "2": # GigaBytes to Bytes
        GigaBytes = float(input("Enter You're Desired Number: "))
        GigaBytes_to_Bytes = 1000000000 * GigaBytes
        
        print(str(GigaBytes) + " GigaBytes is equal to " + str(GigaBytes_to_Bytes) + " Bytes.")

    elif first_data_conversion == "5" and second_data_conversion == "3": # GigaBytes to KiloBytes
        GigaBytes = float(input("Enter You're Desired Number: "))
        GigaBytes_to_KiloBytes = 1000000 * GigaBytes
        
        print(str(GigaBytes) + " GigaBytes is equal to " + str(GigaBytes_to_KiloBytes) + " KiloBytes.")

    elif first_data_conversion == "5" and second_data_conversion == "4": # GigaBytes to MegaBytes
        GigaBytes = float(input("Enter You're Desired Number: "))
        GigaBytes_to_MegaBytes = 1000 * GigaBytes
        
        print(str(GigaBytes) + " GigaBytes is equal to " + str(GigaBytes_to_MegaBytes) + " MegaBytes.")

    elif first_data_conversion == "5" and second_data_conversion == "5": # GigaBytes to GigaBytes
        print("Invalid Conversion!!")

    elif first_data_conversion == "5" and second_data_conversion == "6": # GigaBytes to TeraBytes
        GigaBytes = float(input("Enter You're Desired Number: "))
        GigaBytes_to_TeraBytes = 0.001 * GigaBytes
        
        print(str(GigaBytes) + " GigaBytes is equal to " + str(GigaBytes_to_TeraBytes) + " TeraBytes.")

    elif first_data_conversion == "5" and second_data_conversion == "7": # GigaBytes to PetaBytes
        GigaBytes = float(input("Enter You're Desired Number: "))
        GigaBytes_to_PetaBytes = 0.000001 * GigaBytes
        
        print(str(GigaBytes) + " GigaBytes is equal to " + str(GigaBytes_to_PetaBytes) + " PetaBytes.")

    elif first_data_conversion == "6" and second_data_conversion == "1": # TeraBytes to Bits
        TeraBytes = float(input("Enter You're Desired Number: "))
        GigaBytes_to_Bits = 8000000000000 * TeraBytes
        
        print(str(TeraBytes) + " TeraBytes is equal to " + str(GigaBytes_to_Bits) + " Bits.")

    elif first_data_conversion == "6" and second_data_conversion == "2": # TeraBytes to Bytes
        TeraBytes = float(input("Enter You're Desired Number: "))
        GigaBytes_to_Bytes = 1000000000000 * TeraBytes
        
        print(str(TeraBytes) + " TeraBytes is equal to " + str(GigaBytes_to_Bytes) + " Bytes.")

    elif first_data_conversion == "6" and second_data_conversion == "3": # TeraBytes to KiloBytes
        TeraBytes = float(input("Enter You're Desired Number: "))
        GigaBytes_to_KiloBytes = 1000000000 * TeraBytes
        
        print(str(TeraBytes) + " TeraBytes is equal to " + str(GigaBytes_to_KiloBytes) + " KiloBytes.")

    elif first_data_conversion == "6" and second_data_conversion == "4": # TeraBytes to MegaBytes
        TeraBytes = float(input("Enter You're Desired Number: "))
        GigaBytes_to_MegaBytes = 1000000 * TeraBytes
        
        print(str(TeraBytes) + " TeraBytes is equal to " + str(GigaBytes_to_MegaBytes) + " MegaBytes.")

    elif first_data_conversion == "6" and second_data_conversion == "5": # TeraBytes to GigaBytes
        TeraBytes = float(input("Enter You're Desired Number: "))
        GigaBytes_to_GigaBytes = 1000 * TeraBytes
        
        print(str(TeraBytes) + " TeraBytes is equal to " + str(GigaBytes_to_GigaBytes) + " GigaBytes.")

    elif first_data_conversion == "6" and second_data_conversion == "6": # TeraBytes to TeraBytes
        print("Invalid Conversion!!")

    elif first_data_conversion == "6" and second_data_conversion == "7": # TeraBytes to PetaBytes
        TeraBytes = float(input("Enter You're Desired Number: "))
        GigaBytes_to_PetaBytes = 1000 * TeraBytes
        
        print(str(TeraBytes) + " TeraBytes is equal to " + str(GigaBytes_to_PetaBytes) + " PetaBytes.")

    elif first_data_conversion == "7" and second_data_conversion == "1": # PetaBytes to Bits
        PetaBytes = float(input("Enter You're Desired Number: "))
        PetaBytes_to_Bits = 8000000000000000 * PetaBytes
        
        print(str(PetaBytes) + " PetaBytes is equal to " + str(PetaBytes_to_Bits) + " Bits.")

    elif first_data_conversion == "7" and second_data_conversion == "2": # PetaBytes to Bytes
        PetaBytes = float(input("Enter You're Desired Number: "))
        PetaBytes_to_Bytes = 1000000000000000 * PetaBytes
        
        print(str(PetaBytes) + " PetaBytes is equal to " + str(PetaBytes_to_Bytes) + " Bytes.")

    elif first_data_conversion == "7" and second_data_conversion == "3": # PetaBytes to KiloBytes
        PetaBytes = float(input("Enter You're Desired Number: "))
        PetaBytes_to_KiloBytes = 1000000000000 * PetaBytes
        
        print(str(PetaBytes) + " PetaBytes is equal to " + str(PetaBytes_to_KiloBytes) + " KiloBytes.")

    elif first_data_conversion == "7" and second_data_conversion == "4": # PetaBytes to MegaBytes
        PetaBytes = float(input("Enter You're Desired Number: "))
        PetaBytes_to_MegaBytes = 1000000000 * PetaBytes
        
        print(str(PetaBytes) + " PetaBytes is equal to " + str(PetaBytes_to_MegaBytes) + " MegaBytes.")

    elif first_data_conversion == "7" and second_data_conversion == "5": # PetaBytes to GigaBytes
        PetaBytes = float(input("Enter You're Desired Number: "))
        PetaBytes_to_GigaBytes = 1000000 * PetaBytes
        
        print(str(PetaBytes) + " PetaBytes is equal to " + str(PetaBytes_to_GigaBytes) + " GigaBytes.")

    elif first_data_conversion == "7" and second_data_conversion == "6": # PetaBytes to TeraBytes
        PetaBytes = float(input("Enter You're Desired Number: "))
        PetaBytes_to_TeraBytes = 1000 * PetaBytes
        
        print(str(PetaBytes) + " PetaBytes is equal to " + str(PetaBytes_to_TeraBytes) + " TeraBytes.")

    elif first_data_conversion == "7" and second_data_conversion == "7": # PetaBytes to PetaBytes
        print("Invalid Conversion!!")

def Numeral_System():
    while True:
        Print_Numeral_System()

        first_conversion = input("-Which Numeral System You Desire to Convert From: ")

        second_conversion = input("-Which Numeral System You Desire to Convert To: ")

        if first_conversion == "1" and second_conversion == "1": #Decimal To Decimal
            print("\nInvalid Conversion!\n")
            continue

        elif first_conversion == "1" and second_conversion == "2": #Decimal To Binary
            Decimal_Input = int(input("Enter You're Desired Decimal Number: "))

            Decimal_To_Binary = bin(Decimal_Input)
            print("\n\nThe Given Decimal Number in Binary is " + str(Decimal_To_Binary) + ".\n\n")
            break

        elif first_conversion == "1" and second_conversion == "3": #Decimal To Octal
            Decimal_Input = int(input("Enter You're Desired Decimal Number: "))

            Decimal_To_Octal = oct(Decimal_Input)
            print("\n\nThe Given Decimal Number in Octal is " + str(Decimal_To_Octal) + ".\n\n")
            break

        elif first_conversion == "1" and second_conversion == "4": #Decimal To HexaDecimal
            Decimal_Input = int(input("Enter You're Desired Decimal Number: "))

            Decimal_To_HexaDecimal = hex(Decimal_Input)
            print("\n\nThe Given Decimal Number in HexaDecimal is " + str(Decimal_To_HexaDecimal) + ".\n\n")
            break

        elif first_conversion == "2" and second_conversion == "1": #Binary To Decimal
            Binary_Input = input("Enter You're Desired Binary Number: ")
            Binary_Conversion = int(Binary_Input , 2)
            
            Binary_To_Decimal = int(Binary_Conversion)
            print("\n\nThe Given Binary Number in Decimal is " + str(Binary_To_Decimal) + ".\n\n")
            break

        elif first_conversion == "2" and second_conversion == "2": #Binary To Binary
            print("\nInvalid Conversion!\n")
            continue

        elif first_conversion == "2" and second_conversion == "3": #Binary To Octal
            Binary_Input = input("Enter You're Desired Binary Number: ")
            Binary_Conversion = int(Binary_Input , 2)
            
            Binary_To_Octal = oct(Binary_Conversion)
            print("\n\nThe Given Binary Number in Octal is " + str(Binary_To_Octal) + ".\n\n")
            break

        elif first_conversion == "2" and second_conversion == "4": #Binary To HexaDecimal
            Binary_Input = input("Enter You're Desired Binary Number: ")
            Binary_Conversion = int(Binary_Input , 2)
            
            Binary_To_HexaDecimal = hex(Binary_Conversion)
            print("\n\nThe Given Binary Number in HexaDecimal is " + str(Binary_To_HexaDecimal) + ".\n\n")
            break

        elif first_conversion == "3" and second_conversion == "1": #Octal To Decimal
            Octal_Input = input("Enter You're Desired Octal Number: ")
            Octal_Conversion = int(Octal_Input , 8)
            
            Octal_To_HexaDecimal = int(Octal_Conversion)
            print("\n\nThe Given Octal Number in Decimal is " + str(Octal_To_HexaDecimal) + ".\n\n")
            break

        elif first_conversion == "3" and second_conversion == "2": #Octal To Binary
            Octal_Input = input("Enter You're Desired Octal Number: ")
            Octal_Conversion = int(Octal_Input , 8)
            
            Octal_To_Binary = bin(Octal_Conversion)
            print("\n\nThe Given Octal Number in Binary is " + str(Octal_To_Binary) + ".\n\n")
            break

        elif first_conversion == "3" and second_conversion == "3": #Octal To Octal
            print("\nInvalid Conversion!\n")
            continue

        elif first_conversion == "3" and second_conversion == "4": #Octal To HexaDecimal
            Octal_Input = input("Enter You're Desired Octal Number: ")
            Octal_Conversion = int(Octal_Input , 8)
            
            Octal_To_HexaDecimal = hex(Octal_Conversion)
            print("\n\nThe Given Octal Number in HexaDecimal is " + str(Octal_To_HexaDecimal) + ".\n\n")
            break

        elif first_conversion == "4" and second_conversion == "1": #HexaDecimal To Decimal
            HexaDecimal_Input = input("Enter You're Desired HexaDecimal Number: ")
            HexaDecimal_Conversion = int(HexaDecimal_Input , 16)
            
            HexaDecimal_To_Decimal = int(HexaDecimal_Conversion)
            print("\n\nThe Given HexaDecimal Number in Decimal is " + str(HexaDecimal_To_Decimal) + ".\n\n")
            break

        elif first_conversion == "4" and second_conversion == "2": #HexaDecimal To Binary
            HexaDecimal_Input = input("Enter You're Desired HexaDecimal Number: ")
            HexaDecimal_Conversion = int(HexaDecimal_Input , 16)
            
            HexaDecimal_To_Binary = bin(HexaDecimal_Conversion)
            print("\n\nThe Given HexaDecimal Number in Binary is " + str(HexaDecimal_To_Binary) + ".\n\n")
            break

        elif first_conversion == "4" and second_conversion == "3": #HexaDecimal To Octal
            HexaDecimal_Input = input("Enter You're Desired HexaDecimal Number: ")
            HexaDecimal_Conversion = int(HexaDecimal_Input , 16)
            
            HexaDecimal_To_Octal = oct(HexaDecimal_Conversion)
            print("\n\nThe Given HexaDecimal Number in Octal is " + str(HexaDecimal_To_Octal) + ".\n\n")
            break
            break

        elif first_conversion == "4" and second_conversion == "4": #HexaDecimal To HexaDecimal
            print("\nInvalid Conversion!\n")
            continue
        
        else:
            print("\nInvalid Input!\n")
            continue

def Temperature_Conversion():
    while True:
        Print_Temperature_Conversion()

        first_conversion = input("-Which Temperature Unit You Desire to Convert From: ")

        second_conversion = input("-Which Temperature Unit You Desire to Convert To: ")
        
        if first_conversion == "1" and second_conversion == "1": #Celsius To Celsius
            print("\nInvalid Conversion!\n")
            continue
        
        elif first_conversion == "1" and second_conversion == "2": #Celsius To Fahrenheit
            Celsius = float(input("Enter You're Desired Celsius Temperature: "))
            C_to_F = (Celsius * (9/5)) + 32
            format_C_to_F = "{:.2f}".format(C_to_F)
            print("You're Conversion from Celsius to Fahrenheit is: " + format_C_to_F + " F")
            break
            
        elif first_conversion == "1" and second_conversion == "3": #Celsius To Kelvin
            Celsius = float(input("Enter You're Desired Celsius Temperature: "))
            C_to_K = Celsius + 273.15
            format_C_to_K = "{:.2f}".format(C_to_K)
            print("You're Conversion from Celsius to Kelvin is: " + format_C_to_K + " K")
            break
            
        elif first_conversion == "2" and second_conversion == "1": #Fahrenheit To Celsius
            Fahrenheit = float(input("Enter You're Desired Fahrenheit Temperature: "))
            F_to_C = (Fahrenheit - 32) * (5/9)
            format_F_to_C = "{:.2f}".format(F_to_C)
            print("You're Conversion from Fahrenheit to Celsius is: " + format_F_to_C + " C")
            break
            
        elif first_conversion == "2" and second_conversion == "2": #Fahrenheit To Fahrenheit
            print("\nInvalid Conversion!\n")
            continue
        
        elif first_conversion == "2" and second_conversion == "3": #Fahrenheit To Kelvin
            Fahrenheit = float(input("Enter You're Desired Fahrenheit Temperature: "))
            F_to_K = (Fahrenheit - 32) * (5/9) + 273.15
            format_F_to_K = "{:.2f}".format(F_to_K)
            print("You're Conversion from Fahrenheit to Kelvin is: " + format_F_to_K + " K")
            break
        
        elif first_conversion == "3" and second_conversion == "1": #Kelvin To Celsius
            Kelvin = float(input("Enter You're Desired Kelvin Temperature: "))
            K_to_C = Kelvin - 273.15
            format_K_to_C = "{:.2f}".format(K_to_C)
            print("You're Conversion from Kelvin to Celsius is: " + format_K_to_C + " C")
            break
        
        elif first_conversion == "3" and second_conversion == "2": #Kelvin To Fahrenheit
            Kelvin = float(input("Enter You're Desired Kelvin Temperature: "))
            K_to_F = (Kelvin - 273.15) * (9/5) + 32
            format_K_to_F = "{:.2f}".format(K_to_F)
            print("You're Conversion from Kelvin to Fahrenheit is: " + format_K_to_F + " F")
            break
        
        elif first_conversion == "3" and second_conversion == "3": #Kelvin To Kelvin
            print("\nInvalid Conversion!\n")
            continue
        
        else: #Invalid Input
            print("\nInvalid Input!\n")
            continue

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
                    
                    elif conversion_menu == "2": #BMI
                        BMI()
                        while True:
                            Inner_Print()
                            bmi_menu = input("-Waiting for You're Desire: ")
                            
                            if bmi_menu == "1": #Continue
                                BMI()
                            
                            elif bmi_menu == "-": #Back
                                break

                            elif bmi_menu == "q" or bmi_menu == "Q": #Exit
                                sys.exit(1)
                            
                            else:
                                print("Invalid option!\nEnter again: ")
                                continue
                    
                    elif conversion_menu == "3": #Data Unit
                        Data_Unit()
                        while True:
                            Inner_Print()
                            data_menu = input("-Waiting for You're Desire: ")
                            
                            if data_menu == "1": #Continue
                                Data_Unit()
                            
                            elif data_menu == "-": #Back
                                break

                            elif data_menu == "q" or data_menu == "Q": #Exit
                                sys.exit(1)
                            
                            else:
                                print("Invalid option!\nEnter again: ")
                                continue
                    
                    elif conversion_menu == "4": #Numeral System
                        Numeral_System()
                        while True:
                            Inner_Print()
                            numeral_system_menu = input("-Waiting for You're Desire: ")
                            
                            if numeral_system_menu == "1": #Continue
                                Numeral_System()
                            
                            elif numeral_system_menu == "-": #Back
                                break

                            elif numeral_system_menu == "q" or numeral_system_menu == "Q": #Exit
                                sys.exit(1)
                            
                            else:
                                print("Invalid option!\nEnter again: ")
                                continue
                    
                    elif conversion_menu == "5": #Temperature Conversion
                        Temperature_Conversion()
                        while True:
                            Inner_Print()
                            temp_menu = input("-Waiting for You're Desire: ")
                            
                            if temp_menu == "1": #Continue
                                Temperature_Conversion()
                            
                            elif temp_menu == "-": #Back
                                break

                            elif temp_menu == "q" or temp_menu == "Q": #Exit
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
