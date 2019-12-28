1
import os
import pygame as pg
import wget
import keyboard

version = 1
#Check for dev mode, if no devmode file is present, put it into release mode
devFileCheck = open("devmode")
#Puts all the lines from the devmode file into the devLines var
devLines = devFileCheck.readlines()
#Puts only the first line into the variable
devFirstLine = devLines[1]
#checks for the dev term
if devLines == "developer":
    devmode = True
    print("Developer Mode")
except FileNotFoundError:
    print("Release Mode")

#Checks for updates, but only if NOT in developer mode!
if devmode:
    linkToUpdate = "https://raw.githubusercontent.com/shortbow123/checkra1npython/master/program.py"
    wget.download(linkToUpdate, 'availableUpdate.py')
    availableUpdateFile = open("availableUpdate.py", "r")
    updateLines = file.readlines()
    availableVersion = updateLines[1]
    print("Currently, version "+availableVersion+"is available on GitHub.")
    if availableVersion > version:
        print("An update is available.")
        print("Starting update now...")
        os.system('update.py')
os.remove("availableUpdate.py")
#availableUpdate = availableUpdateFile.readlines()
#firstLine = availableUpdate
#str(firstLine)
#print(firstLine)
#3line = 1
#or line in availableUpdate:
#    print("") 
#run program and print version to file then update or not

#make sure the display is inizialized, if not initialize it
print(pg.display.get_init())
if pg.display.get_init() != 1: 
    pg.display.init()
    print("display initialized")
 
#makes sure that the loop will run
running = True

#sets initial screen size
(w, h) = (400, 300)

#set window name
pg.display.set_caption('checkra1npython')

#set the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#sets the screen
screen = pg.display.set_mode((w, h))

while running:
    #get_display active == false:
    #make it active

    #set screen color to black
    screen.fill(blue)
    
    
    #stops the loop
    #for event in pg.event.get()
    #    if event.type == event.QUIT:
    #        running = False
    
    #if need to flip
        #then flip, set need to flip to false
    #flips display to see changes
    pg.display.update()
    pg.display.flip()