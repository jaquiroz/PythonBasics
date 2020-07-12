import turtle
wn = turtle.Screen()
nikea =turtle.Turtle()
nikea.shape("turtle")
nikea.penup()
for size in range(10):
    nikea.forward(50)
    nikea.stamp()
   
wn.exitonclick()