# NAME: William Poole
# ASSIGNMENT: Hw2 q3
# COLLABORATION: none
# Write a program which will calculate and print the volume of certain geometric shapes. Your program will first
# ask the user to select a geometric shape. The options are 1: Cube, 2: Sphere, 3: Cylinder. Then your program
# will ask for the necessary dimensions. The key to this problem is decision logic: if, elif, and else.
import math
radius = 0
height = 0
v = int(0)
x=int(input("Select geometeric shape [1] Cube, [2] Sphere, [3] Cylinder: "))
if x==1:
    v = float(input("Enter length of face in inches: "))**3
elif x==2:
    v= (float(input("Enter radius of sphere in inches: "))**2)*(math.pi)*(4/3)
elif x==3:
    radius = float(input("Enter radius of cylinder in inches: "))
    height = float(input("Enter height of cylinder in inches: "))
    v = float((math.pi)*(height)*((radius)**2))
print(v)