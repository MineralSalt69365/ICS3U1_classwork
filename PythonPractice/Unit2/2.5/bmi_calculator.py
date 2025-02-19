
height_feet = float(input("height in feet:"))
height_inches = float(input("height in inches:"))
weight_pounds = float(input("weight in pounds:"))
height = ((height_feet*12)+ height_inches) / 39.370079
weight = weight_pounds * 0.45359237
bmi = weight/height**2

print(f"{bmi}")