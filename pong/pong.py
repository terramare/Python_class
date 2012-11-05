# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [1, 1]
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if right == True:
        ball_vel = [(random.randrange(120, 240) // 60), - (random.randrange(60, 180) // 60)]
    if right == False:
        ball_vel = [- (random.randrange(120, 240) // 60), - (random.randrange(60, 180) // 60)]
    print ball_vel
    
# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    ball_init(True)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global HEIGHT, WIDTH, BALL_RADIUS, PAD_WIDTH, HALF_PAD_HEIGHT
    global paddle1_vel, paddle2_vel
 
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos > HALF_PAD_HEIGHT and paddle1_pos < HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    else:
        paddle1_pos -= paddle1_vel

    paddle2_pos += paddle2_vel
    
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_line([HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT],[HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    c.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT],[WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], PAD_WIDTH, "White")
     
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        ball_init(True)
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        ball_init(False)
        
    # draw ball and scores
    c.draw_circle(ball_pos, 20, 1, "White", "White")
    
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= 4
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += 4
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= 4
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += 4
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel += 4
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel -= 4
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel += 4
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel -= 4

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)


# start frame
init()
frame.start()

