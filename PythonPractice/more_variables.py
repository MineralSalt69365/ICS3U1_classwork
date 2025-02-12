store = "No Frills"
item = "Apples"
price = 2
quantity = 100
subtotal = price * quantity
tax = subtotal * 0.05
total = tax + subtotal

print(f"At {store} I bought some {item}.") #f-string
print("They sold for $" + str(price) + " each.") #concatenation
print("I wanted to purchase {} of them.".format(quantity)) #dot dormat
print(f"The subtoal before addint the tax is ${subtotal}.")#f-string
print(f"And we need to add up ${tax} for tax") #f-string
print(f"The total price, with tax included, was ${total}.") #f-string
