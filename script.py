#/usr/bin/python

# from turtle import *

# color('red', 'yellow')
# begin_fill()
# while True:
    # forward(200)
    # left(170)
    # if abs(pos()) < 1:
        # break
# end_fill()
# done()

import tkinter
import random

#create canvas using tkinter
haupt = tkinter.Tk()
c = tkinter.Canvas(haupt, bg="white", height=500, width=500)

x = 10
y = 10

#draw lines
for num in range(0,10):
	r = random.randint(1,100)
	r2 = random.randint(1,100)
	x2 = x+r
	y2 = y+r2
#	if x2 >= 500:
#		x2 = x-r
#
#	if y2 >= 500:
#		y2 = y -r
		
	line = c.create_line(x, y, x2, y2,fill='red')
	
	x = x2
	y = y2

c.pack()

haupt.mainloop()

