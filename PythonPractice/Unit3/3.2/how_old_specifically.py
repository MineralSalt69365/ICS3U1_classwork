name = input("Hey, what's your name? (Sorry, I keep forgetting):")
age = int(input(f"Ok, {name}, how old are you?"))

if age < 16:
    print("you can't drive, you can't vote and you can't rent a car!!")
elif 16< age <18:
    print("you can't vote or rent a car!!")
elif 18< age < 21:
    print("You can't rent a car!")
else:
    print("You can do anything legal!!!")    
