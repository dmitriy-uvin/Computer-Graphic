import turtle as tr
import random as r

colors = [
    ["#0eb017", "#cd090b"],
    ["#0eb017", "#f4a405", "#52176b"],
    ["#0eb017", "#07a0bc", "#7cbd14"],
    ["#0eb017", "#e2410a", "#86124f"],
    ["#0eb017", "#febe04", "#cd090b", "#00346d"],
    ["#0eb017", "#f4a405", "#cd090b", "#00346d"]
]

screen = tr.Screen()
screen.screensize(800, 600)

figure = tr.Turtle()
figure.speed(5)
figure.width(5)

startCoord = [
    {"x":  0, "y":  40, "angle":  45},
    {"x":  0, "y": -40, "angle": 315},
    {"x":  5, "y":   0, "angle": 315},
    {"x": -5, "y":   0, "angle": 225}
]
figure.color(r.choice(r.choice(colors)))

for i in range(len(startCoord)):
    figure.penup()
    figure.goto(startCoord[i]['x'], startCoord[i]['y'])
    figure.right(startCoord[i]['angle'])
    figure.pendown()
    figure.forward(200)
    if i % 2 == 0:
        figure.right(90)
        figure.forward(200)
        figure.right(90)
        figure.forward(200)
        figure.right(90)
        figure.forward(200)
        figure.right(45)
    else:
        figure.left(90)
        figure.forward(200)
        figure.left(90)
        figure.forward(200)
        figure.left(90)
        figure.forward(200)
        figure.left(45)

    figure.penup()
    figure.home()

tr.done()
