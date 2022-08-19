
import random as ran

dice_number = []
while True:
    dice_number.append(ran.randint(0 , 6))
    if 6 in dice_number:
        print("\n\nSum of All Pulled Numbers: " + str(sum(dice_number)))
        break
    
    else:
        continue

print("\nNumber of Tries To Get Number '6': " + str(len(dice_number)-1) + "\n\n")