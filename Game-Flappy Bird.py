# miniproject Flappy Bird - by: Luqi

import simplegui
import random

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 10
pipe_width= 20
pipe_distance= 150
ball_pos = [WIDTH / 2, HEIGHT / 2]
vel_ball = [0, 0]  # pixels per tick
vel_pipe = [0, 0]  # pixels per tick
time = 0
score = 0
word = ''
contro_vel = 0


distance1 = 0
upper_y1 = 0
lower_y1 = 0
distance2 = 0
upper_y2 = 0
lower_y2 = 0
distance3 = 0
upper_y3 = 0
lower_y3 = 0
distance4 = 0
upper_y4 = 0
lower_y4 = 0

# initialize pipe position
UpperPipe_pos1_1 = [0, 0]
UpperPipe_pos1_2 = [0, 0]
LowerPipe_pos1_1 = [0, 0]
LowerPipe_pos1_2 = [0, 0]
UpperPipe_pos2_1 = [0, 0]
UpperPipe_pos2_2 = [0, 0]
LowerPipe_pos2_1 = [0, 0]
LowerPipe_pos2_2 = [0, 0]
UpperPipe_pos3_1 = [0, 0]
UpperPipe_pos3_2 = [0, 0]
LowerPipe_pos3_1 = [0, 0]
LowerPipe_pos3_2 = [0, 0]
UpperPipe_pos4_1 = [0, 0]
UpperPipe_pos4_2 = [0, 0]
LowerPipe_pos4_1 = [0, 0]
LowerPipe_pos4_2 = [0, 0]
  

# define event handlers
def tick():
    global time
    time = time + 1 
    
def new_game():
    global ball_pos, vel_ball, vel_pipe, score, word, contro_vel
    global distance1, distance2, distance3, distance4
    global upper_y1, upper_y2, upper_y3, upper_y4, lower_y1, lower_y2, lower_y3, lower_y4
    global UpperPipe_pos1_1, UpperPipe_pos1_2, UpperPipe_pos2_1, UpperPipe_pos2_2, UpperPipe_pos3_1, UpperPipe_pos3_2, UpperPipe_pos4_1, UpperPipe_pos4_2
    global LowerPipe_pos1_1, LowerPipe_pos1_2, LowerPipe_pos2_1, LowerPipe_pos2_2, LowerPipe_pos3_1, LowerPipe_pos3_2, LowerPipe_pos4_1, LowerPipe_pos4_2
    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    vel_ball = [0, 1]  # pixels per tick
    vel_pipe = [1, 0]  # pixels per tick
    score = 0
    word = ''
    contro_vel = 30
    distance1 = random.randrange(80, 140)
    upper_y1 = random.randrange(10, 250)
    lower_y1 = upper_y1 + distance1
    distance2 = random.randrange(80, 140)
    upper_y2 = random.randrange(10, 250)
    lower_y2 = upper_y2 + distance2
    distance3 = random.randrange(80, 140)
    upper_y3 = random.randrange(10, 250)
    lower_y3 = upper_y3 + distance3
    distance4 = random.randrange(80, 140)
    upper_y4 = random.randrange(10, 250)
    lower_y4 = upper_y4 + distance4
    # initialize pipe position
    UpperPipe_pos1_1 = [0, 0]
    UpperPipe_pos1_2 = [0, upper_y1]
    LowerPipe_pos1_1 = [0, 400]
    LowerPipe_pos1_2 = [0, lower_y1]
    UpperPipe_pos2_1 = [pipe_distance, 0]
    UpperPipe_pos2_2 = [pipe_distance, upper_y2]
    LowerPipe_pos2_1 = [pipe_distance, 400]
    LowerPipe_pos2_2 = [pipe_distance, lower_y2]
    UpperPipe_pos3_1 = [2 * pipe_distance, 0]
    UpperPipe_pos3_2 = [2 * pipe_distance, upper_y3]
    LowerPipe_pos3_1 = [2 * pipe_distance, 400]
    LowerPipe_pos3_2 = [2 * pipe_distance, lower_y3]
    UpperPipe_pos4_1 = [3 * pipe_distance, 0]
    UpperPipe_pos4_2 = [3 * pipe_distance, upper_y4]
    LowerPipe_pos4_1 = [3 * pipe_distance, 400]
    LowerPipe_pos4_2 = [3 * pipe_distance, lower_y4]
    
    if UpperPipe_pos1_1[0] % 600 < 5:
        distance1 = random.randrange(50, 90)
        upper_y1 = random.randrange(10, 300)
        lower_y1 = upper_y1 + distance1
    elif UpperPipe_pos2_1[0] % 600 < 5:
        distance2 = random.randrange(50, 90)
        upper_y2 = random.randrange(10, 300)
        lower_y2 = upper_y2 + distance2

