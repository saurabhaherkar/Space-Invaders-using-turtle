import turtle
import math

# Set up the Screen
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Space Invaders')

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)
player.setposition(0, -250)
player.left(90)

player_speed = 15

# Create the enemy turtle
enemy = turtle.Turtle()
enemy.color('red')
enemy.shape('circle')
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, -200)

enemy_speed = 2

# Create the player bullet
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bullet_speed = 20

# Define bullet state
# ready - ready to fire
# fire - bullet is firing
bullet_state = 'ready'


# Move the player left and right
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    # Declare bullet_state as a global if it needs changes
    global bullet_state
    if bullet_state == 'ready':
        bullet_state = 'fire'
        # Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


# Create keyboard binding
turtle.listen()
turtle.onkey(move_left, 'Left')
turtle.onkey(move_right, 'Right')
turtle.onkey(fire_bullet, 'space')

# Main game loop
while True:
    # Move the enemy
    x = enemy.xcor()
    x += enemy_speed
    enemy.setx(x)

    # Move the enemy back and down
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemy_speed *= -1
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)
        enemy_speed *= -1

    # Move the bullet
    if bullet_state == 'fire':
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # Check to see if the bullet has gone to the top
    if bullet.ycor() > 280:
        bullet.hideturtle()
        bullet_state = 'ready'

    # Check for the collision between the bullet and the enemy
    if isCollision(bullet, enemy):
        # Reset the bullet
        bullet.hideturtle()
        bullet_state = 'ready'
        bullet.setposition(0, -400)
        # Reset the enemy
        enemy.setposition(-200, 250)

    # Check for the collision between the enemy and the player
    if isCollision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print('Game Over')
        break

turtle.done()
delay = input('Press enter to finish')