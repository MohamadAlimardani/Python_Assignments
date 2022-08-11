
static_username = "Alimardani"
static_password = 12345

const = (0 , 1 , 2 , 3)

loop_counter = const[0]
counter_tries = const[0]
counter_limit = const[0]

while loop_counter < const[3]:

    loop_counter += const[1]
    counter_tries = const[3] - loop_counter

    dynamic_username = input("Enter you're Username: ")
    dynamic_password = int(input("Enter you're Password: "))

    if static_username == dynamic_username and static_password == dynamic_password:
        print("You're Successfully Logged in. ")
        break
    
    elif static_username != dynamic_username or static_password != dynamic_password:
        counter_limit += const[1]
        if const[2] <= counter_tries <= const[3]:
            print("Username or Password is Wrong! " , "\nYou've got only \"" , counter_tries , "\" more tries. ")
            continue
        elif counter_tries == const[1]:
            print("You've got only \"" , counter_tries , "\" more try. ")
            continue
        else:
            print("You've got no more tries. ")

if counter_limit == const[3]:
    print("You're Account has been Locked due to Entering wrong informations. ")
