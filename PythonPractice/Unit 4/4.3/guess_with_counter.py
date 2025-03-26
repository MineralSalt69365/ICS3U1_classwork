import random
magical_num = random.randrange(1,11)
count = 1

print("I have chosen a number between 1 and 10. Try to guess it.")
guess = int(input("Your Guess: "))


while guess != magical_num:
    print("That is incorrect. Guess again.")
    count += 1
    guess = int(input("Your Guess: "))

print("You are correct!")
print(f"It took you {count} tries!")

