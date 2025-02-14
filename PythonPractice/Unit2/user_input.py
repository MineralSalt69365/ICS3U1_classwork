print("Enter the following information about an item you wish to purchase..")
print()

name = input("The name of the item:")

price = float(input("The price: $"))

quantity = int(input("How many do you want?"))

subtotal = price * quantity
tax = subtotal * 0.13
total = subtotal + tax

print()
print(f"You choose to buy {quantity} {name}.")
print(f"That will come out to ${total}")

#3. The input of the name is above the question, this make the computer ask for input first then print out the question, which can confuse the users.
#4. int() and float() convert variable into integer/decimals. If I remove them, they won't be able to multiply each other becasue they are consider string for computer.