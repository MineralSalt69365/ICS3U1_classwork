mark = 0
consent = input("Are you ready for a quiz?")
if consent == "yes":
    print("Okay, here it comes!")
    print()
    Q1 = input("Q1) What is the capital of Alaska?\n1) Melbourne\n2) Anchorage\n3) Juneau\n")
    if Q1 == "3":
        print("That is correct!")
        mark += 1
    else:
        print("No, the answer is 3")
    
    Q2 = input("Q2) In Python, the way you get keyboard input is the keyobard_input function.\n1) true\n2) false\n")
    if Q2 == "1":
        print("Correct!")
        mark += 1
    else:
      print("no")  
    
    Q3 = input("Q3) What is the result of 9 + 6 / 3?\n1) 5\n2) 11\n3) 15/3\n")
    if Q3 == "2":
        print("Correct!")
        mark += 1
    else:
      print("no")
    
    print(f"You got {int((mark/3)*100)}%!!!")
else:
    False