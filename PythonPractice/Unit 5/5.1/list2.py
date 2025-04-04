import random
list = []

for i in range(10):
    list.append(random.randrange(1,101))

for a in range(len(list)):
    print(f"Slot {a} contains a {list[a]}")