from turtle import Turtle, Screen
from random import randint

race_is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
turtles = ["red", "orange", "yellow", "green", "blue", "purple"]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
if user_bet:
    race_is_on = True
for i in range(0,6):
    turtles[i] = Turtle("turtle")
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(-230 ,(-50+(i*30)))

while race_is_on:
    for i in range(0,6):
        turtles[i].forward(randint(0, 10))
        if turtles[i].xcor() >= 230:
            race_is_on = False
            winner = turtles[i].pencolor()
            break

if winner == user_bet.lower():
    print(f"You won, the winner is {winner}")
else:
    print(f"You lost, the winner is {winner}")





screen.exitonclick()