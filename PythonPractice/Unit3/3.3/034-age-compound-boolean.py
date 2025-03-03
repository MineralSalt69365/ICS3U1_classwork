name = input("Your name:")
age = int(input("Your age:"))

if age < 16:
    print("you can't drive, you can't vote and you can't rent a car!!")
if age <18 and age >= 16:
    print("you can't vote or rent a car!!")
if age < 21 and age >= 18:
    print("You can't rent a car!")
if age > 21:
    print("You can do anything legal!!!") 