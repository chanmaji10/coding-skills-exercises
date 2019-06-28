import numpy as np
import sys
from sys import argv
from time import sleep
import os
import curses

stdscr = curses.initscr()
field_range, survive, birth, threshold, time = [30, [2, 3], [3], 0.2, 100]
for i,arg in enumerate(argv[:]):
    if  i==0:
        continue
    s, v = arg.split('=')
    if s == 'field_range':
        field_range = int(v)
    if s == 'survive':
        survive = list(map(int, v[1:-1].split(','))) 
    if s == 'birth':
        birth = list(map(int, v[1:-1].split(','))) 
    if s == 'threshold':
        threshold = int(v) 
    if s == 'time':
        time = int(v) 

def field_print():
    stdscr.clear()
    l = ""
    for y in range(1, field_range+1):
        for x in range(1, field_range+1):
            if field[x,y]:
                l += " ■"
            else:
                l += " □"
        l += "\n"
    stdscr.addstr(0, 0,  l) 
    stdscr.refresh()  
    sleep(0.3)
    
field = np.random.random([field_range+2, field_range+2])
field = field < threshold

for _ in range(time):
    field_print()
    nextsites = []

    # judge
    for x in range(1, field_range+1):
        for y in range(1, field_range+1):
            if field[x,y]:
                neighber = np.sum(field[x-1:x+2, y-1:y+2])-1
                if neighber in survive:
                    nextsites.append((x, y))
            else:
                neighber = np.sum(field[x-1:x+2, y-1:y+2])
                if neighber in birth:
                    nextsites.append((x, y))

    field[:] = False
    for nextsite in nextsites:
        field[nextsite] = True