# 1. print out numbers from 1-100
# count1 = 1
# while count1 <= 100:
#     print(count1)
#     count1 += 1

# 2. Add up the numbers from 1-100, only even
# count2 = 2
# sum2 = 0
# while count2 <= 100:
#     print(count2)
#     sum2 += count2
#     count2 += 2
# print(f"The sum is {sum2}")

# 3. Add up numbers from 1-1000, only multiples of 5 and 7
# count3 = 1
# sum3 = 0
# while count3 <= 1000:
#     if count3 % 5 == 0 or count3 % 7 == 0:
#         sum3 += count3
#         print(count3)
#     count3 += 1
# print(f"The sum is {sum3}")
# 4. Present the user with two choices, "eat dinner" or "sleep",
#     if they don't respond with either, say invalid and ask again, Use a loop for this
# running = True
# while running:
#     choice = input("Do you want to Eat Dinner(a) or Sleep(b)?")
#     if choice == "a":
#         print("Ok, just get something from the fridge")
#         running = False
#     elif choice == "b":
#         print("Good Night")
#         running = False
#     else:
#         print("invalid input")

#5. Ask the user to enter numbers and display the sum of all the numbers inputted. They will enter "stop" to stop inputting numbers
ask = True
sum5 = 0
print("type 'stop' when you want to stop adding up numbers")
while ask:
    num = input("What num?")
    if num == "stop":
        ask = False
    else:
        sum5 += int(num)
print(sum5)
    
