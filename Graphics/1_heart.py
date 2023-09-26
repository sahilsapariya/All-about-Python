from turtle import *

t = Turtle()

t.begin_fill()
t.fillcolor('red')

t.setheading(135)
t.forward(100)
t.circle(-50, 180)

t.setheading(45)
t.circle(-50, 180)
t.forward(100)

t.end_fill()

mainloop()