print("TWO QUESTIONS!\nThink of an object, and I'll try to guess it")

category = input("Question 1) Is it animal, vegetable, or mineral?\n")

if category == "animal":
    size1 = input("Question 2) Is it bigger than a breadbox?")
    if size1 == "yes":
        print("You're thinking of a moose!")
    elif size1 == "no":
        print("You're thinking of a squirrel!")
elif category == "vegetable":
    size2 = input("Question 2) Is it bigger than a breadbox?")
    if size2 == "yes":
        print("You're thinking of a watermelon!")
    elif size2 == "no":
        print("You're thinking of a carrot!")
elif category == "mineral":
    size3 = input("Question 2) Is it bigger than a breadbox?")
    if size3 == "yes":
        print("You're thinking of a camero!")
    elif size3 == "no":
        print("You're thinking of a paper clip]!")
