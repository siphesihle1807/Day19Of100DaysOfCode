from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(500, 400)
player_bet = screen.textinput(title="PRIDE RACE", prompt="Who will win the race? Pick a colour: ")
turtle_colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(0, 6):
    kago = Turtle(shape="turtle")
    kago.color(turtle_colours[i])
    kago.up()
    kago.goto(x=-230, y=y_positions[i])
    all_turtles.append(kago)

if player_bet:
    race_on = True

while race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == player_bet:
                print(f"You have won. The winning colour is: {winning_colour}!")

            else:
                print(f"Ooops, you lost this time. The winning colour is: {winning_colour}")


        random_distance = random.randint(0,10)
        turtle.forward(random_distance)












screen.exitonclick()