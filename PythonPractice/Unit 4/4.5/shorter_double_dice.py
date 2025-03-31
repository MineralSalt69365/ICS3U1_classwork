import random


while True:
    print("HERE COMES THE DICE!")
    dice1 = random.randrange(1,7)
    dice2 = random.randrange(1,7)
    total = dice1 + dice2
    print(f"roll 1 : {dice1}")
    print(f"roll 2 : {dice2}")
    print(f"The total is {total}!")

    if dice1 == dice2:
        break

