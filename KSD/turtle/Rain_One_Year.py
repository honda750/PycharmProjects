"""
    Rain one year in Bergen
"""
import turtle

def setupTurtle():
    myTurtleInside =  turtle.Turtle()
    myTurtleInside.pensize(2.5)
    myTurtleInside.speed(100)
    return myTurtleInside

def pulse(high, width):
    myTurtle.left((90))
    myTurtle.forward(high/10)
    myTurtle.right(90)
    myTurtle.forward(width)
    myTurtle.right(90)
    myTurtle.forward(high/10)
    myTurtle.left(90)
    myTurtle.forward(width)

def pos(x, y):
    myTurtle.penup()
    myTurtle.setpos(x, y)
    myTurtle.pendown()

def color(color):
    myTurtle.color(color)

rainQuantity =[260,240,200,150,100,130,160,190,220,240,260,270]
month = ['Jan', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Des']

myTurtle = setupTurtle()

# Write heading
pos(-190,200)
color('brown')
myTurtle.write('Rain one year in Bergen', font=("Copperplate", 30, "normal"))

# Write total quantity
pos(-140,170)
color('black')
myTurtle.write('Total  Quantity Of Rain =', font=("Ariel", 20, "normal"))
pos(80,170)
color('black')
myTurtle.write(sum(rainQuantity[:]), font=("Ariel", 20, "normal"))

# Draw diagram for rain quantity
pos(-300, -200)
color('blue')
for rain in rainQuantity:
    pulse(rain,25)

# Write the months
pos(-295, -220)
color('black')
for name in month:
    myTurtle.write(name,font=("Arial", 12, "normal"))
    myTurtle.penup()
    myTurtle.forward(50)
    myTurtle.pendown()

turtle.done()
