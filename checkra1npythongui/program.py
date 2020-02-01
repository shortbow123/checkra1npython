import os
import pygame as pg
import wget
import time
#To be used soon
#import keyboard

#add config.txt for font saving and all settings
version = "2"
#revision = "2" TO BE ADDED SOON IN BETA UPDATE
devmode = False
running = True
devKeyword = ""
pg.font.init()

mainFont = pg.font.Font("fonts/starmap.ttf", 20)

#checks for old update files, if they exist, delete le file
try:
    os.remove("availableVersion.py")
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
    
#Enabled until it is working correctly on my rpi :(
devmode = True

#Checks for updates, but only if NOT in developer mode!
if devmode == False:
    versionFile = open("version", "w")
    versionFile.write(version)
    versionFile.close()
    wget.download('https://raw.githubusercontent.com/shortbow123/checkra1npython/master/checkra1npythongui/version', 'availableVersion')
    availableVersion = open("availableVersion", "r")
    versionLines = availableVersion.readlines()
    availableVersion = versionLines[0]
    print("\n Version "+availableVersion+" is available on GitHub, the current version is "+version+".")
    if availableVersion > version:
        print("An update is available.")
        print("Starting update now...")
        os.system('python3 update.py')
        
#Again, try to delete le files
try:
    os.remove("availableVersion.py")
    print("Update files removed")
except FileNotFoundError:
    print("No update files to delete.")

#Make sure the display is inizialized, if not initialize it
if pg.display.get_init() != 1: 
    pg.display.init()
    print("display initialized")

#Checks for custom screen dimensions, if there is no custom dimentions, falls back to default.
try: 
    customScreen = open("resources/settings/CustomDimensions")
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
lightGrey = (200, 200, 200)
darkGrey = (50, 50, 50)
grey = (155, 155, 155)
test1 = 0
test2 = 2
test3 = 4

#sets the screen
screen = pg.display.set_mode((w, h))

def homeScreen():
    global curScreen
    global checkra1nButton
    global rcmButton
    global button3
    global button4
    global button5
    global settingsButton
    screen.fill(black)
    curScreen = 0
    
    #Give dimensions and locations of the buttons
    checkra1nButton = pg.Rect(35, 35, 200, 200)
    rcmButton = pg.Rect(35, 260, 200, 200)
    button3 = pg.Rect(260, 36, 200, 200)
    button4 = pg.Rect(260, 260, 200, 200)
    button5 = pg.Rect(485, 37, 200, 200)
    settingsButton = pg.Rect(485, 260, 200, 200)

    
    #Give text to the buttons
    checkra1nText = mainFont.render("checkra1n test", True, white)
    rcmText = mainFont.render("RCM payloads", True, white)
    text3 = mainFont.render("3rd Option", False, white)
    text4 = mainFont.render("4th Option", False, white)
    text5 = mainFont.render("5th Option", False, white)
    settingsText = mainFont.render("Settings", False, white)
    
    print("here")
    pg.draw.rect(screen, darkGrey, checkra1nButton)
    pg.draw.rect(screen, darkGrey, rcmButton)
    pg.draw.rect(screen, darkGrey, button3)
    pg.draw.rect(screen, darkGrey, button4)
    pg.draw.rect(screen, darkGrey, button5)
    pg.draw.rect(screen, darkGrey, settingsButton)
    
    #put the text + images on the stuff
    screen.blit(checkra1nText, (57, 125))
    screen.blit(rcmText, (70, 350))
    screen.blit(text3, (300, 125))
    screen.blit(text4, (300, 350))
    screen.blit(text5, (525, 125))
    screen.blit(settingsText, (540, 350))
    
homeScreen()
running = True
while running:
    
    #flips display to see changes
    screen.fill(blue)
    pg.display.flip()

    #stops the loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 
            pg.quit()
    mousePosition = pg.mouse.get_pos()
    mouseButton = pg.mouse.get_pressed()
    #get_display active == false:
        #make it active
    
    if curScreen == 0 and checkra1nButton.collidepoint(mousePosition) and mouseButton > (0, 0, 0):
        print("switching to checkra1n")
        screen.fill(blue)
        time.sleep(0.1)
    elif curScreen == 0 and rcmButton.collidepoint(mousePosition) and mouseButton > (0, 0, 0):
        print("switching to rcm loader")
        screen.fill(lightGrey)
        time.sleep(0.1)
    elif curScreen == 0 and button3.collidepoint(mousePosition) and mouseButton > (0, 0, 0):
        print("switching to button3")
        screen.fill(black)
        time.sleep(0.1)
    elif curScreen == 0 and button4.collidepoint(mousePosition) and mouseButton > (0, 0, 0):
        print("switching to button4")
        screen.fill(black)
        time.sleep(0.1)
    elif curScreen == 0 and button5.collidepoint(mousePosition) and mouseButton > (0, 0, 0):
        print("switching to button5")
        screen.fill(black)
        time.sleep(0.1)
    elif curScreen == 0 and settingsButton.collidepoint(mousePosition) and mouseButton > (0, 0, 0):
        print("switching to settings pane")
        screen.fill(grey)
        time.sleep(0.1)