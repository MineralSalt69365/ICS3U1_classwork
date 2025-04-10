# #1
# number_list = []
# while True:
#     user = input("please enter number:")
#     if user == "stop":
#         break
#     number_list.append(int(user) )

# print(number_list)


#2
# list = [1, -5, 90, 73, -88, 99]

# for a in range(len(list)):  
#     if list[a] < 0:
#         list[a] = abs(list[a])

# print(list)

#3
# list = [1, -5, 90, 73, -88, 99]
# new_list = []
# for i in list:
#     if i < 0:
#         new_list.append(abs(i))
#     else:
#         new_list.append(i)

# print(new_list)


#4
list = [1, -5, 90, 73, -88, 99, 101, ]
positive = []
negative = []

for b in list:
    if b < 0:
        negative.append(b)
    else:
        positive.append(b)

print(positive)
print(negative)

#5
for c in positive:
    if c > 100:
        positive.remove(c)
print(positive)

#6 
for d in positive:
    if d > 100:
        positive.remove(d)
        positive.append(0)
print(positive)
