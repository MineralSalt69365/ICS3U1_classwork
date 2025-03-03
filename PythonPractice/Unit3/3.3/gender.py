gender = input("What is your gender?(m or f):")
first_name = input("Your First Name:")
last_name = input("Your Last Name:")
age = int(input("Age:"))
print()
marriage = input(f"Are you married, {first_name} (y or n)?")

if gender == "f":
    if age >= 20:
        if marriage == "y":
            print(f"Then I shall call you Mrs. {last_name}")
        else:
            print(f"Then I shall call you Mr. {last_name}")
    elif age < 20:
        print(f"Then I shall call you Ms. {last_name}")
elif gender == "m":
    if age >= 20:
        print(f"Then I shall call you Mr. {last_name}")
    else:
        print(f"Then I shall call you {first_name} {last_name}")
