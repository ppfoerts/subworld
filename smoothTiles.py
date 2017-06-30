#!/usr/bin/python

import tkinter
import random

#list for the map
virtualMap = [['blue' for x in range(500)] for y in range (500)]

def surroundingTiles(x,y):
    count = 0
    #get surrounding x and y tiles
    for adjx in range(x-1,x+2):
        for adjy in range(y-1,y+2):
            if(adjx >= 0 and adjx < 500 and adjy >= 0 and adjy < 500):
                if(adjx != x or adjy != y):
                    if(virtualMap[adjx][adjy] == 'green'):
                        count += 1
    return count
    
def smoothMap():
    for x in range(0,500):
        for y in range(0,500):
            neighbors = surroundingTiles(x,y)
            
            if(neighbors > 4):
                virtualMap[x][y] = 'green'
            elif(neighbors < 4):
                virtualMap[x][y] = 'blue'

if __name__ == "__main__":
    for x in range(0,500):
        for y in range(0,500):
            r = random.randint(99,100)
            color = 'red'
            if (r >= 100):
                color = 'green'
            else:
                color = 'blue'
                
            virtualMap[x][y] = color
            
    #create canvas using tkinter
    haupt = tkinter.Tk()
    c = tkinter.Canvas(haupt, bg="white", height=500, width=500)
    smoothMap()
    smoothMap()
            
    for num in range(0,500):
        for num2 in range(0,500):
            shiftx = num * 5
            shifty = num2 * 5
            square = c.create_polygon(0+shiftx,0+shifty,0+shiftx,5+shifty,5+shiftx,5+shifty,5+shiftx,0+shifty,fill=virtualMap[num][num2])
            

    c.pack()

    haupt.mainloop()