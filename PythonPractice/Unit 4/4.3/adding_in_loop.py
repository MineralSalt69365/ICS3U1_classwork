print("I will add up the numbers you give me. Type 0 to tell me you want to stop")
num = int(input("Number:"))
total = 0
while num != 0:
    total += num
    print(f"The total so far is {total}")
    num = int(input("Number:"))


print(f"The total is {total}")

