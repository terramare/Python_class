# template for "Stopwatch: The Game"

import simplegui
import math

# define global variables
timer_int = 0

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D
def format(timer_int):
	A = timer_int
    tenths = timer_int - math.floor(timer_int)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    tick.start()
    
def stop_handler():
    tick.stop()
    
def reset_handler():
    global timer_int
    tick.stop()
    timer_int = 0

def draw(canvas):
    global timer_int
    canvas.draw_text(str(timer_int), (50, 50), 24, "White")

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global timer_int
    timer_int = timer_int + 1
    print timer_int

# create frame
frame = simplegui.create_frame("Stopwatch Game", 300, 200)

# register event handlers
start = frame.add_button("Start", start_handler)
stop = frame.add_button("Stop", stop_handler)
reset = frame.add_button("Reset", reset_handler)
frame.set_draw_handler(draw)
tick = simplegui.create_timer(100, timer_handler)

# start timer and frame
frame.start()