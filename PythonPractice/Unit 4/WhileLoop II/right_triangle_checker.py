print("ENTER THREE INTEGER:")

int1 = int(input("Side 1:"))
int2 = int(input("Side 2:"))

running = True
while int2 < int1:
    
    print(f"{int2} is smaller than {int1}")
    int2 = int(input("Side 2:"))

int3 = int(input("Side 3:"))

while int3 < int2:
    
    print(f"{int3} is smaller than {int2}")
    int3 = int(input("Side 3:"))

if int1**2 + int2**2 == int3**2 or int2**2 + int3**2 == int1**2 or int1**2 + int3**2 == int2**2:
    print(f"Your three side are {int1} {int2} {int3}")
    print("These sides *do* make a right triangle.  Yippy-skippy!")
else:
    print(f"Your three side are {int1} {int2} {int3}")
    print("NO!  These sides do not make a right triangle!")