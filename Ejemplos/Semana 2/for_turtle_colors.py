import turtle            # set up alex
wn = turtle.Screen()
wn.bgcolor("black")
alex = turtle.Turtle()

for aColor in ["yellow", "red", "purple", "blue"]:
    alex.color(aColor)
    alex.forward(50)
    alex.left(90)

wn.exitonclick()