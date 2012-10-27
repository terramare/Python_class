# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# import modules

import random
import simplegui

# global variable initialization

num_range = 100
secret_number = 0
i = 7

# event handlers for control panel


def init():
    # begins a new game
    global num_range
    if num_range == 100:
        range100()
    elif num_range == 1000:
        range1000()

def range100():
    # button that changes range to range [0,100)
    global secret_number
    global num_range
    global i
    i = 7
    num_range = 100
    secret_number = random.randrange(0, 101)
    print "New Game. Enter a number between 0 and",num_range

def range1000():
    # button that changes range to range [0,1000)
    global secret_number
    global num_range
    global i
    i = 10
    num_range = 1000
    secret_number = random.randrange(0, 1001)
    print "New Game. Enter a number between 0 and",num_range

def get_input(guess):
    # main game logic goes here
    global secret_number
    global i
    print "You guessed " + guess
    if int(guess) == secret_number:
        print "Your guess is correct!\n"
        init()
    elif int(guess) > secret_number:
        i = i - 1
        print "Lower"
        print "You have", i,"guesses left.\n"
    elif int(guess) < secret_number:
        i = i - 1
        print "Higher"
        print "You have", i,"guesses left.\n"
    if i == 0:
        print "You've run out of guesses. Try a new game.."
        init()
        
# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)

# registration of event handlers for control elements
frame.add_button("Range: 0 - 100", range100, 200)
frame.add_button("Range: 0 - 1000", range1000, 200)
frame.add_input("Enter a guess", get_input, 200)

# start frame
frame.start()

#call to begin game
init()