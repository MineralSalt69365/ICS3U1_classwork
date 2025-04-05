import random

number = []
for x in range(10):
    number.append(random.randrange(1, 101))
print("Array:", number)

largest = number[0]
largest_location = 0

for location, i in enumerate(number):
    if i > largest:
        largest = i
        largest_location = location
    
print(f"The largest number is {largest}")
print(f"It is at {largest_location}")