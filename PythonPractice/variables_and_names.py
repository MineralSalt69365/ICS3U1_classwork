team = "Toronto Blue Jays"
current_date = "July 18, 2021"
player = "Vladimir Guerrero Jr."
#Each text is being stored in assigned variables
home_runs_to_date = 31
games_played = 88
total_season_games = 162
home_run_record = 73
# Numbers are stored in each assigned varirables

#the space provided is to make the code clearer, making it easy to read
games_remaining = total_season_games - games_played #162-88 = 74
home_runs_per_game = home_runs_to_date / games_played #31/88 = 0.3522727272727273
projected_home_runs = home_runs_per_game * total_season_games # 0.3522727272727273*162
can_break_record = projected_home_runs > home_run_record
#calculations that use exsisting value stored in variables

print(f"{player} of the {team}")
print(f"currently has {home_runs_to_date} home runs as of {current_date}.")
print(f"The current MLB record for most home runs in a season is {home_run_record}.")
print(f"With {games_remaining} games remaining and an average of {round(home_runs_per_game)} home runs per game,")
print(f"it is {can_break_record} that he is on pace to break the record.")
print(f"{player} is projected to hit {round(projected_home_runs)} home runs this season.")

########
# "games_remaining = total_season_games - games_played" must be correct because the sum of the game that remains and game that is played is equal to the total numer of the game