from turtle import *
width(5)
#house
color('blue')
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()
penup()
goto(200,200)
pendown()



#roof
color('red')
begin_fill()
left(90)
left(180)
right(45)
forward(141)
left(90)
forward(141)
end_fill()

left(45)
penup()
goto(80,0)
pendown()
left(180)

#door
color('purple')
begin_fill()
forward(80)
right(90)
forward(40)
right(90)
forward(80)
end_fill()


penup()
goto(20,180)
pendown()



#window1
color('yellow')
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()


penup()
goto(180,180)
pendown()

#window2
color('yellow')
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

exitonclick()
