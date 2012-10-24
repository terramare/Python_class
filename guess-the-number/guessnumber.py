# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

# initialize global variables used in your code
num_range = 100
secret_number = 0

# define event handlers for control panel

def range100():
    # button that changes range to range [0,100) and restarts
    global secret_number
    secret_number = random.randrange(0, 101)
    return secret_number

def range1000():
    # button that changes range to range [0,1000) and restarts
    global secret_number
    secret_number = random.randrange(0, 1001)
    return secret_number

def get_input(guess):
    # main game logic goes here
    global secret_number
    print "You guessed " + guess
    print secret_number
    if guess == secret_number:
        print "Your guess is correct!"
    elif guess > secret_number:
        print "Lower"
    else:
        print "Higher"

# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)

# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_input("Enter a guess", get_input, 200)

# start frame
frame.start()