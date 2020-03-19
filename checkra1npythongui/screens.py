import pygame
import os
import time
import commands

global curScreen

pygame.font.init()
pygame.init()

try: 
    customScreen = open("resources/settings/CustomDimensions")
    customScreenLines = customScreen.readlines()
    customScreenWidth = customScreenLines[0]
    customScreenHeight = customScreenLines[1]
    (w, h) = (customScreenWidth, customScreenHeight)
    
except FileNotFoundError:
    print("No custom screen dimensions, falling back to default")
    (w, h) = (720, 480)

mainFont = pygame.font.Font("fonts/starmap.ttf", 20)
screen = pygame.display.set_mode((w, h))
#set the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
lightGrey = (200, 200, 200)
darkGrey = (50, 50, 50)
ultraDarkGrey = (25, 25, 25)
grey = (155, 155, 155)

global kahoot

#add some effects when something is tapped

def inDevelopment():
    global curScreen
    
    print("area closed for now... come back soon...")
    curScreen = 4
    
    sorryText = mainFont.render("This area is currently in development.", False, white)
    sorryText2 = mainFont.render("Please come back later. :)", False, white)
    #insert construction image here
    
    screen.blit(sorryText, (300, 30))
    screen.blit(sorryText2, (300, 70))

def dKeys ():
    print("loading dKeys")
    
    #make sure that you cant tap things behind it.
    #add button that hides the buttons like on that LG so that stuff behind it can be pressed.sudo
    
    backBar = pygame.Rect(0, 420, w, 75)
    backButton = pygame.Rect(200, 420, 100, 100)
    homeButton = pygame.Rect(250, 420, 100, 100)
    
    pygame.draw.rect(screen, ultraDarkGrey, backBar)
    pygame.draw.polygon(screen, white, ((260, 430), (230, 450), (260, 470)), 6)
    pygame.draw.circle(screen, white, (350, 450), 23, 6)
    
def checkra1n():
    import commands
    global curScreen
    #remember to add instrustions on how to install checkra1n or add that to the installation.
    #dont need sudo to add the repo
    curScreen = 1
    
    startButton = pygame.Rect(35, 35, 200, 200)
    homeButton = pygame.Rect(250,250, 100, 100)
    
    startText = mainFont.render("start", False, white)
    
    pygame.draw.rect(screen, darkGrey, homeButton)
    pygame.draw.rect(screen, darkGrey, startButton)
    
    screen.blit(startText, (60, 60))
    print("")
    
    while curScreen == 1:
        pygame.display.flip()
        #print("here")
        #stops the loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
                pygame.quit()
                
        mousePosition = pygame.mouse.get_pos()
        mouseButton = pygame.mouse.get_pressed()
        #print(mouseButton)
        #print(mousePosition)
        
        
        #maybe add some def for this to make less and nicer looking code?
        if curScreen == 1 and homeButton.collidepoint(mousePosition) and mouseButton > (0, 0, 0):
            print("going back to home")
            curScreen = 0
            #shomeScreen()
            time.sleep(0.1)
        elif curScreen == 1 and startButton.collidepoint(mousePosition) and mouseButton > (0, 0, 0):
            print("pressed start")
            commands.checkra1n("-c")
    
def rcmLoader():
    print("loading rcmLoader")
    
def kahoot():
    global curScreen
    
    curScreen = 3
    spamCount = 20
    spamCountSTR = str(spamCount)
     
    spamStartButton = pygame.Rect(35, 35, 200, 200)
    spamStopButton = pygame.Rect(35, 260, 200, 200)
    spamCountUp = pygame.Rect(250, 35, 100, 100)
    spamCountDown = pygame.Rect(250, 300, 100, 100)
    homeButton = pygame.Rect(250,250, 100, 100)
    spamCountText = mainFont.render(spamCountSTR, False, white)
    
    
    pygame.draw.rect(screen, green, spamStartButton)
    pygame.draw.rect(screen, red, spamStopButton)
    pygame.draw.rect(screen, darkGrey, spamCountUp)
    pygame.draw.rect(screen, darkGrey, spamCountDown)
    pygame.draw.rect(screen, darkGrey, homeButton)
    
    screen.blit(spamCountText, (250, 300))
    
    #if button pressed
    kahootSpamming = True
    
    while kahootSpamming:
        
        pygame.display.flip()
        #print("here")
        #stops the loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
                pygame.quit()
        mousePosition = pygame.mouse.get_pos()
        mouseButton = pygame.mouse.get_pressed()
        #print(mouseButton)
        #print(mousePosition)
        
        if curScreen == 3 and homeButton.collidepoint(mousePosition) and mouseButton > (0, 0, 0):
            print("going back to home")
            curScreen = 0
            #shomeScreen()
            time.sleep(0.1)
            break
     
def settings():
    print("settings")
    