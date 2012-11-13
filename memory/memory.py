# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def init():
    global deck, exposed, xpos
    deck = [card % 8 for card in range(16)]
    random.shuffle(deck)
    exposed = [True, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False]
    xpos = 0
    print deck
    print exposed
    
# define event handlers
def mouseclick(pos):
    global deck
    pass
    

# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck, exposed, xpos
    pos = 10
    i = 0
    for card in deck:
        if exposed[i] == True:
            canvas.draw_text(str(card), [pos,70], 48, "White")
            pos += 50
        elif exposed[i] == False:
            canvas.draw_polygon([(xpos,0), (xpos + 50,0), (xpos + 50, 100), (xpos, 100)], 2, "White", "Black")
            pos += 50
        canvas.draw_text(str(deck), [25,90], 12, "White")
        i += 1
        xpos += 50
        
#    canvas.draw_text(str(deck), [25,90], 12, "White")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
l=frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric