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
ball.x_speed = 3  # ball movement speed in x axis
ball.y_speed = 2  # ball movement speed in y axis
ball.x_saved = 0  # for when you press the pause button it saves the previous 
ball.y_saved = 0  # velocity so it can return to moving in the exact same fashion upon unpause

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('black')
pen.penup()  #every turtle obj starts at 0,0 and when it moves there will be a line draw and we dont want that
pen.hideturtle()
pen.goto(0, 260)
player_one_score = 0
player_two_score =0
pen.write(f'player 1: {player_one_score}                                           player 2: {player_two_score}', align='center', font=('Arial',22,'normal'))

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


def pause():
    if ball.x_speed > 0 or ball.x_speed < 0:
        ball.x_saved = ball.x_speed
        ball.y_saved = ball.y_speed
        ball.x_speed = 0
        ball.y_speed = 0
    elif ball.x_speed == 0:
        ball.x_speed = ball.x_saved
        ball.y_speed = ball.y_saved
       
# keyBind

wndw.listen()
wndw.onkeypress(paddle_a_up,"w")
wndw.onkeypress(paddle_a_down,'s')
wndw.onkeypress(paddle_b_up,'Up')
wndw.onkeypress(paddle_b_down,'Down')
wndw.onkeypress(pause, 'p')



# Main game loop
while True:
    wndw.update()

    #move the ball
    ball.setx(ball.xcor() + ball.x_speed)
    ball.sety(ball.ycor() + ball.y_speed)

    # Bounce off top and bottom borders
    if ball.ycor() > 270 or ball.ycor() < -285:
        ball.y_speed *= -1

    if (ball.xcor() > 340 ) and ((paddle_b.ycor() - ball.ycor()) < 40 and (paddle_b.ycor() - ball.ycor()) > -40):
        ball.x_speed *= -1

    if (ball.xcor() < -340) and ((paddle_a.ycor() -  ball.ycor())<40 and (paddle_a.ycor()- ball.ycor()>-40)):
        ball.x_speed *= -1


    if ball.xcor() > 450:
        player_one_score += 1
        pen.clear()
        pen.write(f'player 1: {player_one_score}                                           player 2: {player_two_score}',
                  align='center', font=('Arial', 22, 'normal'))
        ball.goto(0, 0)
        ball.x_speed *= -1

    elif ball.xcor() < -450:
        player_two_score += 1
        pen.clear()
        pen.write(f'player 1: {player_one_score}                                           player 2: {player_two_score}',
                  align='center', font=('Arial', 22, 'normal'))
        ball.goto(0, 0)
        ball.x_speed *= -1
