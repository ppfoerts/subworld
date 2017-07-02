#!/usr/bin/python

import tkinter
import random
from PIL import Image
import pyscreenshot as ImageGrab
import time

#list for the map
height = 500
width = 500
virtualMap = [['blue' for x in range(width)] for y in range (height)]
smoothness = 4
white = (255,255,255)


def surroundingTiles(x,y):
    count = 0
    #get surrounding x and y tiles
    for adjx in range(x-1,x+2):
        for adjy in range(y-1,y+2):
            if(adjx >= 0 and adjx < height and adjy >= 0 and adjy < width):
                if(adjx != x or adjy != y):
                    if(virtualMap[adjx][adjy] == 'green'):
                        count += 1
    return count
    
def smoothMap():
    for x in range(0,height):
        for y in range(0,width):
            neighbors = surroundingTiles(x,y)
            
            if(neighbors > 4):
                virtualMap[x][y] = 'green'
            elif(neighbors < 4):
                virtualMap[x][y] = 'blue'

if __name__ == "__main__":
    for x in range(0,height):
        for y in range(0,width):
            r = random.randint(0,100)
            color = 'red'
            if (r >= 50):
                color = 'green'
            else:
                color = 'blue'
                
            virtualMap[x][y] = color
            
    
    
    for i in range(0,smoothness):
        smoothMap()
        
    #create canvas using tkinter
    haupt = tkinter.Tk()
    c = tkinter.Canvas(haupt, bg="white", height=height, width=width)
    
    for num in range(0,height):
        for num2 in range(0,width):
            shiftx = num * 5
            shifty = num2 * 5
            square = c.create_polygon(0+shiftx,0+shifty,0+shiftx,5+shifty,5+shiftx,5+shifty,5+shiftx,0+shifty,fill=virtualMap[num][num2])
      
        
    #c.update()
   
    c.pack()

    #create image
    #image1 = Image.new("RGB",(width,height),white)
    #draw = ImageDraw.Draw(image1)
    #time.sleep(3)
    #x = 100
    #y = 200
    #print(x,y)
    #filename = time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
    #ImageGrab.grab(bbox=(x,y,x+width,y+height)).save(filename + '.jpg')
    
    
    haupt.mainloop()
    