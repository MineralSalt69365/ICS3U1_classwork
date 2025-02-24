weight = int(input("Please enter your current earth weight:"))
# 1	Venus	0.78
# 2	Mars	0.39
# 3	Jupiter	2.65
# 4	Saturn	1.17
# 5	Uranus	1.05
# 6	Neptune	1.23

print("I have information for the following planets:")
print("  1. Venus   2. Mars    3. Jupiter") 
print("  4. Saturn  5. Uranus  6. Neptune")

planet = int(input("Which planet are you visiting?"))

if planet == 1:
    print(f"Your weight would be {weight*0.78} pounds on that planet.")
elif planet == 2:
    print(f"Your weight would be {weight*0.39} pounds on that planet.")
elif planet == 3:
    print(f"Your weight would be {weight*2.65} pounds on that planet.")
elif planet == 4:
    print(f"Your weight would be {weight*1.17} pounds on that planet.")
elif planet == 5:
    print(f"Your weight would be {weight*1.05} pounds on that planet.")
elif planet == 6:
    print(f"Your weight would be {weight*1.23} pounds on that planet.")
else:
    print("what")