1
import os
import pygame as pg
import wget
#To be used soon
#import keyboard

version = "1"
devmode = False
running = True
devKeyword = ""
#checks for old update files, if they exist, delete le files
try:
    os.remove("availableUpdate.py")
    print("Old update files removed")
except FileNotFoundError:
    print("No old update files to delete.")

try: 
    #Check for dev mode, if no devmode file is present, put it into release mode
    devFileCheck = open("devmode")
    devLines = devFileCheck.readlines()
    devKeyword = devLines[0]
    if devKeyword == "developer":
        devmode = True
        print("Developer Mode")
    else:
        devmode = False
        print("Release Mode")
    
    
except FileNotFoundError:
    print("Release Mode")
    
#checks for the dev term
if devKeyword == "developer":
    devmode = True
    print("Developer Mode")
else:
    devmode = False
    print("Release Mode")

#Checks for updates, but only if NOT in developer mode!
if devmode == False:
    linkToUpdate = "https://raw.githubusercontent.com/shortbow123/checkra1npython/master/program.py"
    wget.download(linkToUpdate, 'availableUpdate.py')
    availableUpdateFile = open("availableUpdate.py", "r")
    updateLines = availableUpdateFile.readlines()
    availableVersion = updateLines[1]
    print("Currently, version "+availableVersion+"is available on GitHub.")
    if availableVersion > version:
        print("An update is available.")
        print("Starting update now...")
        os.system('python3 update.py')

#Again, try to delete le files
try:
    os.remove("availableUpdate.py")
    print("Update files removed")
except FileNotFoundError:
    print("No update files to delete.")

#Make sure the display is inizialized, if not initialize it
if pg.display.get_init() != 1: 
    pg.display.init()
    print("display initialized")

#make sure to add instructions in installation
#check for existing file with screen dimensions
    #apply dimentions

#sets initial screen size, made for my 3.5" screen :)
(w, h) = (720, 480)

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