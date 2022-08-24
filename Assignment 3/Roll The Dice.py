
import random as ran

dice_number = []
while True:
    dice = ran.randint(1 , 6)
    dice_number.append(dice)  
    if dice == 6:
        continue
    
    else:
        print("\n\nSum of All Pulled Numbers: " + str(sum(dice_number)) 
        + "\n\nList Of Numbers That We Pulled from Rolling The Dice: \n" + str(dice_number))
        break

print("\nNumber of Tries: " + str(len(dice_number)) + "\n\n")
