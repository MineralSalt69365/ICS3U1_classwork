team_a_points = 25
team_a_wins = 15

team_b_points = 20
team_b_wins = 16

if team_a_points > team_b_points:
    print("Team A wins!")
    team_a_wins += 1
elif team_b_points > team_a_points:
    print("Team B wins!")
    team_b_wins += 1
else:
    print("Tie.")

if team_a_wins > team_b_wins:
    print("Team A has more wins than Team B.")
elif team_b_wins > team_a_wins:
    print("Team B has more wins than Team A.")
else:
    print("Both Teams A and B have the same number of wins.")
    
#1. That's because the first if statment add 1 to team_a_wins becasue they have more point, now their wins are equal.
#2. Elif and Else are the condition other than "if", so computer can make different response based on different situation.
#3. Consider if statement as a paragraph, elif are the sub paragraph within it, if you change elif to if, its like you are taking it out of the paragraph, so it will print our "tie" becasue it is a condition that is other than team_b_points larger than team_a_point
