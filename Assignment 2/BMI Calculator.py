
while True:

    weight_kg = float(input("Enter You're Desired Weight(Kg): "))
    height_m = float(input("Enter You're Desired Height(M): "))

    bmi = weight_kg / (height_m ** 2)
    format_bmi = "{:.2f}".format(bmi)

    if 16 <= bmi < 18.5:
        print("You're BMI is " + str(format_bmi) + ", You should Gain some weight Asap. ")
        break

    elif 18.5 <= bmi < 24:
        print("You're BMI is " + str(format_bmi) + ", Congrats! You're weight is Normal. ")
        break

    elif 24 <= bmi < 30:
        print("You're BMI is " + str(format_bmi) + ", You're slightly Overweight , Watch out You're Diet. ")
        break

    elif 30 <= bmi < 35:
        print("You're BMI is " + str(format_bmi) + ", You've got first Degree Obesity , You should go on a Diet. ")
        break

    elif 35 <= bmi < 40:
        print("You're BMI is " + str(format_bmi) + ", You've got second Degree Obesity , You have to go on a Diet , It's almost Dangerous!")
        break

    elif bmi >= 40:
        print("You're BMI is " + str(format_bmi) + ", You've got third Degree Obesity , You have to go on a Diet , You're Health care is in Danger! ")
        break
    else:
        print("Invalid Information due to super low BMI!\nPlease Enter again.")
        continue
