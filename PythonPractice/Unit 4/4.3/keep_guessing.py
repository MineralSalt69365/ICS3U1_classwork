import random
magical_num = random.randrange(1,11)
print("I have chosen a number between 1 and 10. Try to guess it.")
guess = int(input("Your Guess: "))

while guess != magical_num:
    print("That is incorrect. Guess again.")
    guess = int(input("Your Guess: "))

print("You are correct!")