def draw(canvas):
    global ball_pos, vel_ball, vel_pipe, score, word, contro_vel
    global distance1, distance2, distance3, distance4
    global upper_y1, upper_y2, upper_y3, upper_y4, lower_y1, lower_y2, lower_y3, lower_y4
    global UpperPipe_pos1_1, UpperPipe_pos1_2, UpperPipe_pos2_1, UpperPipe_pos2_2, UpperPipe_pos3_1, UpperPipe_pos3_2, UpperPipe_pos4_1, UpperPipe_pos4_2
    global LowerPipe_pos1_1, LowerPipe_pos1_2, LowerPipe_pos2_1, LowerPipe_pos2_2, LowerPipe_pos3_1, LowerPipe_pos3_2, LowerPipe_pos4_1, LowerPipe_pos4_2
 
    # calculate ball position
    ball_pos[0] += vel_ball[0]
    ball_pos[1] += vel_ball[1]    
    
    # calculate pipe position
    UpperPipe_pos1_1[0] = (UpperPipe_pos1_1[0] - vel_pipe[0]) % 600
    UpperPipe_pos1_2[0] = (UpperPipe_pos1_2[0] - vel_pipe[0]) % 600
    LowerPipe_pos1_1[0] = (LowerPipe_pos1_1[0] - vel_pipe[0]) % 600
    LowerPipe_pos1_2[0] = (LowerPipe_pos1_2[0] - vel_pipe[0]) % 600    
    UpperPipe_pos2_1[0] = (UpperPipe_pos2_1[0] - vel_pipe[0]) % 600
    UpperPipe_pos2_2[0] = (UpperPipe_pos2_2[0] - vel_pipe[0]) % 600
    LowerPipe_pos2_1[0] = (LowerPipe_pos2_1[0] - vel_pipe[0]) % 600
    LowerPipe_pos2_2[0] = (LowerPipe_pos2_2[0] - vel_pipe[0]) % 600   
    UpperPipe_pos3_1[0] = (UpperPipe_pos3_1[0] - vel_pipe[0]) % 600
    UpperPipe_pos3_2[0] = (UpperPipe_pos3_2[0] - vel_pipe[0]) % 600
    LowerPipe_pos3_1[0] = (LowerPipe_pos3_1[0] - vel_pipe[0]) % 600
    LowerPipe_pos3_2[0] = (LowerPipe_pos3_2[0] - vel_pipe[0]) % 600    
    UpperPipe_pos4_1[0] = (UpperPipe_pos4_1[0] - vel_pipe[0]) % 600
    UpperPipe_pos4_2[0] = (UpperPipe_pos4_2[0] - vel_pipe[0]) % 600
    LowerPipe_pos4_1[0] = (LowerPipe_pos4_1[0] - vel_pipe[0]) % 600
    LowerPipe_pos4_2[0] = (LowerPipe_pos4_2[0] - vel_pipe[0]) % 600
       
    # calculate score
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        vel_pipe = [0, 0]
        vel_ball = [0, 0]
        contro_vel = 0
        word = 'Fail !'
    elif ball_pos[0] == UpperPipe_pos1_1[0] + pipe_width / 2 + BALL_RADIUS and (ball_pos[1] > LowerPipe_pos1_2[1] or ball_pos[1] < UpperPipe_pos1_2[1]):
        vel_pipe = [0, 0]
        vel_ball = [0, 0]
        contro_vel = 0
        word = 'Fail !'
    elif ball_pos[0] == UpperPipe_pos2_1[0] + pipe_width / 2 + BALL_RADIUS and (ball_pos[1] > LowerPipe_pos2_2[1] or ball_pos[1] < UpperPipe_pos2_2[1]):
        vel_pipe = [0, 0]
        vel_ball = [0, 0]
        contro_vel = 0
        word = 'Fail !'
    elif ball_pos[0] == UpperPipe_pos3_1[0] + pipe_width / 2 + BALL_RADIUS and (ball_pos[1] > LowerPipe_pos3_2[1] or ball_pos[1] < UpperPipe_pos3_2[1]):
        vel_pipe = [0, 0]
        vel_ball = [0, 0]
        contro_vel = 0
        word = 'Fail !'
    elif ball_pos[0] == UpperPipe_pos4_1[0] + pipe_width / 2 + BALL_RADIUS and (ball_pos[1] > LowerPipe_pos4_2[1] or ball_pos[1] < UpperPipe_pos4_2[1]):
        vel_pipe = [0, 0]
        vel_ball = [0, 0]
        contro_vel = 0
        word = 'Fail !'
    else:
        if UpperPipe_pos1_1[0] == ball_pos[0]:
            if ball_pos[1] < LowerPipe_pos1_2[1] - BALL_RADIUS and ball_pos[1] > UpperPipe_pos1_2[1] + BALL_RADIUS:
                score += 1
            else:
                vel_pipe = [0, 0]
                vel_ball = [0, 0]
                contro_vel = 0
                word = 'Fail !'
        elif UpperPipe_pos2_1[0] == ball_pos[0]:
            if ball_pos[1] < LowerPipe_pos2_2[1] - BALL_RADIUS and ball_pos[1] > UpperPipe_pos2_2[1] + BALL_RADIUS:
                score += 1
            else:
                vel_pipe = [0, 0]
                vel_ball = [0, 0]
                contro_vel = 0
                word = 'Fail !'
        elif UpperPipe_pos3_1[0] == ball_pos[0]:
            if ball_pos[1] < LowerPipe_pos3_2[1] - BALL_RADIUS and ball_pos[1] > UpperPipe_pos3_2[1] + BALL_RADIUS:
                score += 1
            else:
                vel_pipe = [0, 0]
                vel_ball = [0, 0]
                contro_vel = 0
                word = 'Fail !'
        elif UpperPipe_pos4_1[0] == ball_pos[0]:
            if ball_pos[1] < LowerPipe_pos4_2[1] - BALL_RADIUS and ball_pos[1] > UpperPipe_pos4_2[1] + BALL_RADIUS:
                score += 1
            else:
                vel_pipe = [0, 0]
                vel_ball = [0, 0]
                contro_vel = 0
                word = 'Fail !'
                
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 7, "Purple", "Pink")
    # draw pipe
    canvas.draw_line(UpperPipe_pos1_1, UpperPipe_pos1_2, pipe_width, 'Orange')
    canvas.draw_line(LowerPipe_pos1_1, LowerPipe_pos1_2, pipe_width, 'Orange')
    canvas.draw_line(UpperPipe_pos2_1, UpperPipe_pos2_2, pipe_width, 'Orange')
    canvas.draw_line(LowerPipe_pos2_1, LowerPipe_pos2_2, pipe_width, 'Orange')
    canvas.draw_line(UpperPipe_pos3_1, UpperPipe_pos3_2, pipe_width, 'Orange')
    canvas.draw_line(LowerPipe_pos3_1, LowerPipe_pos3_2, pipe_width, 'Orange')
    canvas.draw_line(UpperPipe_pos4_1, UpperPipe_pos4_2, pipe_width, 'Orange')
    canvas.draw_line(LowerPipe_pos4_1, LowerPipe_pos4_2, pipe_width, 'Orange')   
    # draw score
    canvas.draw_text(str(score), (550, 50), 50, 'White') 
    canvas.draw_text(word, (250, 200), 50, 'White') 
    
def keydown(key):
    global ball_pos, contro_vel 
    if key == simplegui.KEY_MAP["down"]:
        ball_pos[1] += contro_vel
    elif key == simplegui.KEY_MAP["up"]:
        ball_pos[1] -= contro_vel   

# create frame
frame = simplegui.create_frame("Motion", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.add_button('Restart', new_game, 100)
timer = simplegui.create_timer(50, tick)

# start frame
new_game()
frame.start()
timer.start()


