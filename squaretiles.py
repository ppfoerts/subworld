#!/usr/bin/python

import tkinter
import random

virtualMap = [['blue' for x in range(500)] for y in range (500)]

for x in range (0,500):
	for y in range(0,500):
		r = random.randint(-500,100)
		color = 'red'
		if (x >= 1 and y >= 1 and x <= 99 and y <= 99):
			if (virtualMap[x-1][y] == 'green' 
				or virtualMap[x][y-1] == 'green' 
				or virtualMap[x-1][y-1] == 'green'):
					r = random.randint(60,160)
			if (virtualMap[x-1][y] == 'green' and virtualMap[x][y-1] == 'green'):
				r = random.randint(90,180)
			if (virtualMap[x-1][y] == 'green' 
				and virtualMap[x][y-1] == 'green' 			
				and virtualMap[x-1][y-1] == 'green'):
					r = random.randint(99,200)
			if (virtualMap[x-1][y-1] == 'green' and virtualMap[x-1][y] == 'blue' and virtualMap[x][y-1] == 'blue'):
				r = random.randint(0,100)
				
		if (r >= 100):
			color = 'green'
		else:
			color = 'blue'
		virtualMap[x][y] = color 

#create canvas using tkinter
haupt = tkinter.Tk()
c = tkinter.Canvas(haupt, bg="white", height=500, width=500)

for num in range(0,500):
	for num2 in range(0,500):
		shiftx = num * 5
		shifty = num2 * 5
		square = c.create_polygon(0+shiftx,0+shifty,0+shiftx,5+shifty,5+shiftx,5+shifty,5+shiftx,0+shifty,fill=virtualMap[num][num2])

c.pack()

haupt.mainloop()