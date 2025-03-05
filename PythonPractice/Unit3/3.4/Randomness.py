#1. What happens if we change random.randrange(1, 6) to random.randrange(1, 5)? Make the change and run the program a few times to see the result. What seems to be the new range of numbers that pop up?
#The new range is going to be from 1 to 4 instead of from 1 to 5.
#2. After the import statement, use the random.seed() function and give it an integer like random.seed(400). What do you notice? What happened to the random numbers?
#The computer outputs a definite random number, so the result does not change.
#3. Change the random seed to something else and observe the behavior. What happens to the random numbers?
# The result will be different, but if you repeat it multiple times, it keeps outputting the same results.
#4. There are a couple popular games I can think of that use this concept of a “seed”. Why do you suppose they use it, and what does it do in the game
# In a game, random.seed() function can be useful because it can recreate the same thing when you want while it also saves a lot of data from building maps in a game.
