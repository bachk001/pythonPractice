"""
### Task #8

✅ Triangle Classifier:

Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sides are equal),
isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle.
"""
L1 = int(input("Enter L1 : "))
L2 = int(input("Enter L2 : "))
L3 = int(input("Enter L3 : "))

if L1==L2 and L2==L3 and L1==L3:
    print("Equilateral Triangle")
elif L1!=L2 and L2!=L3 and L1!=L3:
    print("Scalene Triangle")
else:
    print("Isosceles Triangle")