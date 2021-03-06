# implementation of card game - Memory

import simplegui
import random

# all global variables are initialized via a call to init()
# this occurs on application launch and by pressing Restart button
def init():
    global deck, exposed, width, card, state, try1, try2, moves
    deck = [card % 8 for card in range(16)]
    random.shuffle(deck)
    exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    width = 800
    state = 0
    try1 = None
    try2 = None
    moves = 0
    label.set_text("Moves = " + str(moves))
    
# define event handlers
def mouseclick(pos):
    global card, state, try1, try2, deck, moves
    card = pos[0] // 50
    if exposed[card] == False:
        exposed[card] = True
        if state == 0:
            try1 = card
            state = 1
        elif state == 1:
            try2 = try1
            try1 = card
            state = 2
        else:
            if deck[try2] == deck[try1]:
                exposed[try1] = True
                exposed[try2] = True
            else:
                exposed[try1] = False
                exposed[try2] = False
            moves += 1
            label.set_text("Moves = " + str(moves))
            try1 = card
            state = 1

def draw(canvas):
    #each draw call determines whether card should be face up or down and draws respectively
    global deck, exposed, width, card, state
    textpos = 10
    i = 0
    xinc = 50
    for card in deck:
        xpos = width - (50 * (len(deck) - i))
        if exposed[i] == True:
            canvas.draw_polygon([(xpos,0), (xpos + xinc,0), (xpos + xinc,100), (xpos,100)], 2, "White")
            canvas.draw_text(str(card), [textpos,70], 48, "White")
        elif exposed[i] == False:
            canvas.draw_polygon([(xpos,0), (xpos + xinc,0), (xpos + xinc,100), (xpos,100)], 2, "White", "Black")
        i += 1
        textpos += 50
        xinc += 50

# creates frame, button, and label
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

# initializes global variables and beginning game state
init()

# registers event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# gets things rolling
frame.start()
