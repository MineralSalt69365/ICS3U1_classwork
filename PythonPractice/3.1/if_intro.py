robot_location = 30
ball_location = 35
goal_location = 20
have_ball = False

if robot_location < ball_location:
    print("Almost at the ball")

if robot_location > goal_location:
    print("You are beyond the goal.")

if robot_location == goal_location:
    print("The robot is at the goal.")

robot_location += 5

if robot_location == goal_location:
    print("At the goal.")

if robot_location == ball_location:
    print("At the ball")
    print("Picking up the ball.")
    have_ball = True
    print("Now make your way to the goal.")

robot_location -= 15

if robot_location < goal_location:
    print("You went too far.")

if robot_location == goal_location and have_ball is True:
    print("You scored a goal!")
    have_ball = False     

##1. Function of if statement
#It allows the computer to operate based on different conditions.
##2. Purpose of indenting in the if statement
#Indentation ensure the code is enclosed by if statement. We can tell if a code is enclosed by if statement by looking at its indentation and position, make sure if it is under the if statement, and indented.
##4. What does += and -= do
#They are simplified version of x=x+1 or x=x-1, allow it to add or minus an value to its variable.