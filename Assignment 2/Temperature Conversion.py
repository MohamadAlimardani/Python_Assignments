
while True:
    print("Hi! \n-Choose an option from below: \n" , 
    "\n1.Fahrenheit to Celsius. " , 
    "\n2.Celsius to Fahrenheit. " , 
    "\n3.Kelvin to Celsius. " , 
    "\n4.Celsius to Kelvin. " , 
    "\n5.Kelvin to Fahrenheit. " , 
    "\n6.Fahrenheit to Kelvin. \n")
    number_of_option = int(input("-Waiting for you're Desire: "))

    if number_of_option == 1:
        Fahrenheit = float(input("Enter You're Desired Fahrenheit Temperature: "))
        F_to_C = (Fahrenheit - 32) * (5/9)
        format_F_to_C = "{:.2f}".format(F_to_C)
        print("You're Conversion from Fahrenheit to Celsius is: " , format_F_to_C)
        while True:
            print("-Choose an option from below: " , "\n1.Back to Main Menu! " , "\n2.Exit! ")    
            num_continue = int(input("-Waiting for you're Desire: "))
            if num_continue == 1:
                break
            elif num_continue == 2:
                exit = True
                break
            else:
                print("Invalid option!\nEnter again: ")
                continue
        
        if exit == True:
            break
        else:
            continue
    
    elif number_of_option == 2:
        Celsius = float(input("Enter You're Desired Celsius Temperature: "))
        C_to_F = (Celsius * (9/5)) + 32
        format_C_to_F = "{:.2f}".format(C_to_F)
        print("You're Conversion from Celsius to Fahrenheit is: " , format_C_to_F)
        while True:
            print("-Choose an option from below: " , "\n1.Back to Main Menu! " , "\n2.Exit! ")    
            num_continue = int(input("-Waiting for you're Desire: "))
            if num_continue == 1:
                break
            elif num_continue == 2:
                exit = True
                break
            else:
                print("Invalid option!\nEnter again: ")
                continue
        
        if exit == True:
            break
        else:
            continue
    
    elif number_of_option == 3:
        Kelvin = float(input("Enter You're Desired Kelvin Temperature: "))
        K_to_C = Kelvin - 273.15
        format_K_to_C = "{:.2f}".format(K_to_C)
        print("You're Conversion from Kelvin to Celsius is: " , format_K_to_C)
        while True:
            print("-Choose an option from below: " , "\n1.Back to Main Menu! " , "\n2.Exit! ")    
            num_continue = int(input("-Waiting for you're Desire: "))
            if num_continue == 1:
                break
            elif num_continue == 2:
                exit = True
                break
            else:
                print("Invalid option!\nEnter again: ")
                continue
        
        if exit == True:
            break
        else:
            continue
    
    elif number_of_option == 4:
        Celsius = float(input("Enter You're Desired Celsius Temperature: "))
        C_to_K = Celsius + 273.15
        format_C_to_K = "{:.2f}".format(C_to_K)
        print("You're Conversion from Celsius to Kelvin is: " , format_C_to_K)
        while True:
            print("-Choose an option from below: " , "\n1.Back to Main Menu! " , "\n2.Exit! ")    
            num_continue = int(input("-Waiting for you're Desire: "))
            if num_continue == 1:
                break
            elif num_continue == 2:
                exit = True
                break
            else:
                print("Invalid option!\nEnter again: ")
                continue
        
        if exit == True:
            break
        else:
            continue
    
    elif number_of_option == 5:
        Kelvin = float(input("Enter You're Desired Kelvin Temperature: "))
        K_to_F = (Kelvin - 273.15) * (9/5) + 32
        format_K_to_F = "{:.2f}".format(K_to_F)
        print("You're Conversion from Kelvin to Fahrenheit is: " , format_K_to_F)
        while True:
            print("-Choose an option from below: " , "\n1.Back to Main Menu! " , "\n2.Exit! ")    
            num_continue = int(input("-Waiting for you're Desire: "))
            if num_continue == 1:
                break
            elif num_continue == 2:
                exit = True
                break
            else:
                print("Invalid option!\nEnter again: ")
                continue
        
        if exit == True:
            break
        else:
            continue
    
    elif number_of_option == 6:
        Fahrenheit = float(input("Enter You're Desired Fahrenheit Temperature: "))
        F_to_K = (Fahrenheit - 32) * (5/9) + 273.15
        format_F_to_K = "{:.2f}".format(F_to_K)
        print("You're Conversion from Fahrenheit to Kelvin is: " , format_F_to_K)
        while True:
            print("-Choose an option from below: " , "\n1.Back to Main Menu! " , "\n2.Exit! ")    
            num_continue = int(input("-Waiting for you're Desire: "))
            if num_continue == 1:
                break
            elif num_continue == 2:
                exit = True
                break
            else:
                print("Invalid option!\nEnter again: ")
                continue
        
        if exit == True:
            break
        else:
            continue
    
    else:
        print("Invalid option!\nChoose again: ")
        continue
