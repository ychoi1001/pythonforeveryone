from ezgraphics import GraphicsWindow

#create the window and access the canvas
win = GraphicsWindow(400,200)
canvas = win.canvas()

#draw on the canvas
canvas.drawRect(0, 10, 200, 10)
canvas.drawRect(0, 30, 300, 10)
canvas.drawRect(0, 50, 100, 10)

#wait for the user to close the window
win.wait()
