#F.Kruusimäe
#10.10.22
#Kilpkonna liikumise harjutamine
import turtle


#tekitan akna ja lisan muutujasse
aken = turtle.Screen()
aken.setup(300,300)
aken.title("Kilpkonna harjutus 01")

#Konna loomine
konn1 = turtle.Turtle()
konn1.color("lime")
konn1.left(0)
konn1.forward(100)

konn2 = turtle.Turtle()
konn2.color("lime")
konn2.left(45)
konn2.forward(100)

konn3 = turtle.Turtle()
konn3.color("lime")
konn3.left(90)
konn3.forward(100)

konn4 = turtle.Turtle()
konn4.color ("red")
konn4.forward(90)
konn4.left(100)

konn5 = turtle.Turtle()
konn5.color("lime")
konn5.forward(-90)
konn5.left(-100)

konn6 = turtle.Turtle()
konn6.color("lime")
konn6.forward(-100)
konn6.left(-100)

turtle.exitonclick()

