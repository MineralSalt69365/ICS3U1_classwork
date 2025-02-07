print("I have a class of 33 students.")
print("There are 11 girls, so that means..")
print(f"there are " + {33 - 11} + " boys.")
#substraction
print()
print(f"That means {(round((11/33)*100))} % are girls...")
#division
print(f"and {(round((22 / 33)*100))} % are boys.")
# substraction(first) & division
print()
print("If we made groups of six...")
print(f"There would be {33 // 6} groups of six.")
#floor division, where it rounds down the result to the nearest integer less than or equal to the division result.
print(f"And then a smaller group of {33 % 6} people.")
#modulus, it gives the remainder after a division
print("-" * 30)
#multiplication, the character "-" is being multiplied by 30 times
print("If we had 17 apples and 3 people...")
print(f"Each person would get {17 // 3} whole apples.")
#floor division
print(f"There would be " + {17 % 3} + " apples remaining.")
#modulus
print()
print("If we charged each person $2 each for their 5 apples..")
print(f"they would each pay ${2*5}.")
#multiplicaiton