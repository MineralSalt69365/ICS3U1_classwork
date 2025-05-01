# 1. Create a function called say_ouch. When you call it
#    it prints out "ouch!". Call it three times.

# def say_ouch():
#     print("ouch!")

# say_ouch()

# 2. Create a function that takes a number and prints out that
#    number to the power of itself.

# def number(num):
#     print(num**num)

# number(1)

# 3. Create a function that takes a start and an end number
#    it will print out all numbers from start to (including) end

# def number(start, end):
#     for i in range(start, end+1):
#         print(i)

# number(1, 10)

# 4. Create a function that takes two numbers. It RETURNS the sum.

# def math(num1, num2):
#     print(num1 + num2)
# math(1,3)

# 5. Create a function that takes two numbers start and end and returns
#    a list of numbers from start to (not including) end. while loop only.

# def another_number(start2, end2):
#     count = start2
#     while start2 < end2:
#         print(start2)
#         start2 += 1
# another_number(2,10)

# 6. Modify #5 to take a third argument for how much to count up by.
#    Call this function kinda_range. while loop only.

def another_number(start3, end3, step3):
    while start3 < end3:
        print(start3)
        start3 += step3
another_number(2,10,2)

# 7. Create a function that takes a list and a target number. The function
#    will search for the target number in the list and return the index
#    where the target was located. Return -1 if not found.

def find(list, target_num):
    have = None
    for location, i in enumerate(list):
        if i == target_num:
            print(f"The number {target_num} is at index {location}")
            have = True
            break
        else:
            continue
    if have == None:
        print(-1)
        print("There is no number you want in this list")
a_list = [66, 23, 90, -5, 329, 22, 6]

find(a_list, 100)