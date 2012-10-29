# template for "Stopwatch: The Game"

import simplegui

# define global variables
timer_int = 0
success_stops = 0
total_stops = 0

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D
def format(timer_int):
    A = timer_int // 600
    B = timer_int % 600 // 100
    C = timer_int % 100 // 10 
    D = timer_int % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    tick.start()
    
def stop_handler():
    global timer_int, total_stops, success_stops
    tick.stop()
    total_stops = total_stops + 1
    if timer_int % 10 == 0:
        success_stops = success_stops + 1
    
def reset_handler():
    global timer_int, total_stops, success_stops
    tick.stop()
    timer_int = 0
    total_stops = 0
    success_stops = 0

def draw(canvas):
    global timer_int, success_stops, total_stops
    canvas.draw_text(format(timer_int), (130, 175), 72, "White")
    canvas.draw_text(str(success_stops) + "/" + str(total_stops), (430, 40), 24, "Red")

# define event handler for timer with 0.1 sec interval
def timer_handler():
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