# 1. calculate the sum of the numbers from 1 to 10.
count1 = 1
sum1 = 0
while count1 <= 10:
    print(count1)
    sum1 += count1
    count1 += 1
print(sum1)
# 2. calculate the sum of the numbers from 100 to 200.
count2 = 100
sum2 = 0
while count2 <= 200:
    print(count2)
    sum2 += count2
    count2 += 1
print(sum2)
# 3. calculate the difference between the sum of the numbers from 100 to 200 and the sum of the numbers from 200 to 300.
count31 = 100
sum31 = 0
while count31 <= 200:
    sum31 += count31
    count31 += 1
count32 = 200
sum32 = 0
while count32 <= 300:
    sum32 += count32
    count32 += 1
print(sum32 - sum31)
# 4.calculate the sum of the multiples of 5 between the numbers 1000 and 10000.
count4 = 1000
sum4 = 0
while count4 <= 10000:
    sum4 += count4
    count4 += 5
print(sum4)
# calculate the sum of the multiples of 5 between 1 and 100, but do not include numbers that are multiples of 3. Modulus (%) will come in handy here.
count5 = 5
sum5 = 0
while count5 <= 100:
    print(count5)
    if count5 % 3 != 0:
        sum5 += count5
    count5 += 5
print(sum5)
