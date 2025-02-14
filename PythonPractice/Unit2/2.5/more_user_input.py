
# First name: Helena
# Last name: Bonham-Carter
# Grade (9-12): 12
# Student ID: 453916
# Login: bonham_453916
# Average: 75.0

# Your information:
# 	Login:     bonham_453916 
# 	ID:        453916 
# 	Name:      Bonham-Carter, Helena 
# 	Average:   75.0 %
# 	Grade:     12 
print("Welcome! To create a student account, please fill out the following information!")
first_name = input ("What is your first name?")
last_name = input ("What is your last name?")
grade = int(input(f"What grade are you in, {first_name}?"))
id = input("Please type in your student ID.")
login = input ("And your username plz.")
avg = float(input("What is your current average?"))

print("")
print("Your information:")
print(f"ID: {id}")
print(f"Name: {last_name},{first_name}")
print(f"Average: {avg}%")
print(f"Grade: {grade}")



