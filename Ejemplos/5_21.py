import turtle

bg=input("Ingrese el color del fondo: ")
co=input("Ingrese el color de la tortuga: ")
gr=input("Ingrese el grosor de linea: ")
gr_num=int(gr)
wn = turtle.Screen()
wn.bgcolor(bg)        # set the window background color

tess = turtle.Turtle()
tess.color(co)              # make tess blue
tess.pensize(gr_num)                 # set the width of her pen

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()                # wait for a user click on the canvas
