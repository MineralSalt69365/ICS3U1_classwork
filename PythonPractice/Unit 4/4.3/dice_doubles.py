import random

dice1 = random.randrange(1,7)
dice2 = random.randrange(1,7)
total = dice2 + dice2
print("HERE COMES THE DICE!")
print(f"roll 1 : {dice1}")
print(f"roll 2 : {dice2}")
print(f"The total is {total}!")

while dice1 != dice2:
    print("HERE COMES THE DICE!")
    dice1 = random.randrange(1,7)
    dice2 = random.randrange(1,7)
    total = dice2 + dice2
    print(f"roll 1 : {dice1}")
    print(f"roll 2 : {dice2}")
    print(f"The total is {total}!")
