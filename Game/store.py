#Store

import pygame

def loadScore():    #load score file
    import pickle
    scoreFile=open(("scorefile.dat"),'rb')   #open
    totalScore=pickle.load(scoreFile)    #load score
    scoreFile.close()
    return totalScore

def writeScore(totalScore,cost):       #writes new score
    import pickle
    scoreFile=open(("scorefile.dat"),'wb')
    totalScore-=cost                      #adds on current game score
    pickle.dump(totalScore, scoreFile)   #write
    scoreFile.close()

def store():

    def goBack():
        
        from menu import mainMenu
        pygame.display.init()
        mainMenu()
    
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
    pygame.display.set_caption("Store")
    screenWidth=screen.get_rect().width     #Get width of screen
    screenHeight=screen.get_rect().height   #height of screen
    menuFont=pygame.font.SysFont("dejavsusans", 60)     #Defined font
    menuItems=[MenuOption("Car 1", (250,235)), MenuOption("Grass",(250,375)), #Using menu option class to create elements using criteria
          MenuOption("Car 2",(250,515)), MenuOption("Snow",(250,655)),MenuOption("Go Back",(250,800))]       #List object to minimise code with screen positions and text


        
    car=pygame.image.load("Car.png")
    van=pygame.image.load("Van.png")
    road=pygame.image.load("road.jpg")

    while gameRunning:   #whilst the game is running

        

        
        pygame.event.pump() #internally processes pygame event handlers
        pygame.display.update()
        screen.fill((99,99,99))      #fill background grey
        Cost1Text=menuFont.render("Cost: 0",True,(255,255,255))
        Cost2Text=menuFont.render("Cost: 0",True,(255,255,255))    #text items
        Cost3Text=menuFont.render("Cost: 1000",True,(255,255,255))
        Cost4Text=menuFont.render("Cost: 1500",True,(255,255,255))
        totalScoreReturn=str(loadScore())
        totalScoreText=menuFont.render("Total Score: "+totalScoreReturn,True,(255,255,255))
        screen.blit(Cost1Text,(600,220))        #display text
        screen.blit(car,(400,170))
        screen.blit(totalScoreText,(800,10))
        
        
        for item in menuItems:    #For each item in the menu item list
            if item.rect.collidepoint(pygame.mouse.get_pos()):   #If mouse is touching text
                MenuOption.mouseOver=True                        #Set boolean to true
            else:
                MenuOption.mouseOver=False                       #Set to false
            item.draw()    #Draw the item with either colour option

            if item==menuItems[0]:    #If first item 
                if pygame.mouse.get_pressed()[0] and item.rect.collidepoint(pygame.mouse.get_pos()):   #If text touching mouse and mouse clicked
                   unlock=True
                
            if item==menuItems[1]:
                if pygame.mouse.get_pressed()[0] and item.rect.collidepoint(pygame.mouse.get_pos()):     #Detect selection
                    unlock1=True

            if item==menuItems[2]:
                if pygame.mouse.get_pressed()[0] and item.rect.collidepoint(pygame.mouse.get_pos()):
                    if loadScore()<1000:
                        None
                    else:
                        writeScore(totalScore,1000)
                        
                    
  
        pygame.display.update()   #Update display

        if item==menuItems[3]:
                if pygame.mouse.get_pressed()[0] and item.rect.collidepoint(pygame.mouse.get_pos()):
                     print('d')
        if item==menuItems[4]:
            if pygame.mouse.get_pressed()[0] and item.rect.collidepoint(pygame.mouse.get_pos()):
                goBack()
        

    


