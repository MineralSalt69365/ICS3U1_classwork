# print("Type in a message, and I'll display it ten times.")

# message = input("Message: ")
# print()

# n = 10
# while n <= 100:
#     print(f"{n}. {message}")
#     n += 10

# 1. What does n += 1 do? Remove it and see what happens. (Then put it back.) ctrl + c may come in handy.
# It allows n increase everytime by 1. If u stop it, it is gonna be unstopable becasue n will never reach 5 and over.

#4
print("Type in a message, and I'll display it several times.")
message2 = input("Message: ")
print()
x = int(input("How many times?"))
y = 10

while y <= x*10:
    print(f"{y}. {message2}")
    y += 10