# 1. Create a loop that will ask the user for 5 numbers. Add the numbers together, 
#    except for the negative ones. Just ignore those.

# total = 0
# count = 1

# while count <= 5:
#     num1 = int(input("Enter num:"))
#     if num1 >= 0:
#         total += num1
#     count += 1

# print(f"The total, excepts those negative number, is {total}")

# 2. Two Sportz-Ball teams, the A's and the B's face off against eachother five times in a season. 
#    Enter the scores one by one alternating between the two teams.
#    For example if the first game they played was 35-67, that means the A's won that one. It would be entered as...
#    35
#    67
#    Followed by all the other games, so for example:
#    35
#    67
#    22
#    25
#    67
#    55
#    34
#    77
#    88
#    101
#    That's five games. It looks like the B's won most of the games.
# a_wins = 0
# b_wins = 0
# game_count = 0
# game_num = 5

# while game_count < game_num:
#     print("hi, enter the scores below:")
#     a = int(input(""))
#     b = int(input(""))
#     if a > b:
#         a_wins += 1
#     elif a < b:
#         b_wins += 1
#     game_count += 1

# if a_wins > b_wins:
#     print(f"That's five games. It looks like the A's won most of the games.")
# if a_wins < b_wins:
#     print(f"That's five games. It looks like the B's won most of the games.")
# if a_wins == b_wins:
#     print(f"That's five games. It looks like its a tie")

# 3. Create a program to ask the user to enter a sentence. 
#    The program will count how many of the letter a there is.
# sentence = str(input("Enter a sentence:"))
# a_count = sentence.count("a")
# print(f"There are {a_count} a letters")

# 4. Create a program that will ask the user for a word. 
#    The program will create a new string, a copy of the original without any of the vowels.

word = input("Enter word: ")
new_string = ""
for _ in word:
    if _ != "a" and _ != "e" and _ != "i" and _ != "o" and _ != "u":
        new_string += _

print(new_string)