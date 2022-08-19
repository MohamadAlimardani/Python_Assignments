
password = 1234
report_police = 4321
counter = 4

while True:
    print("\n")
    user_pass = int(input("Enter You're Password: "))
    print("\n")
    
    if password == user_pass:
        print("You're Successfully Logged in.")
        break
    
    elif not 1000 <= user_pass <= 9999:
        print("You Must Enter a 4-Digit Password.\nPlease Enter You're Password Again: ")
        continue
    
    elif user_pass == report_police:
        print("You Better Run Filthy Thieve , Coz You're About to get caught!.  (x(x_(o_o)_x)x)"
        + "\nMake Sure You come Back Later.\n(^_^)\n")
        break    
    else:
        counter -= 1
        if counter != 0:
            print("You've Got only " + str(counter) + " more Tries.\n")
            continue

        else:
            print("You've Got No More Tries.\n\nYou're Account got locked Due to Entering Wrong Password.\n\n")
            break
