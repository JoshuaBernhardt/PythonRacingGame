#Menu for Game

import pygame


def mainMenu():

    def beginGame():
        
        from game import gameStart
        pygame.display.init()
        gameStart()

    def openStore():
        from store import store
        pygame.display.init()
        store()
    
    class MenuOption:     #class object for menu text

        mouseOver=False   #Mouse is not over the item, will change if true

        def __init__(self, text, position):    #initialize item
            self.text=text                     #the item's text
            self.position=position             #position of item
            self.setRect()                     #Dimensions of text 
            self.draw()                        #Drawing of item on screen (blit)

        def draw(self):
            self.setRender()               
            screen.blit(self.render, self.rect) #Draw item on screen

        def getColour(self):
            if self.mouseOver:        #If mouse over text, text colour = yellow
                return(255,255,0)
            else:
                return(255,255,255)   #If not, text=white

        def setRender(self):
            self.render=menuFont.render(self.text, True, self.getColour())    #Rendering the text with colour

        def setRect(self):
            self.setRender()                   #Uses rendered text
            self.rect=self.render.get_rect()   #Gets the dimensions of the text
            self.rect.center=self.position       #Centres text on its position

    pygame.init()       #Initialise pygame module
    gameRunning=True    #Modifier for game quit function
    screen=pygame.display.set_mode((1200,1080),0)   #Set display to res of monitor with fullscreen
    pygame.display.set_caption("Game Menu")
    screenWidth=screen.get_rect().width     #Get width of screen
    screenHeight=screen.get_rect().height   #height of screen
    menuFont=pygame.font.SysFont("dejavsusans", 60)     #Defined font
    menuItems=[MenuOption("Start Game", (950,255)), MenuOption("Store(View Score)",(950,345)), #Using menu option class to create elements using criteria
           MenuOption("Exit",(950,535))]       #List object to minimise code with screen positions and text

    
        
    car=pygame.image.load("Car.png")
    van=pygame.image.load("Van.png")
    road=pygame.image.load("road.jpg")

    while gameRunning:   #whilst the game is running
        pygame.event.pump() #internally processes pygame event handlers
        pygame.display.update()
        screen.fill((99,99,99))      #fill background grey
        screen.blit(road,(100,600))
        screen.blit(road,(100,0))
        screen.blit(road,(1200,0))
        screen.blit(road,(1200,600))
        screen.blit(car,(430,800))
        screen.blit(van,(140,400))
        
        for item in menuItems:    #For each item in the menu item list
            if item.rect.collidepoint(pygame.mouse.get_pos()):   #If mouse is touching text
                MenuOption.mouseOver=True                        #Set boolean to true
            else:
                MenuOption.mouseOver=False                       #Set to false
            item.draw()    #Draw the item with either colour option

            if item==menuItems[0]:    #If first item 
                if pygame.mouse.get_pressed()[0] and item.rect.collidepoint(pygame.mouse.get_pos()):   #If text touching mouse and mouse clicked
                    beginGame()
                
            if item==menuItems[1]:
                if pygame.mouse.get_pressed()[0] and item.rect.collidepoint(pygame.mouse.get_pos()):
                    openStore()

            
  
        pygame.display.update()   #Update display

        if item==menuItems[2]:
                if pygame.mouse.get_pressed()[0] and item.rect.collidepoint(pygame.mouse.get_pos()):
                    gameRunning=False
                    pygame.quit()          #If the exit button is hovered over and the mouse is clicked, exit the menu

        #ent in pygame.event.get()
    
    
        

    
