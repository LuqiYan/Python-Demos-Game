# miniproject Memory Game - by: Luqi

import simplegui
import random

# helper function to initialize globals
def new_game():
    global exposed, card_pos, turns, state, card_num1, card_num2, cards
    exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]    
    card_pos = [0, 0]
    turns = 0
    state = 0   
    card_num1 = 0
    card_num2 = 0  
    num1 = range(8)
    num2 = range(8)
    cards = num1 + num2
    random.shuffle(cards)   

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global card_pos, state, turns, cards, card_num1, card_num2, exposed
    card_pos = list(pos)
    card_num = card_pos[0] // 50
    if exposed[card_num] == False:
        if state == 0:
            card_num1 = card_num
            exposed[card_num1] = True
            state = 1
        elif state == 1:
            card_num2 = card_num
            exposed[card_num2] = True
            state = 2
            turns += 1
        else:
            if cards[card_num1] != cards[card_num2]:
                exposed[card_num1] = False
                exposed[card_num2] = False
            else:
                exposed[card_num1] = True
                exposed[card_num2] = True               
            card_num1 = card_num
            exposed[card_num1] = True
            state = 1
                      
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards, turns, exposed   
    for i in range(16):
        if exposed[i] == True:
            for num in cards:
                canvas.draw_text(str(cards[i]), (10 + 50 * i, 70), 50, "White")   
        else:  
            canvas.draw_line((25 + 50 * i, 0), (25 + 50 * i, 100), 48, 'Green')
    turnstr = "Turns = " + str(turns)
    label.set_text("Turns = " + str(turns))     
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
