# miniproject "Ping Pong", by: Luqi


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
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left 
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [random.randrange(3, 5), -random.randrange(1, 2)]
    if not direction:
        ball_vel[0] = - ball_vel[0] 
        

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    init_direction = random.choice([LEFT, RIGHT])
    spawn_ball(init_direction)
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # collide and reflect off of top or bottom of canvas
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1] 
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos < HALF_PAD_HEIGHT:
        paddle1_pos = HALF_PAD_HEIGHT
    elif paddle1_pos > HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    elif paddle2_pos < HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
    elif paddle2_pos > HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
    else:
        paddle1_pos += paddle1_vel
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_line((HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT), (HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT), PAD_WIDTH, 'Red')
    canvas.draw_line((WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT), (WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT), PAD_WIDTH, 'Blue')
    
    # determine whether paddle and ball collide  
    if ball_pos[0] <= HALF_PAD_WIDTH + BALL_RADIUS:
        if ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT and ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0] * 1.1
            ball_vel[1] = ball_vel[1] * 1.1
        else:
            score2 += 1
            spawn_ball(RIGHT)

           
    elif ball_pos[0] >= WIDTH - HALF_PAD_WIDTH - BALL_RADIUS:
        if ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT and ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0] * 1.1
            ball_vel[1] = ball_vel[1] * 1.1
        else:
            score1 += 1
            spawn_ball(LEFT)
            
         
    # draw scores
    canvas.draw_text(str(int(score1)), (100, 70), 60, 'Red')
    canvas.draw_text(str(int(score2)), (WIDTH - 130, 70), 60, 'Blue')
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    vel = 5
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = vel
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -vel
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = vel
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -vel 
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button('Restart', new_game, 100)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
frame.start()
