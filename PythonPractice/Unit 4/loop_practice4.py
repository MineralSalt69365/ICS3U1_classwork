# 1. Create a loop that will ask the user to enter positive numbers,
#    Stop asking when they enter a negative number.
#    Find the total and the average of the numbers.
# total = 0
# count = 0
# while True:
#     num1 = int(input("Please Enter A Positive Number <3 :"))
#     if num1 < 0:
#         break
#     elif num1 >= 0:
#         total += num1
#     count += 1
    
# average = total/count
# print(f"The avergage is {average}")
# 2. Ask the user for a sentence, then in a loop print out the letters
#    one-by-one. Beside each vowel, print "VOWEL". For example:
#    Enter a sentence: Hello
#    H
#    e VOWEL
#    l
#    l
#    o VOWEL
# 3. Ask the user to enter a word. Create a new string with all the 
#    leter a and e switched. Print out the result.
#    Enter a word: healthy
#    haelthy
# word = input("Enter a word babe:")
# new_word = ""
# for char in word:
#     if char == "a":
#         new_word += "e"
#     elif char == "e":
#         new_word += "a"
#     else:
#         new_word += char
# print(new_word)

# 4. (perhaps too difficult for a written test)
#    Ask the user for a string of characters. The goal is to condense
#    all the letters useing a compression algorithm. Any repeated
#    letters will be condensed with a number indicating how many times
#    the letter was repeated. For example
#    "abbcdeeeff" -> "a2bcd3e2f"
# """
character = input("Give me some radom characters baby:")
new_char = ""

for x in character:
print(x[2])