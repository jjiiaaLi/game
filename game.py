import turtle

wndw = turtle.Screen()
wndw.title('Jack\'s first game')
wndw.bgcolor('white')
wndw.setup(width=800, height=600)
wndw.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #update speed to the fasted setting
paddle_a.shape('square')
paddle_a.color('black')
paddle_a.shapesize(stretch_wid=4, stretch_len=0.5)
paddle_a.penup()  #turtle default to drawing a line to movement and we dont want that
paddle_a.goto(-350,0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # update speed to the fasted setting
paddle_b.shape('square')
paddle_b.color('black')
paddle_b.shapesize(stretch_wid=4, stretch_len=0.5)
paddle_b.penup()  # turtle default to drawing a line to movement and we dont want that
paddle_b.goto(350, 0)


#ball
ball = turtle.Turtle()
ball.speed(0)  # update speed to the fasted setting
ball.shape('circle')
ball.color('black')
ball.penup()  # turtle default to drawing a line to movement and we dont want that
ball.goto(0, 0)
ball.x_speed = 4  #ball movement speed in x axis
ball.y_speed = 2  #ball movement speed in y axis

# Move paddle functions
def paddle_a_up():
    current_y_coord = paddle_a.ycor()
    current_y_coord += 10
    paddle_a.sety(current_y_coord)

def paddle_a_down():
    current_y_coord = paddle_a.ycor()
    current_y_coord -= 10
    paddle_a.sety(current_y_coord)


def paddle_b_up():
    current_y_coord = paddle_b.ycor()
    current_y_coord += 10
    paddle_b.sety(current_y_coord)


def paddle_b_down():
    current_y_coord = paddle_b.ycor()
    current_y_coord -= 10
    paddle_b.sety(current_y_coord)

# keyBind

wndw.listen()
wndw.onkeypress(paddle_a_up,"w")
wndw.onkeypress(paddle_a_down,'s')
wndw.onkeypress(paddle_b_up,'Up')
wndw.onkeypress(paddle_b_down,'Down')



# Main game loop
while True:
    wndw.update()

    #move the ball
    ball.setx(ball.xcor() + ball.x_speed)
    ball.sety(ball.ycor() + ball.y_speed)

    # Bounce off top and bottom borders
    if ball.ycor() > 290 or ball.ycor() < -285:
        ball.y_speed *= -1

    if (ball.xcor() > 340 ) and ((paddle_b.ycor() - ball.ycor()) < 40 and (paddle_b.ycor() - ball.ycor()) > -40):
        ball.x_speed *= -1

    if (ball.xcor() < -340) and ((paddle_a.ycor() -  ball.ycor())<40 and (paddle_a.ycor()- ball.ycor()>-40)):
        ball.x_speed *= -1

    if ball.xcor() > 400 or ball.xcor() < -400:
        ball.goto(0,0)
        ball.x_speed *= -1
