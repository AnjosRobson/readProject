from turtle import *
bgcolor('black')
speed(0)
hideturtle()

for i in range(240):
    color('red')
    circle(i)
    color('orange')
    circle(i*0.8)
    left(-3)
    forward(3)
done()
