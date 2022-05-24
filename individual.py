import math
print("The bases of the isosceles trapezoid and the angle with a larger base are given.")
print("Find the area of the trapezoid.")
a = float(input("Enter the length of the larger base a: "))
b = float(input("Enter the length of the smaller base b: "))
rov = float(input("Enter the angle at a larger base in degrees: "))
S = (a**2-b**2)/4*math.tan(rov*math.pi/180)
D = round(S, 2)
print(D)

