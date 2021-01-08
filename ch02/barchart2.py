from ezgraphics import GraphicsWindow

#create the window and access the canvas
win = GraphicsWindow(400,200)
canvas = win.canvas()

#draw on the canvas
canvas.setColor("red")
canvas.drawRect(0,10,200,10)

canvas.setColor("green")
canvas.drawRect(0,30,300,10)

canvas.setColor("blue")
canvas.drawRect(0,50,100,10)

win.wait()
