import time


swimmer1 = "GALLANT"
swimmer2 = "GOOFUS "

minimum_temperature = 79.0  # degrees Fahrenheit
current_temperature = 0.0
saved_temperature = 0.0
swim_time = 0

current_temperature = float(input("What is the current water temperature? "))
saved_temperature = current_temperature  # saves a copy of this value so we can get it back later.

print(f"\nOkay, so the current water temperature is {current_temperature} F.")
print(f"{swimmer1} approaches the lake....")

swim_time = 0
while current_temperature >= minimum_temperature:
    print(f"\t{swimmer1} swims for a bit.", end="")
    swim_time += 1
    print(f" Swim time: {swim_time} min.")
    time.sleep(0.6)  # pauses for 600 milliseconds
    current_temperature -= 0.5  # subtracts 1/2 a degree from the water temperature
    print(f"\tThe current water temperature is now {current_temperature} F.")


print(f"{swimmer1} stops swimming. Total swim time: {swim_time} min.")

current_temperature = saved_temperature  # restores original water temperature

print(f"\nOkay, so the current water temperature is {current_temperature} F.")
print(f"{swimmer2} approaches the lake....")

swim_time = 0
while True:
    print("\t" + swimmer2 + " swims for a bit.", end="")
    swim_time += 1
    print(f" Swim time: {swim_time} min.")
    time.sleep(0.6)
    current_temperature -= 0.5
    print(f"\tThe current water temperature is now {current_temperature} F.")
    
    if current_temperature < minimum_temperature:
        break

print(f"{swimmer2} stops swimming. Total swim time: {swim_time} min.")

# Run the program, and type in 80.5 for the current water temperature. Do Goofus and Gallant swim for the same amount of time? Put your answer in a comment.
# Yes they swim for the same amount of time.

# Run the program again, but this time enter 78 for the starting temperature. What changes?

# Does Gallant check the water temperature first, or does he just dive right in?

# What about Goofus? Does he check the water temperature first or just dive in?

# What is the difference between the first while loop and the second while loop? What do you suppose the keyword break does in the second loop?

# One of these loops is sometimes called a “pre-test loop”, and the other is called a “post-test loop”. Which one is which?

