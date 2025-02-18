# Hello.  What is your name? Percy Bysshe Shelley

# Hi, Percy Bysshe Shelley!  How old are you? 34

# Did you know that in five years you will be 39 years old?
# And five years ago you were 29! Imagine that!
name = input("Hello.  What is your name?")
age = int(input(f"Hi, {name}!  How old are you?"))
older_age = age + 5
younger_age = age - 5
print(f"Did you know that in five years you will be {older_age} years old?")
print(f"And five years ago you were {younger_age}! Imagine that!")