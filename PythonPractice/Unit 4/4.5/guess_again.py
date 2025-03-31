import random
magical_num = random.randrange(1,11)
count = 1

while True:
    print("That is incorrect. Guess again.")
    count += 1
    guess = int(input("Your Guess: "))

    if guess == magical_num:
        break

print("You are correct!")
print(f"It took you {count} tries!")