import turtle
turtle. shape ('turtle')
square = turtle.clone()
square.shape('square')
square.penup()
square.goto(100, 100)
square.pendown()
square.goto(100, 200)
square.goto(200,200)
square.goto(200,100)
square.goto(100, 100)

triangle = turtle.clone()
triangle.shape('turtle')
triangle.shape('triangle')

triangle.goto(-150, 150)
triangle.goto(300, 150)
triangle.goto(0, 0)
square.penup()
square.goto(100,-200)


UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
direction = UP
UP_ARROW ="Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
SPACEBR = "space"

UP = 0
direction = up
