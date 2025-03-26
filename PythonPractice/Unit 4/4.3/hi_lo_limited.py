import random
num = random.randrange(1,101)
count = 1
max = 7
print(f"I have chosen a number between 1 and 100. Try to guess it.{num}")
guess = int(input("Your Guess: "))


while count <= max:
    if guess > num:
        print("That is too high. Guess again.")  
    elif guess < num:
        print("That is too low. Guess again.")
    else:
        print("You are correct!")
        break
    
    count += 1
    if count >= 7:
        print("Sorry, you didn't guess it in 7 tries.  You lose.")
        break
    guess = int(input("Your Guess: "))
