num = int(input("Starting Number: "))
numlist = []

while num != 1:
    if num % 2 ==0:
        num = num // 2
        numlist.append(num)

    else:
        num = (num*3) + 1
        numlist.append(num)

print(*numlist)
