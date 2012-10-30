# "Stopwatch: The Game"

import simplegui

# define global variables
timer_int = 0
success_stops = 0
total_stops = 0
last_stop = 0

def format(timer_int):
    # helper function that converts integer counting tenths of
    # seconds into formatted string A:BC.D
    A = timer_int // 600
    B = timer_int % 600 // 100
    C = timer_int % 100 // 10 
    D = timer_int % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start_handler():
    tick.start()
    
def stop_handler():
    # stops timer and increments success and attempt counters
    # unless the stopwatch was already stopped. this code is
    # functional, but I would be interested to hear feedback from
    # experienced programmers if there is a more elegant method
    global timer_int, total_stops, success_stops, last_stop
    tick.stop()
    if last_stop != timer_int:
        total_stops = total_stops + 1
        if timer_int % 10 == 0:
            success_stops = success_stops + 1
    last_stop = timer_int
    
def reset_handler():
    # stops timer and resets timer and counters to zero
    global timer_int, total_stops, success_stops
    tick.stop()
    timer_int = 0
    total_stops = 0
    success_stops = 0

def draw(canvas):
    # draw helper function, which draws stopwatch and successful
    # and total attempt counters
    global timer_int, success_stops, total_stops
    canvas.draw_text(format(timer_int), (130, 175), 72, "White")
    canvas.draw_text(str(success_stops) + "/" + str(total_stops), (430, 40), 24, "Red")

def timer_handler():
    # define event handler for timer with 0.1 sec interval
    global timer_int
    timer_int = timer_int + 1

# create frame
frame = simplegui.create_frame("Stopwatch Game", 500, 300)

# register event handlers
start = frame.add_button("Start", start_handler)
stop = frame.add_button("Stop", stop_handler)
reset = frame.add_button("Reset", reset_handler)
tick = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw)

# start timer and frame
frame.start()