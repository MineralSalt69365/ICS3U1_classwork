import random

list = []
for x in range(10):
    list.append(random.randrange(1, 51))
print("List:", list)

find_value = int(input("Value to find:"))

for i, number in enumerate(list):
    if number == find_value:
        print(f'{number} is in the list')
