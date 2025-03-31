import math

print("SQUARE ROOT!")
num = int(input("Enter Number:"))

while num < 0:
    print("You can't take the square root of a negative number, silly.")
    num = int(input("Try Again:"))

root = math.sqrt(num)
print(f"The square root of {num} is {root}.")
