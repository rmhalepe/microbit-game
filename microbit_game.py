'''Rachel Halepeska : pledged
In this game of catch, players must position the mitt to catch the balls
3 misses = game over'''
from microbit import *
import time
import math
import random

#displays all balls in the list
def show(li):
    for coord in li:
        x, y = coord[0], coord[1]
        display.set_pixel(x, y, 9)

#adds a new ball to the list (with random x coord)
def addNewBall(li):
    x = random.randint(0, 4)
    coord = (x, 0)
    li.append(coord)

#finds any ball that is in the last row
def checkForBall(li):
    for coord in li:
        y = coord[1]
        if y == 4:
            return coord
    return None

#checks whether a ball is in the same x position as the catcher
def didScore(coord, position):
    x = coord[0]
    if x == position:
        return True
    return False

#adds one to each y coord in the list, returns a new list
def updateList(li):
    newList = []
    for coord in li:
        x, y = coord[0], coord[1]
        newCoord = (x, y+1)
        newList.append(newCoord)
    return newList

misses = 0     #counts how many times a player has missed a ball
catcher = 0    #keeps track of the position of the mitt
loops = 0      #keeps track of the number of loops
score = 0      #counts how many times a player has caught a ball
list1 = []     #stores the balls currently in play

while misses < 3:
    display.clear()     #reset pixels for each loop
#every 5 loops move balls down a row
    if loops%5 == 0:
        list1 = updateList(list1)
#every other 5 loops (every 10 loops) add a new ball
        if loops%2:
            addNewBall(list1)

#handles button presses to move the catcher
    if button_a.is_pressed():
        catcher += -1
        if catcher < 0: catcher = 0
    if button_b.is_pressed():
        catcher += 1
        if catcher > 4: catcher = 4
    display.set_pixel(catcher, 4, 9)
    show(list1)
#checks for misses and scores, removes the ball or clears the list
    coord = checkForBall(list1)
    if coord is None:
        pass
    else:
        if didScore(coord, catcher):
            score += 1
            list1.remove(coord)
        else:
            misses += 1
            display.show(Image.SAD)
            time.sleep_ms(500)
            list1.clear()
    loops += 1
    time.sleep_ms(100)

#game over: displays score
while True:
    display.clear()
    text = "SCORE:"+str(score)
    display.scroll(text, loop=True)