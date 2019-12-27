import pygame as pg

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
blue = (0, 255, 0)
green = (0, 0, 255)

#sets the screen
screen = pg.display.set_mode((w, h))

while running:
    #get_display active == false:
    #make it active

    #set screen color to black
    screen.fill(black)
    
    #stops the loop
    #for event in pg.event.get()
    #    if event.type == event.QUIT:
    #        running = False
          
    #flips display to see changes
    pg.display.update()
    pg.display.flip()