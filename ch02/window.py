##
# This program creates a graphics window with a rectangle. It provides the
# template used with all of the graphical programs used in the book
#

from ezgraphics import GraphicsWindow

# create the window and access the canvas
win = GraphicsWindow()
canvas = win.canvas()

#draw on the canvas
canvas.drawRect(5,10,20,30)

#wait for the user to close the window
win.wait()
