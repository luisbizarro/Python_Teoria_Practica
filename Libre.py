import turtle
turtle.setup(400,500)
turtle.bgcolor("blue")
turtle.color("white")
turtle.speed(0)
turtle.width(6)

for i in range(110):
    turtle.forward(i * 5)
    turtle.right(90)
    
turtle.Screen().exitonclick()