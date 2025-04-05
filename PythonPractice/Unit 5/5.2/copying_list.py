import random

list1 = []
list2 = []

for i in range(10):
    list1.append(random.randrange(1,101))

for a in range(len(list1)):
    list2.append(list1[a])

list1[-1] = -7

print("list1:", list1)
print("list2:", list2)

