PIN = 12345

print("WELCOME TO THE BANK OF GALLO.")
entry = int(input("ENTER YOUR PIN: "))

while entry != PIN:
    print("\nINCORRECT PIN. TRY AGAIN.")
    # entry = int(input("ENTER YOUR PIN: "))


print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")



# 1. How is a while loop similar to an if statement?
# Like if statement it allows the computer to do certain things under a certain condition. 
# 2. How is a while loop different from an if statement?
# If statement execute command one time to do things under different condition. But while loop allows to execute the command over and over again until the condition is False.
# What would we have to change in our program if the PIN was stored as an integer rather than a string? For example if it was initialized as PIN = 12345.
# You will need to use int() to change user's input to integer.
# Comment out the line entry = input(...) from inside the while loop. What happens? Why?

# (Uncomment the entry = input(...) before you turn in the assignment.)