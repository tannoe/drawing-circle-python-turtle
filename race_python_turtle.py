import turtle
import random, time

player1 = turtle.Turtle()
player1.shape("turtle")
player1.penup()
player1.goto(10,20)
player1.pendown()
player1.color('blue')
player1.write('Player 1')
player2 = turtle.Turtle()
player2.shape("turtle")
player2.penup()
player2.goto(10,80)
player2.pendown()
player2.color('green')
player2.write('Player 2')

start1 = 0 
start2 = 0
end = 100
# creating end circle for player1
endTurtle1 = turtle.Turtle()
endTurtle1.penup()
# creating end circle for player 1 position
endTurtle1.goto(200,20)
endTurtle1.pendown()
# creating circle
endTurtle1.shape('circle')
endTurtle1.fillcolor('white')

endTurtle2 = turtle.Turtle()
endTurtle2.penup()
endTurtle2.goto(200,80)
endTurtle2.pendown()
endTurtle2.shape('circle')
endTurtle2.fillcolor('white')

wn = turtle.Screen()
# running while loop until the start
# position for any player is less than end position
while start1<=end or start2<=end:
    if start1>=end:
        wn.title(f"Player1 position is {start1}, Player2 position is {start2}, Player1 wins")
        time.sleep(5)
        break
    elif start2>=end:
        wn.title(f"Player1 position is {start1}, Player2 position is {start2}, Player2 wins")
        time.sleep(5)
        break

# dice
dice1 = random.randrange(1,6)
dice2 = random.randrange(1,6)
# forwading
player1.forward(dice1*2)
time.sleep(1)

player2.forward(dice2*2)
time.sleep(1)
# increasing position value
start1 += dice1*2
start2 += dice2*2
wn.title(f"Player1 position is {start1},Player2 position is {start2}, no one wins")
time.sleep(3)
turtle.bye()