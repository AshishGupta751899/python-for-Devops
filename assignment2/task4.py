# Task: Calculate the Area of a Circle
# ● Objective: Write a program to calculate the area of a circle.
# ● Hints:
# ○ Ask the user to input the radius of the circle.
# ○ Calculate the area of the circle using the formula: Area = π *
# radius^2.
# ○ Display the calculated area.

import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
   
print(f"The area of the circle with radius {radius} is: {area:.2f}")
