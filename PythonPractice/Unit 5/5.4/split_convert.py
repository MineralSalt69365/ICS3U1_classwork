#1
animal_string = "monkey bat cat dog"
animal_list = animal_string.split()

for i in animal_list:
    print(i)

#2
num_string = "65, 75, 32, 22"
num_list = []

for location, num in enumerate(num_string.split(", ")):
    num_list.append(int(num))
    print(f"{location}: {num}")

#3
numbers = "one,two,three,four"
numbers_list = []

for x in numbers.split(","):
    if x.lower() == "one":
        x = 1
    elif x.lower() == "two":
        x = 2
    elif x.lower() == "three":
        x = 3
    elif x.lower() == "four":
        x = 4
    elif x.lower() == "five":
        x = 5
    numbers_list.append(x)

print(numbers_list)

#4
wins_loses = "W W L T T W"
record_list = []

for y in wins_loses.split():
    if y.lower() == "w":
        y = 2
    elif y.lower() == "t":
        y = 1
    elif y.lower() == "l":
        y = 0

    record_list.append(y)

print(record_list)

#5
data = "x:3,x:6,x:14,x:22"
print(data)

data2 = data.split(",")

x_position = []
for a in data2:
    number = int(data2.split(":")[1])
    x_position.append(number)

print(x_position)

#6
location = "x:2,y:5 - x:5,y:11 - x:7,y:14"

each_location = location.split("-")
x_y_position = []


for b in each_location:
    parts = each_location.split("")
    x = int(parts[0].split(":")[1])
    y = int(parts[1].split(":")[1])
    x_y_position.append([x, y])

print(x_y_position)
