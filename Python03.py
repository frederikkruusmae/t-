#F.Kruusimäe
#10.10.22
#Kilpkonn
import turtle

konn1 = turtle.Turtle()


aken = turtle.Screen()
aken.setup(300,300)
aken.title("Kilpkonna harjutus 03")
konn1.speed(10)

for i in range (2):
    konn1.left(90)
    konn1.forward(80)
    konn1.left(90)
    konn1.forward(25)
    konn1.left(90)
    konn1.forward(80)
    konn1.left(90)
    konn1.forward(125)
    konn1.left(90)
    konn1.forward(25)
    konn1.left(90)
    konn1.forward(100)
    konn1.left(90)
    konn1.forward(25)
    konn1.right(90)
    
turtle.exitonclick()
