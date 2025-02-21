age = int(input("How old are you!!!"))
if age < 16:
    print("you can't drive, you can't vote and you can't rent a car!!")
elif age <18:
    print("you can't vote or rent a car!!")
elif age < 21:
    print("You can't rent a car!")
else:
    print("You can anything legal!!!")