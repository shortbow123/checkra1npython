import os
import pygame as pg
import wget
#To be used soon
#import keyboard

version = "2"
#revision = "2" TO BE ADDED SOON IN BETA UPDATE
devmode = False
running = True
devKeyword = ""
#checks for old update files, if they exist, delete le file
try:
    os.remove("/checkra1npythongui/availableUpdate.py")
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
    versionFile = open("/checkra1npythongui/version", "w")
    versionFile.write(version)
    versionFile.close()
    linkToVersion = "https://raw.githubusercontent.com/shortbow123/checkra1npython/master/version"
    wget.download(linkToVersion, '/checkra1npythongui/availableVersion')
    availableVersion = open("/checkra1npythongui/availableVersion", "r")
    versionLines = availableVersion.readlines()
    availableVersion = versionLines[0]
    print("\n Version "+availableVersion+" is available on GitHub, the current version is "+version+".")
    if availableVersion > version:
        print("An update is available.")
        print("Starting update now...")
        os.system('python3 /checkra1npythongui/update.py')
        
#Again, try to delete le files
try:
    os.remove("/checkra1npythongui/availableUpdate.py")
    print("Update files removed")
except FileNotFoundError:
    print("No update files to delete.")

#Make sure the display is inizialized, if not initialize it
if pg.display.get_init() != 1: 
    pg.display.init()
    print("display initialized")

#Checks for custom screen dimensions, if there is no custom dimentions, falls back to default.
try: 
    customScreen = open("/resources/settings/CustomDimensions")
    customScreenLines = customScreen.readlines()
    customScreenWidth = customScreenLines[0]
    customScreenHeight = customScreenLines[1]
    (w, h) = (customScreenWidth, customScreenHeight)
    
except FileNotFoundError:
    print("No custom screen dimensions, falling back to default")
    (w, h) = (720, 480)

#set window name
pg.display.set_caption('checkra1npython')

#set the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

test1 = 0
test2 = 2
test3 = 4


#sets the screen
screen = pg.display.set_mode((w, h))

while running:
    #get_display active == false:
        #make it active
    
    test1 + 1
    test2 + 2
    test3 + 4
    
    if test1 >= 255 or test1 == 255:
        test1 = 0
    if test2 >= 255 or test2 == 255:
        test2 = 2
    if test3 >= 255 or test3 == 255:
        test3 = 4
    #set screen color to black
    screen.fill((test1, test2, test3))
    
    
    #stops the loop
    #for event in pg.event.get()
    #    if event.type == event.QUIT:
    #        running = False
    
    #flips display to see changes
    pg.display.update()
    pg.display.flip()