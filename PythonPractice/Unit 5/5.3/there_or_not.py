import random

list = []
for x in range(10):
    list.append(random.randrange(1, 51))
print("List:", list)

find_value = int(input("Value to find:"))
count = 0

for i, number in enumerate(list):
    if number == find_value:
        count += 1

if count >= 1:
    print(f'{find_value} is in the list')
else:
    print(f'{find_value} is not in the list')
