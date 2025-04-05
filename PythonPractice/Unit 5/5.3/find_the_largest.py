import random

number = []
for x in range(10):
    number.append(random.randrange(1, 101))
print("Array:", number)

largest = number[0]

for i in number:
    if i > largest:
        largest = i
    
print(f"The largest number is {largest}")