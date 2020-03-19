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

#add some effects when something is tapped
def didQuit():
    print("probably not")

def checkMouse():
    print("checking mouse")
    for event in pygame.event.GET():
        print("event")

def tap():
    print("tap or click recieved")
    
    
