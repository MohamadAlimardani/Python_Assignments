
import math as mt
import os

angles = dict()
for i in range(361):
    if i == 90 or i == 270:
        angles[i] = 0.00000
        continue
    angles[i] = "{:.5f}".format(mt.cos(mt.radians(i)))

os.system("cls")
while True:
    angle = int(input("Enter an Angle(In Degrees) Between 0° - 360°: "))
    os.system("cls")
    print(f"Cos({angle}°) =", angles[angle], 2 * "\n")