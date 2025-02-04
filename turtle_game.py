import turtle
import random
import time

wn_screen = turtle.Screen()
wn_screen.bgcolor("light blue")
wn_screen.title("Turtle Game")
FONT=("Arial", 20, "normal")

score = 0
score_turtle = turtle.Turtle()
score_turtle.color("dark blue")
score_turtle.penup()
score_turtle.setposition(0,280)
score_turtle.write(f"Score: {score}", move=False, align="center", font=FONT)
score_turtle.hideturtle()

timee = 20
time_turtle = turtle.Turtle()
time_turtle.color("black")
time_turtle.penup()
time_turtle.setposition(0,240)
time_turtle.write(f"Time: {timee}", move=False, align="center", font=FONT)
time_turtle.hideturtle()

figure_turtle = turtle.Turtle()
figure_turtle.shape("turtle")
figure_turtle.color("green")
figure_turtle.turtlesize(2)


def teleport():
    if timee > 0:
        figure_turtle.penup()
        figure_turtle.hideturtle()
        wn_screen.ontimer(show_turtle, 500)

def show_turtle():
    if timee > 0:
        figure_turtle.penup()
        x = random.randint(-270, 270)
        y = random.randint(-220, 220)
        figure_turtle.goto(x, y)
        figure_turtle.showturtle()
        wn_screen.ontimer(teleport, 700)

def score_board(x,y):
    global score
    score += 1
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", move=False, align="center", font=FONT)

def countdown():
    global timee
    if timee > 0:
        timee -= 1
        time_turtle.clear()
        time_turtle.write(f"Time: {timee}", move=False, align="center", font=FONT)
        wn_screen.ontimer(countdown, 1000)
    else:
        game_over()

def game_over():
    time_turtle.clear()
    score_turtle.clear()
    figure_turtle.hideturtle()
    time_turtle.goto(0, 0)
    time_turtle.write("GAME OVER!", align="center", font=("Arial", 30, "bold"))


figure_turtle.onclick(score_board)
teleport()
countdown()




























turtle.mainloop()






