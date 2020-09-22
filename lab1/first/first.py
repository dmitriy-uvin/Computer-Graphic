import turtle as tr

screen = tr.Screen()
screen.setup(800, 600)
firstWin = tr.Turtle()

firstWin.color("green", "white")

firstWin.speed(10)
firstWin.penup()

for i in range(1, 120, 20):
    if i != 1:
        firstWin.goto(0, -150)
        firstWin.right(90)
        firstWin.forward(i)
        firstWin.right(270)
        firstWin.pendown()
        firstWin.forward(i)
        firstWin.left(90)
        firstWin.forward(2*i)
        firstWin.left(90)
        firstWin.forward(2*i)
        firstWin.left(90)
        firstWin.forward(2*i)
        firstWin.left(90)
        firstWin.forward(i)
        firstWin.penup()
        firstWin.goto(0, -150)

firstWin.color("red", "black")
firstWin.penup()

for i in range(1, 140, 20):
    if i > 40:
        firstWin.goto(0, 150)
        firstWin.right(90)
        firstWin.forward(i)
        firstWin.right(270)
        firstWin.pendown()
        firstWin.circle(i)
        firstWin.penup()
        firstWin.home()

tr.done()
