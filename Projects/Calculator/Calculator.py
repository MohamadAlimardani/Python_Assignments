
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
            + "\n| 1.Sum." + 16 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
            + "\n| 2.Subtraction." + 8 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
            + "\n| 3.Multiplication." + 5 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
            + "\n| 4.Division." + 11 * " " + "|" + "\n" + "|" + 23 * "-" + "|" 
            + "\n| 5.Remainder." + 10 * " " + "|" + "\n" + "|" + 23 * "-" + "|" 
            + "\n| 6.Percentage." + 9 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
            + "\n| - Back." + 15 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
            + "\n| Q.Exit." + 15 * " " + "|" + "\n" + "|" + 23 * "_" + "|\n")

def Print_Advanced_Menu():
    print(" " + 4 * "*" + " Advanced Menu " + 4 * "*" + "\n " + 23 * "_" + "\n" + "| -Choose an Option: " + 3 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
            + "\n| 1.Trigonometry." + 7 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
            + "\n| 2.Other Operations." + 3 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
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

def Inner_Print():
    print(" " + 23 * "_" + "\n" + "| -Choose an Option: " + 3 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
        + "\n| 1.Continue." + 11 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
        + "\n| - Back." + 15 * " " + "|" + "\n" + "|" + 23 * "-" + "|"
        + "\n| Q.Exit." + 15 * " " + "|" + "\n" + "|" + 23 * "_" + "|\n")

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

while True: #Main Menu
    Print_Main_Menu()
    menu = input("-Waiting for You're Desire: ")
    print("\n\n")

    if menu == "1": #Basic Menu
        while True: #Basic Menu
            Print_Basic_Menu()
            basic_menu = input("-Waiting for You're Desire: ")
            print("\n\n")

            if basic_menu == "1": #Sum             
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

            elif basic_menu == "2": #Subtraction
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
                
            elif basic_menu == "3": #Multiplication             
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
                
            elif basic_menu == "4": #Division             
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
            
            elif basic_menu == "5": #Remainder             
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

            elif basic_menu == "6": #Percentage             
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

            elif advanced_menu == "-": #Back
                break

            elif advanced_menu == "q" or advanced_menu == "Q": #Exit
                sys.exit(1)

            else: #Invalid
                print("Invalid Option!\nPlease Choose Again.")
                continue

    elif menu == "q" or menu == "Q": #Exit
        sys.exit(1)