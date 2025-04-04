import random
list = []

for i in range(1000):
    list.append(random.randrange(10, 100))

for a in range(len(list)):
    print(list[a], end="  ")