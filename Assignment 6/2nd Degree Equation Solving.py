
import math

def Equation_2nd_degree(a , b , c):
    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print(f"\n{a}x² + {b}x + {c} = 0" + "\n\nThe Given Equation Has No Answers.\n")

    elif delta == 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        print(f"\n{a}x² + {b}x + {c} = 0" + "\n\nx1 = x2 = " , x1 , "\n")

    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        format_x1 = "{:.4f}".format(x1)
        
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        format_x2 = "{:.4f}".format(x2)
        
        print(f"\n{a}x² + {b}x + {c} = 0" + "\n\nx1 =" , format_x1 , "\nx2 =" , format_x2 , "\n")

print("\n\nax² + bx + c = 0\n")
a = int(input("Enter The Value of \"a\": "))

print(f"\n\n{a}x² + bx + c = 0\n")
b = int(input("Enter The Value of \"b\": "))

print(f"\n\n{a}x² + {b}x + c = 0\n")
c = int(input("Enter The Value of \"c\": "))

print(f"\n\nYou're Desired Equation: \n{a}x² + {b}x + {c} = 0\n\n")

Equation_2nd_degree(a , b , c)