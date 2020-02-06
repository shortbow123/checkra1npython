import os
import pygame as pg
import wget
import time

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
    pg.display.init(
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
    checkra1nButton = pg.Rect(35, 25, 200, 200)
    rcmButton = pg.Rect(35, 250, 200, 200)
    button3 = pg.Rect(260, 26, 200, 200)
    button4 = pg.Rect(260, 250, 200, 200)
    button5 = pg.Rect(485, 27, 200, 200)
    settingsButton = pg.Rect(485, 250, 200, 200)


    #Give text to the buttons
    checkra1nText = mainFont.render("checkra1n test", True, white)
    rcmText = mainFont.render("RCM payloads", True, white)
    text3 = mainFont.render("3rd Option", False, white)
    text4 = mainFont.render("4th Option", False, white)
    text5 = mainFont.render("5th Option", False, white)
    settingsText = mainFont.render("Settings", False, white)

    print("here")
    #print(curScreen)
    pg.draw.rect(screen, darkGrey, checkra1nButton)
    pg.draw.rect(screen, darkGrey, rcmButton)
    pg.draw.rect(screen, darkGrey, button3)
    pg.draw.rect(screen, darkGrey, button4)
    pg.draw.rect(screen, darkGrey, button5)
    pg.draw.rect(screen, darkGrey, settingsButton)

    #put the text + images on the stuff
    screen.blit(checkra1nText, (57, 115))
    screen.blit(rcmText, (70, 340))
    screen.blit(text3, (300, 115))
    screen.blit(text4, (300, 340))
    screen.blit(text5, (525, 115))
    screen.blit(settingsText, (540, 340))

    pg.display.flip()


def checkra1nScreen():
    global curScreen

    print("switching to checkra1n screen")
    curScreen = 1
    screen.fill(black)

    #define the rectangles
    pwnButton = pg.Rect(35, 25, 450, 200)

    #text
    pwnText = mainFont.render("pwn ur i", False, white)

    #draw
    pg.draw.rect(screen, darkGrey, pwnButton)

    #put texts up

    screen.blit(pwnText, (200,200))



    print(curScreen)
    pg.display.flip()
    time.sleep(0.1)
    while curScreen == 1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
        mouseButton = pg.mouse.get_pressed()
        if mouseButton > (0, 0, 0):
            homeScreen()
            time.sleep(0.1)

def rcmLoaderScreen():
    global curScreen

    print("switching to rcm loader screen")
    curScreen = 2
    screen.fill(lightGrey)

    print(curScreen)
    pg.display.flip()
    time.sleep(0.1)
    while curScreen == 2:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
        mouseButton = pg.mouse.get_pressed()
        if mouseButton > (0, 0, 0):
            homeScreen()
            time.sleep(0.1)


def toolsScreen():
    global curScreen

    print("switching to tools pane")
    curScreen = 5
    screen.fill(black)

    wifiHotspotButton = pg.Rect(200, 200, 200, 200)
    webServerButton = pg.Rect(200, 200, 200, 200)

    while curScreen == 5:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
        mouseButton = pg.mouse.get_pressed()
        if mouseButton > (0, 0, 0):
            #wait until the mousebutton is up to switch screens maybe...
            time.sleep(0.1)
            homeScreen()


def settingsScreen():
    global curScreen

    print("switching to settings pane")
    curScreen = 6
    screen.fill(grey)

    displayButton = pg.Rect(200, 200, 200, 200)
    powerManagementButton = pg.Rect(200, 200, 200, 200)
    storageManagementButton = pg.Rect(200, 200, 200, 200)
    experimentalSettingsButton = pg.Rect(200, 200, 200, 200)



    print(curScreen)
    pg.display.flip()
    time.sleep(0.1)
    while curScreen == 6:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
        mouseButton = pg.mouse.get_pressed()
        if mouseButton > (0, 0, 0):
            homeScreen()
            time.sleep(0.1)


homeScreen()
running = True
while running:

    #stops the loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
    mousePosition = pg.mouse.get_pos()
    mouseButton = pg.mouse.get_pressed()
    #get_display active == false:
        #make it active

    #print(curScreen)

    if curScreen == 0 and checkra1nButton.collidepoint(mousePosition) and mouseButton > (0, 0, 0):
        checkra1nScreen()
        time.sleep(0.1)

    elif curScreen == 0 and rcmButton.collidepoint(mousePosition) and mouseButton > (0, 0, 0):
        rcmLoaderScreen()
        time.sleep(0.1)

    elif curScreen == 0 and button3.collidepoint(mousePosition) and mouseButton > (0, 0, 0):
        print("switching to button3")
        screen.fill(white)
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
        settingsScreen()
        time.sleep(0.1)
