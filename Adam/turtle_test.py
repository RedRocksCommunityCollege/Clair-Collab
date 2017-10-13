import turtle
import curses

def Reset():
    turtle.goto(0,0)
    turtle.clear()

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

key = ''

while key != ord('q'):
    turtle.begin_fill()
    key = stdscr.getch()
    stdscr.addch(20,25,key)
    stdscr.refresh()
    if key == curses.KEY_UP:
        turtle.forward(50)
        turtle.end_fill()
    elif key == curses.KEY_DOWN:
        turtle.backward(50)
        turtle.end_fill()
    elif key == curses.KEY_LEFT:
        turtle.left(10)
        turtle.end_fill()
    elif key == curses.KEY_RIGHT:
        turtle.right(10)
        turtle.end_fill()
    elif key == ord('c'):
        Reset()




curses.endwin()
