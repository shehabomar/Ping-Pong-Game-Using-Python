# Imported Modules
import turtle

# Customising the settings of the Screen
wind = turtle.Screen() # intialize screen
wind.title("Ping Pong Game") 
wind.bgcolor("black") # set bckground color
wind.setup(width=800,height=600) # set dimensions of the window
wind.tracer(7) # stop window from updating auto

    
# Racket 1 
racket1 = turtle.Turtle() # intialize turtle object 
racket1.speed(0) # set the speed of the animation
racket1.shape("square") # set the shape of the object 
racket1.color("blue") # set the color of the object 
racket1.penup() # set the object from drawing lines
racket1.goto(-350,0)# set the pos
racket1.shapesize(stretch_wid=5,stretch_len=1)# stretch the shape

# Racket 2
racket2 = turtle.Turtle()
racket2.speed(0)
racket2.shape("square")
racket2.color("red")
racket2.penup()
racket2.goto(350,0)
racket2.shapesize(stretch_wid=5,stretch_len=1)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2.1
ball.dy = 2.1
ball.setheading(90)
ball.forward(30)


# Scoring
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle() 
score.goto(0,260)
score.write("Player 1: 0 Player 2: 0", align="center",font =("Courier",24,"normal"))

#Movment Functions
def racket1_up():
    y = racket1.ycor()
    y += 20
    racket1.sety(y)

def racket1_down():
    y = racket1.ycor()
    y -= 20
    racket1.sety(y)

def racket2_up():
    y = racket2.ycor()
    y += 20
    racket2.sety(y)
    
def racket2_down():
    y = racket2.ycor()
    y -= 20
    racket2.sety(y)

# keyboard bindings
wind.listen() # Inform the window that there will be a movement 
wind.onkeypress(racket1_up,"w") 
wind.onkeypress(racket1_down,"s")
wind.onkeypress(racket2_up,"Up")
wind.onkeypress(racket2_down,"Down")


# The game loop
while True:
    wind.update() # update the screen 
    
    # ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy) 

    # Border Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
   
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
  
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
          
    # Collision of ball with both rackets
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < racket2.ycor() + 41 and ball.ycor() > racket2.ycor() - 41):
        score2+=1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(score1,score2), align="center",font =("Courier",24,"normal"))
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() >  -350) and (ball.ycor() < racket1.ycor() +41 and ball.ycor() > racket1.ycor() - 41):
        ball.setx(-340)
        ball.dx *= -1
        score1+=1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(score1,score2), align="center",font =("Courier",24,"normal"))
    
    if (score1 == 10 and score1 > socre2):
        score.clear()
        score.write("Player 1 Won!", align="center",font =("Courier",24,"normal"))
        wind.bye() 
    elif  (score2 == 10 and score2 > score1) :
        score.clear()
        score.write("Player 2 Won!", align="center",font =("Courier",24,"normal"))
        wind.bye()
    # Call update function after a specific delay
    wind.ontimer(wind.update(), 10)

# Run the turtle main loop
turtle.mainloop()
