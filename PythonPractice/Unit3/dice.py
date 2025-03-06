import random
cpt_score = 0
user_score = 0
game = True

print("welcome to dice game!")
for i in range (3):
    input("Press ENTER to start game.")

    cpt_dice = random.randrange(1,7)
    user_dice = random.randrange(1,7)

    print(f"you rolled a {user_dice}, computer rolled a {cpt_dice}")

    if cpt_dice > user_dice:
        cpt_score += 1
        print("you lose!")
        print(f"You:{user_score}, Computer:{cpt_score}")
    elif cpt_dice < user_dice:
        user_score += 1
        print("you win!")
        print(f"You:{user_score}, Computer:{cpt_score}")
    else:
        print("its a tie")
        print(f"You:{user_score}, Computer:{cpt_score}")
    
    if cpt_score == 2 or user_score == 2:
        print("game over")
        game = False
    elif cpt_score == 3 or user_score == 3:
        print("game over")
        game = False
    else:
        game = True
