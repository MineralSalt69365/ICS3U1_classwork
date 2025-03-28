# 1. Create a loop that counts from 0 to 10, but skip the number 7.
count = 0
while count < 11:
    if count == 7:
        count += 1
        continue
    print(count)
# 2. Create a loop that will add the numbers from 5 to 20 but not any multiples of 3. Use modulus.
num = 5
total = 0
while num <= 20:
    if num % 3 == 0:
        num += 1 
        continue
    total += num
    num += 1
print(total)

# 3. Ask the user for a starting number and an ending number. The program will get the sum of all the numbers from the start to the end (using a loop). However, our program is a bit of a diva: the program will stop summing the numbers if it encounters a 13 or a 31. It will still output the sum up to that point.
start = int(input("Enter a starting number:"))
end = int(input("Enter a ending number girrrl:"))
total = 0

while start <= end:
    if start == 13 or start == 31:
        break
    total += start
    start += 1

print(total)
# 4. Create an infinite loop using while True:. In that loop ask the user for a word. For each word they enter, output the following "Your word: {word}". If ever they enter the word "stop" the program will break out of the loop. Finally the program will output "Goodbye!".
run = True
while run:
    word = input("Enter a word:")
    if word == "stop":
        break
    print(f"Your word: {word}")
print("Goodbye!")