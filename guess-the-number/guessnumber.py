# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

# initialize global variables used in your code
num_range = 100
secret_number = 0
i = 7

# define event handlers for control panel

def init():
    global num_range
    if num_range == 100:
        range100()
        print "New Game. Enter a number between 0 and",num_range
    elif num_range == 1000:
        range1000()
        print "New Game. Enter a number between 0 and",num_range

def range100():
    # button that changes range to range [0,100) and restarts
    global secret_number
    global num_range
    global i
    i = 7
    num_range = 100
    secret_number = random.randrange(0, 101)
    return secret_number

def range1000():
    # button that changes range to range [0,1000) and restarts
    global secret_number
    global num_range
    global i
    i = 10
    num_range = 1000
    secret_number = random.randrange(0, 1001)
    return secret_number

def get_input(guess):
    # main game logic goes here
    global secret_number
    global i
    # print "Please enter a number between 0 and",num_range
    # if i == 0:
    print "You guessed " + guess
    print secret_number
    if int(guess) == secret_number:
        print "Your guess is correct!\n"
        init()
    elif int(guess) > secret_number:
        i = i - 1
        print "Lower"
        print "You have", i,"guesses left. Try again..\n"
    elif int(guess) < secret_number:
        i = i - 1
        print "Higher"
        print "You have", i,"guesses left. Try again..\n"
    if i == 0:
        print "You've run out of guesses. Try a new game.."
        init()
        
# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)

# register event handlers for control elements
frame.add_button("Range: 0 - 100", range100, 200)
frame.add_button("Range: 0 - 1000", range1000, 200)
frame.add_input("Enter a guess", get_input, 200)

# start frame
frame.start()

init()