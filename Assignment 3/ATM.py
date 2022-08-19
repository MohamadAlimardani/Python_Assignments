
password = 1234
counter = 3
for i in range(4):
    flag = counter-i
    print("\n")
    user_pass = int(input("Enter You're Password: "))
    print("\n")
    
    if password == user_pass:
        print("You're Successfully Logged in.")
        break
    
    else:
        if flag != 0:
            print("You've Got only " + str(flag) + " more Tries.\n")
        
        else:
            print("You've Got No More Tries.\n\nYou're Account got locked Due to Entering Wrong Password.\n\n")